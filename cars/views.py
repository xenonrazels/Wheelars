from django.shortcuts import render,get_object_or_404
from .models import  car
from django.core.paginator import  Paginator,PageNotAnInteger,EmptyPage
# Create your views here.
def cars(request):
    cars_list=car.objects.all()
    paginator=Paginator(cars_list, 4)
    page=request.GET.get('page')
    paginated_cars=paginator.get_page(page)
    state_search = car.objects.values_list('states', flat=True).distinct()
    brand_search = car.objects.values_list('brand', flat=True).distinct()
    transmission_search = car.objects.values_list('transmission', flat=True).distinct()
    year_search = car.objects.values_list('years', flat=True).distinct()
    body_search = car.objects.values_list('body_style', flat=True).distinct()
    data={
        'cars_list':paginated_cars,
        'state_search': state_search,
        'brand_search': brand_search,
        'year_search': year_search,
        'transmission_search': transmission_search,
        'body_style_search': body_search
    }
    print(transmission_search)
    return render(request,'cars/cars.html',data)

def car_details(request,id):
    details_page=get_object_or_404(car,pk=id)
    data={
        'car_detail':details_page,
    }
    return render(request,'cars/car_details.html',data)

def search(request):
    searched_cars=car.objects.order_by('-created_date')
    state_search = car.objects.values_list('states', flat=True).distinct()
    brand_search = car.objects.values_list('brand', flat=True).distinct()
    transmission_search = car.objects.values_list('transmission', flat=True).distinct()
    year_search = car.objects.values_list('years', flat=True).distinct()
    body_search = car.objects.values_list('body_style', flat=True).distinct()
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        if keywords:
            searched_car=searched_cars.filter(description__icontains=keywords ) or searched_cars.filter(car_title__icontains=keywords)
    if 'model' in request.GET:
        model= request.GET['model']

        if model:
            searched_car=searched_cars.filter(model__iexact=model)
    if 'location' in request.GET:
        location = request.GET['location']

        if location:
            searched_car=searched_cars.filter(states__iexact=location)
    if 'body_type' in request.GET:
        body_type = request.GET['body_type']

        if body_type:
            searched_car=searched_cars.filter(body_style__iexact=body_type)
    if 'year' in request.GET:
        year = request.GET['year']

        if year:
            searched_car=searched_cars.filter(years__iexact=year)
    if 'brand' in request.GET:
        brand = request.GET['brand']

        if brand:
            searched_car = searched_cars.filter(brand__iexact=brand)
    if 'transmission' in request.GET:
        transmission = request.GET['transmission']

        if transmission:
            searched_car = searched_cars.filter(transmission__iexact=transmission)

    data={
        'searched_cars':searched_car,
        'state_search': state_search,
        'brand_search': brand_search,
        'year_search': year_search,
        'transmission_search': transmission_search,
        'body_style_search': body_search,

    }
    return render(request,'pages/search.html',data)