from django.http import Http404
from django.shortcuts import render
import requests

from django.shortcuts import get_object_or_404

from main.models import Car, Sale, Client

def cars_list_view(request):
    # получите список авто
    template_name = 'main/list.html'
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, template_name, context)


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404

    template_name = 'main/details.html'
    car = get_object_or_404(Car, pk=car_id)
    context = {'car': car}
    return render(request, template_name, context)

def sales_by_car(request, car_id):
    # получите авто и его продажи
    template_name = 'main/sales.html'

    try:
        sales = Sale.objects.filter(car = car_id)
        context = {'sales': sales}
        return render(request, template_name, context)

    except Sale.DoesNotExist:
            raise Http404('Sale not found')



