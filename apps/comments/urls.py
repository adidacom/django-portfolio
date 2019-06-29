from django.conf.urls import url
from . import views

app_name = 'comments'
urlpatterns = [
    # url(r'^blog$', views.allblogs, name='all'),
    url(r'^(?P<comment_id>\d+)$', views.comment_thread, name='thread'),
    # url(r'^blog/(?P<blog_id>\d+)/edit$', views.comment_update, name='comment_update'),
    # url(r'^blog/create$', views.create),
    url(r'^(?P<comment_id>\d+)/delete$', views.comment_delete, name='delete')
]