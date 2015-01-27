from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
           url(r'^$', views.QuestionListView.as_view(), name='index'),
           url(r'^detail/(?P<pk>\d+)/$', views.QuestionDetailView.as_view(),
                name ='detail'),
           url(r'^detail/(?P<pk>\d+)/update$',
           views.QuestionUpdateView.as_view(), name = 'update'))
