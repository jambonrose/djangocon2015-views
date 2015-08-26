from django.shortcuts import (
    get_object_or_404, render)
from django.views.decorators.http import \
    require_http_methods

from .models import ExampleModel


@require_http_methods(['GET', 'HEAD'])
def model_detail(request, *args, **kwargs):
    request_slug = kwargs.get('slug')
    example_obj = get_object_or_404(
        ExampleModel, slug=request_slug)
    return render(
        request,
        'viewsapp/detail.html',
        {'object': example_obj})
