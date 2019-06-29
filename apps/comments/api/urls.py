from django.conf.urls import url
from apps.comments.api.views import (
    CommentListAPIView,
    CommentDetailAPIView,
    CommentCreateAPIView,


)

app_name = 'comments-api'
urlpatterns = [
    url(r'^$', CommentListAPIView.as_view(), name='all'),
    url(r'^create/$', CommentCreateAPIView.as_view(), name='create'),
    url(r'^(?P<comment_id>\d+)$', CommentDetailAPIView.as_view(), name='thread'),
    # url(r'^(?P<comment_id>\d+)/edit$', CommentEditAPIView.as_view(), name='thread'),
    # url(r'^(?P<comment_id>\d+)/delete$', BlogDeleteAPIView.as_view(), name='delete')
]