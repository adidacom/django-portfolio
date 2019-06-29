from django.conf.urls import url
from apps.blog.api.views import (
    BlogListAPIView,
    BlogDetailAPIView,
    BlogUpdateAPIView,
    BlogDeleteAPIView,
    BlogCreateAPIView,
)

app_name = 'blogs-api'
urlpatterns = [
    url(r'^$', BlogListAPIView.as_view(), name='all'),
    url(r'^(?P<slug>[\w-]+)$', BlogDetailAPIView.as_view(), name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit$', BlogUpdateAPIView.as_view(), name='update'),
    url(r'^create$', BlogCreateAPIView.as_view(), name='create'),
    url(r'^(?P<slug>[\w-]+)/delete$', BlogDeleteAPIView.as_view(), name='delete')
]