from django.urls import path
from .views import home_view,ItemListView, ItemDetailView
app_name = 'item'
urlpatterns = [
    path('', home_view, name="home"),
    path('items/', ItemListView.as_view()),
    path('items/<pk>', ItemDetailView.as_view(), name="detail"),
]
