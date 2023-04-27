from django.urls import path
from . import views

urlpatterns = [
    path('api/item', views.ItemList.as_view(), name='item_list'), # api/items will be routed to the ItemList view for handling
    path('api/item/<int:pk>', views.ItemDetail.as_view(), name='item_detail'), 
]
