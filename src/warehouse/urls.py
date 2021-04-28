from django.urls import path
from .views import home_view
app_name = 'warehouse'
urlpatterns = [
    path('', home_view, name="home"),
    # path('items/', ItemListView.as_view()),
    # path('items/<pk>', ItemDetailView.as_view(), name="detail"),
]
