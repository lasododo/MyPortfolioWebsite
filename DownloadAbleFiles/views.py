from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.http import Http404

from .models import Program


class ProductListView(ListView):
    queryset = Program.objects.all()
    template_name = "download_list.html"

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Program.objects.all()


class ProductDetailSlugView(DetailView):
    queryset = Program.objects.all()
    template_name = "download_details.html"

    def get_object(self, *args, **kwargs):
        request = self.request
        slug = self.kwargs.get('slug')
        # instance = get_object_or_404(Product, slug=slug, active=True)
        try:
            instance = Program.objects.get(slug=slug)
        except Program.DoesNotExist:
            raise Http404("Not Found........")
        except Program.MultipleObjectsReturned:
            qs = Program.objects.filter(slug=slug)
            instance = qs.first()
        except:
            raise Http404("Hmmmm......")
        return instance


def product_list_view(request):
    queryset = Program.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, "download_list.html", context)