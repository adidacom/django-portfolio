from django.db.models import Q
from django.contrib.auth import get_user_model, login, authenticate

from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

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
from apps.blog.api.pagination import BlogLimitOffsetPagination, BlogPageNumberPagination
from apps.blog.api.permissions import IsOwnerOrReadOnly


from .serializers import (
    UserCreateSerializer,
    UserLoginSerializer,

)
User = get_user_model()


class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()
    permission_classes = [AllowAny]


class UserLoginAPIView(APIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        user = authenticate(request, username=username, password=password)
        serializer = UserLoginSerializer(data=data)
        login(request, user)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

