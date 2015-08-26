from django.shortcuts import (
    get_object_or_404, redirect, render)
from django.views.generic import View

from .forms import ExampleForm
from .models import ExampleModel


class ModelDetail(View):

    def get(self, request, *args, **kwargs):
        request_slug = kwargs.get('slug')
        example_obj = get_object_or_404(
            ExampleModel, slug=request_slug)
        return render(
            request,
            'viewsapp/detail.html',
            {'object': example_obj})


class ModelCreate(View):
    context_object_name = 'form'
    form_class = ExampleForm
    template_name = 'viewsapp/form.html'

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            {self.context_object_name:
                self.form_class()})

    def post(self, request, *args, **kwargs):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(
            request,
            self.template_name,
            {self.context_object_name:
                bound_form})
