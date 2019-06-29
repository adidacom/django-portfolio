from django.conf.urls import url
from . import views

app_name = 'blogs'
urlpatterns = [
    url(r'^$', views.allblogs, name='all'),
    url(r'^(?P<slug>[\w-]+)$', views.detail, name='detail'),
    url(r'^(?P<slug>[\w-]+)/edit$', views.update, name='update'),
    url(r'^blog/create$', views.create, name='create'),
    url(r'^(?P<slug>[\w-]+)/delete$', views.delete, name='delete')
]