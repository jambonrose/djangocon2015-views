from django.views.generic import (
    CreateView, DetailView)

from .forms import ExampleForm
from .models import ExampleModel


class ModelDetail(DetailView):
    model = ExampleModel
    template_name = 'viewsapp/detail.html'


class ModelCreate(CreateView):
    context_object_name = 'form'
    form_class = ExampleForm
    template_name = 'viewsapp/form.html'
