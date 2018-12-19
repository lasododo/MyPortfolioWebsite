import random
import os

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse


def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1, 18341264712)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename= new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename= new_filename,
        final_filename=final_filename
    )


class ProductQuerySet(models.query.QuerySet):
    def python_programs(self):
        return self.filter(python_check_box=True)

    def java_programs(self):
        return self.filter(java_check_boxe=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()


class Program(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    file = models.FileField(upload_to=upload_image_path, null=False, blank=False)
    python_check_box = models.BooleanField(default=False)
    java_check_box = models.BooleanField(default=False)

    objects = ProductManager()

    def get_absolute_url(self):
        # return "{slug}/".format(slug=self.slug)
        return reverse("xxx:list")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title
