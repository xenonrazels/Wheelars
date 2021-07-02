from django.shortcuts import render
from .models import Team
# Create your views here.
from cars.models import car


def home(request):
    Teams=Team.objects.all()
    Featured_cars=car.objects.order_by('-created_date').filter(is_featured=True)
    Latest_cars=car.objects.order_by('-created_date')
    # search_fields=car.objects.values('states','brand','model','years','body_style') #you can use distinct here also
    state_search=car.objects.values_list('states',flat=True).distinct()
    brand_search=car.objects.values_list('brand',flat=True).distinct()
    model_search=car.objects.values_list('model',flat=True).distinct()
    year_search=car.objects.values_list('years',flat=True).distinct()
    body_search=car.objects.values_list('body_style',flat=True).distinct()
    data={
        'teams':Teams,
        'featured_cars':Featured_cars,
        'latest_cars':Latest_cars,
        # 'search_fields':search_fields
        'state_search':state_search,
        'brand_search':brand_search,
        'year_search':year_search,
        'model_search':model_search,
        'body_style_search':body_search
    }

    return render(request, 'pages/home.html',data)

def about(request):
    Teams = Team.objects.all()
    data = {
        'teams': Teams
    }
    return render(request,'pages/about.html', data)
def services(request):
    return render(request,'pages/services.html')
def contact(request):
    return render(request, 'pages/contact.html')