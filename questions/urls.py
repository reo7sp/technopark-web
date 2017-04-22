from django.conf.urls import url

from questions import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hot$', views.hot, name='hot'),
    url(r'^tag/(?P<pk>[^/]+)$', views.tag, name='tag'),
    url(r'^question/(?P<pk>[0-9]+)$', views.question, name='question'),
    url(r'^logout$', views.logout, name='logout'),
    url(r'^login$', views.login, name='login'),
    url(r'^signup$', views.signup, name='signup'),
    url(r'^ask$', views.ask, name='ask'),
    url(r'^settings$', views.settings, name='settings'),
]
