from django.conf.urls import url

from . import views

app_name = 'blog'
urlpatterns = [
    # ex: /blog/
    #url(r'^$', views.index, name='index'),
    
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    #url(r'^post/new/$', views.post_new, name='post_new'),
    
    # ex: /blog/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    
    # ex: /blog/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    
    # ex: /blog/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]

