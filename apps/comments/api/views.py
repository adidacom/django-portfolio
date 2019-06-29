from django.db.models import Q

from rest_framework.filters import (
    SearchFilter,  # use ?search=, can chain with ?q= search
    OrderingFilter  # shows ordering of search, descending/ascending
)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

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
from apps.comments.api.pagination import CommentLimitOffsetPagination, CommentPageNumberPagination
from apps.blog.api.permissions import IsOwnerOrReadOnly


from apps.comments.models import Comment


from .serializers import (
    CommentListSerializer,
    CommentDetailSerializer,
    create_comment_serializer,

)


class CommentCreateAPIView(CreateAPIView):
    queryset = Comment.objects.all()
    # serializer_class = BlogCreateUpdateSerializer
    # permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        model_type = self.request.GET.get("type")
        slug = self.request.GET.get("slug")
        parent_id = self.request.GET.get("parent_id", None)
        return create_comment_serializer(
            model_type=model_type,
            slug=slug,
            parent_id=parent_id,
            user=self.request.user
        )


class CommentListAPIView(ListAPIView):
    serializer_class = CommentListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, OrderingFilter]
    ordering = 'created_at'
    search_fields = ['content', 'user__first_name']
    pagination_class = CommentPageNumberPagination  # PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        # blogs_list = super(BlogListAPIView, self).get_queryset(*args, **kwargs)
        comments_list = Comment.objects.filter(id__gte=0)
        query = self.request.GET.get('q')
        if query:
            comments_list = comments_list.filter(
                Q(content__icontains=query) |
                Q(user__first_name__icontains=query) |
                Q(user__last_name__icontains=query)
            ).distinct()
        return comments_list


class CommentEditAPIView(RetrieveAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "comment_id"


class CommentDetailAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    queryset = Comment.objects.filter(id__gte=0)
    serializer_class = CommentDetailSerializer
    lookup_field = "id"
    lookup_url_kwarg = "comment_id"
    permission_classes = [IsOwnerOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

# class BlogUpdateAPIView(RetrieveUpdateAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogCreateUpdateSerializer
#     lookup_field = "id"
#     lookup_url_kwarg = "blog_id"
#     permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#
#     def perform_update(self, serializer):
#         serializer.save(user=self.request.user)


# class BlogDeleteAPIView(DestroyAPIView):
#     queryset = Blog.objects.all()
#     serializer_class = BlogDetailSerializer
#     lookup_field = "id"
#     lookup_url_kwarg = "blog_id"
#     permission_classes = [IsOwnerOrReadOnly]
