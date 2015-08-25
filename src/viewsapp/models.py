from django.db import models


class ExampleModel(models.Model):
    name = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)

    def __str__(self):
        return self.name.title()
