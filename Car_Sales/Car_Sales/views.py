from django.shortcuts import redirect,render
from Car.models import Car
from Brand.models import Car_Brand

def home(request,brand_slug=None):
    data  = Car.objects.all()

    if brand_slug is not None:
        brands = Car_Brand.objects.get(slug=brand_slug)
        data = Car.objects.filter(brand = brands)
    brands = Car_Brand.objects.all()
    return render(request, 'home.html',{'data':data,'brands':brands})