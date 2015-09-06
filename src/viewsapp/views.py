from decorator_plus import (
    require_form_methods, require_safe_methods)
from django.shortcuts import (
    get_object_or_404, redirect, render)

from .forms import ExampleForm
from .models import ExampleModel


@require_safe_methods
def model_detail(request, *args, **kwargs):
    request_slug = kwargs.get('slug')
    example_obj = get_object_or_404(
        ExampleModel, slug=request_slug)
    return render(
        request,
        'viewsapp/detail.html',
        {'object': example_obj})


@require_form_methods
def model_create(request, *args, **kwargs):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            new_obj = form.save()
            return redirect(new_obj)
    else:
        form = ExampleForm()
    return render(
        request,
        'viewsapp/form.html',
        {'form': form})
