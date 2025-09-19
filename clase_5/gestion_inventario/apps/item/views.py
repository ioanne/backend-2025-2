# from django.shortcuts import render
from django.views.generic import ListView

from apps.item.models import Item


# def item_list(request):
#     return render(
#         request=request,
#         template_name='items.html',
#         context={"products": Item.objects.all()},
#     )

class ItemTemplateView(ListView):
    template_name = "items.html"
    model = Item
    context_object_name = "products"
    ordering = ["-name"]
    paginate_by = 2

    def get_queryset(self):
        # extendemos el queryset para agregar un filtro por nombre
        queryset = super().get_queryset()
        filter_name = self.request.GET.get('filter_name')
        return queryset.filter(name__icontains=filter_name)




    # http://localhost:8000/items/list/?page=1