from django.db import models
from django.core.urlresolvers import reverse


class ExampleModel(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)

    def __str__(self):
        return self.name.title()

    def get_absolute_url(self):
        return reverse(
            'model_detail',
            kwargs={'slug': self.slug})
