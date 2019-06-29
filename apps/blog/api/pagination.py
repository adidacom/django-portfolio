from rest_framework.pagination import (
    LimitOffsetPagination,
    PageNumberPagination,
)


class BlogLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10


class BlogPageNumberPagination(PageNumberPagination):
    page_size = 2
