from django.urls import path
from .views import home_view,ItemListView, ItemDetailView
app_name = 'item'
urlpatterns = [
    path('', home_view, name="home"),
    path('items/', ItemListView.as_view(), name="item"),
    path('items/<pk>', ItemDetailView.as_view(), name="detail"),
]
