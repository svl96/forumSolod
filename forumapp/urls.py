
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^\d+/themes/(?P<theme_id>\d+)/$', views.comments, name='comment'),
    url(r'^comment/addcomment/(?P<theme_id>\d+)/$', views.add_comment, name='add_comment'),
    url(r'^(?P<section_id>\d+)/themes/$', views.themes, name='theme'),
    url(r'^', views.sections, name='main'),
]
