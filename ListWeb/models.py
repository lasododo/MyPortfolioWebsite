import random
import os

from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse

from.utils import unique_slug_generator

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name, ext = os.path.splitext(base_name)
    return name, ext


def upload_image_path(instance, filename):
    print(instance)
    print(filename)
    new_filename = random.randint(1,18341264712)
    name, ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename= new_filename, ext=ext)
    return "products/{new_filename}/{final_filename}".format(
        new_filename= new_filename,
        final_filename=final_filename
    )


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

    def featured(self):
        return self.filter(featured=True, active=True)


class ProductManager(models.Manager):
    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset()


class Product(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(blank=True, unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to=upload_image_path, null=False, blank=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    objects = ProductManager()

    def get_absolute_url(self):
        return "{slug}/".format(slug=self.slug)

        # return reverse("products:detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title

    def __unicode__(self):
        return self.title


def product_pre_save_reciever(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(product_pre_save_reciever, sender=Product)
