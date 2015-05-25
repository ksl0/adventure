from django.conf.urls import patterns, url
from polls import views

urlpatterns = patterns('', 
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', views.DetailView.as_view(), name ='detail'), 
    url(r'^(?P<pk>\d+)/results/$', views.ResultsView.as_view(), name='results'), 

    url(r'^(?P<pk>\d+)/vote/$', views.vote, name='vote'),
    url(r'^signup/$', views.signup, name='name'), 
    url(r'^exercise/$', views.get_exercise, name='run'), 
    url(r'^exercise/(?P<pk>\d+)/$', views.get_colors, name='runDetail')
)


