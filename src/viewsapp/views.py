from django.http import HttpResponseNotAllowed
from django.shortcuts import (
    get_object_or_404, render)

from .models import ExampleModel


def model_detail(request, *args, **kwargs):
    if request.method == 'GET':
        request_slug = kwargs.get('slug')
        example_obj = get_object_or_404(
            ExampleModel, slug=request_slug)
        return render(
            request,
            'viewsapp/detail.html',
            {'object': example_obj})
    return HttpResponseNotAllowed(['GET'])
