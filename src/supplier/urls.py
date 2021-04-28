from django.urls import path
from .views import home_view
app_name = 'supplier'
urlpatterns = [
    path('', home_view, name="home"),

]
