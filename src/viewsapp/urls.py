from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create/$',
        views.ModelCreate.as_view(),
        name='model_create'),
    url(r'^(?P<slug>[\w\-]+)/$',
        views.ModelDetail.as_view(),
        name='model_detail'),
]
