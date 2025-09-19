from django.urls import path

# from apps.item.views import item_list
from apps.item.views import ItemTemplateView

urlpatterns = [
    path('list/', ItemTemplateView.as_view(), name='item_list')
]
# http://localhost:8000/items/list/