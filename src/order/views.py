from django.shortcuts import render

# Create your views here.
def home_view(request):
    return render(request, 'order/main.html', {})

def order_create_view(request):
    