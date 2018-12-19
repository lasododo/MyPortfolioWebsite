from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import VideoUpload


class ProductListView(ListView):
    queryset = VideoUpload.objects.all()
    template_name = "VideoList_final.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return VideoUpload.objects.all()


class ProductDetailSlugView(DetailView):
    queryset = VideoUpload.objects.all()
    template_name = "VideoDetail.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = VideoUpload.objects.get(slug=slug)
        except VideoUpload.DoesNotExist:
            raise Http404("Not Found........")
        except VideoUpload.MultipleObjectsReturned:
            qs = VideoUpload.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Hmmmm......")
        return instance


def product_list_view(request):
    queryset = VideoUpload.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "VideoList_final.html", context)
