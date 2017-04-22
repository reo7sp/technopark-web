from django.conf.urls import url

from wsgi_test import views

urlpatterns = [
    url(r'^$', views.index, name='wsgi-test'),
]
