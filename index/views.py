from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from .models import Category, Product, Model, Responsible, RoomsModel
from django.db.models import Count
from django.db.models import Q
from django.contrib.auth.decorators import login_required


def IndexCustom(request):
    query = Category.objects.annotate(count=Count('category'))
    query_count = Product.objects.filter(status=1).count()
    query_count_tw = Product.objects.filter(status=3).count()
    query_count_ir = Product.objects.filter(status=2).count()
    query_count_in = Product.objects.filter(status=0).count()
    context = {
        'query': query, 
        'query_count': query_count, 
        'query_count_tw': query_count_tw,
        'query_count_ir': query_count_ir,
        'query_count_in': query_count_in,
        }
    return render(request, 'catalog_category.html', context=context)


def Base(request, pk):
    query = Product.objects.filter(category_id__id=pk)
    return render(request, 'index.html', {'query': query})


def Detail(request, pk):
    query = Product.objects.filter(pk=pk)
    return render(request, 'detail.html', {'query': query})


def Categories(request):
    query = Category.objects.all()
    return render(request, 'card.html', {'query': query})


def DeviceModels(request):
    query = Model.objects.all()
    return render(request, 'models.html', {'query': query})


def Room(request):
    query = RoomsModel.objects.all()
    return render(request, 'rooms_catalog.html', {'query': query})


def ResponsiblePeople(request):
    query = Responsible.objects.all()
    return render(request, 'responsible_person.html', {'query': query})


class SearchResultsView(ListView):
    model = Product
    template_name = 'search_results.html'

    def get_queryset(self):
        query = self.request.GET.get('search')
        object_list = Product.objects.filter(
            Q(inventar_number__icontains=query)
        )
        return object_list


class ProductListView(TemplateView):
    template_name = 'file/product_add.html'

