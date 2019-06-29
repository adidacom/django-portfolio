from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,  # use ?search=, can chain with ?q= search
    OrderingFilter  # shows ordering of search, descending/ascending
)
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    CreateAPIView,
    RetrieveUpdateAPIView,
)
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)
from .pagination import BlogLimitOffsetPagination, BlogPageNumberPagination

from apps.blog.models import Blog

from .permissions import IsOwnerOrReadOnly

from .serializers import (
    BlogDetailSerializer,
    BlogListSerializer,
    BlogCreateUpdateSerializer,
)


class BlogCreateAPIView(CreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogListAPIView(ListAPIView):
    serializer_class = BlogListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = ['title', 'body', 'user__first_name']
    pagination_class = BlogPageNumberPagination  # PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # blogs_list = super(BlogListAPIView, self).get_queryset(*args, **kwargs)
        blogs_list = Blog.objects.all()
        query = self.request.GET.get('q')
        if query:
            blogs_list = blogs_list.filter(
                Q(title__icontains=query) |
                Q(body__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return blogs_list


class BlogDetailAPIView(RetrieveAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    permission_classes = [AllowAny]
    lookup_field = "slug"


class BlogUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogCreateUpdateSerializer
    lookup_field = "slug"

    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class BlogDeleteAPIView(DestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogDetailSerializer
    lookup_field = "slug"
    permission_classes = [IsOwnerOrReadOnly]
