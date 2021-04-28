from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item, ItemInstance
from .forms import ItemSearchForm
import pandas as pd
# Create your views here.
def home_view(request):

    item_df = None
    form = ItemSearchForm(request.POST or None)

    if request.method == "POST":
        date_from = request.POST.get('date_from')
        date_to = request.POST.get('date_to')
        status = request.POST.get('status')
        print(date_from, date_to, status)

        qs = Item.objects.filter(created__date__gte=date_from, created__date__lte=date_to)

        if len(qs) > 0:
           item_df = pd.Dataframe(qs.values())
        print(qs)
        # df2 = pd.Dataframe(qs.values_list())
    context = {
        'form': form, 
    }
    return render(request, 'item/main.html', context)

class ItemListView(ListView):
    template_name = 'item/items.html'
    model = Item
    # context_object_name = "obj"

class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/detail.html'

# def sale_list_view(request):
#     obj = Item.objects.all()
#     return render(request, 'item/items.html', {'object_list':obj})

# def sale_detail_view(request, pk):
#     object = Item.objects.get(pk=pk)
#     return render(request, 'item/detail.html', {'object_list':object})

