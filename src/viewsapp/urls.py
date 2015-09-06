from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$',
        views.model_create,
        name='model_create'),
    url(r'^(?P<slug>[\w\-]+)/$',
        views.model_detail,
        name='model_detail'),
]
