
from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^(?P<section_id>\d+)/themes/(?P<theme_id>\d+)/$', views.comments, name='comment'),
    url(r'^comment/addcomment/(?P<theme_id>\d+)/$', views.add_comment, name='add_comment'),
    url(r'^comment/deletecomment/(?P<comment_id>\d+)/$', views.del_comment, name='del_comment'),
    url(r'^theme/addtheme/(?P<section_id>\d+)/$', views.add_theme, name='add_theme'),
    url(r'^theme/deletetheme/(?P<theme_id>\d+)/$', views.del_theme, name='del_theme'),
    url(r'^section/deletesection/(?P<section_id>\d+)/$', views.del_section, name='del_section'),
    url(r'^section/addsection/$', views.add_section, name='add_section'),
    url(r'^(?P<section_id>\d+)/themes/$', views.themes, name='theme'),
    url(r'^', views.sections, name='main'),
]
