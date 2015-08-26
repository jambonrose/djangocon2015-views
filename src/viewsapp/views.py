from django.shortcuts import redirect, render
from django.views.generic import DetailView, View

from .forms import ExampleForm
from .models import ExampleModel


class ModelDetail(DetailView):
    model = ExampleModel
    template_name = 'viewsapp/detail.html'


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
