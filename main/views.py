from django.http import Http404
from django.shortcuts import render
import requests


from main.models import Car, Sale, Client

def cars_list_view(request):
    # получите список авто
    template_name = 'main/list.html'
    cars = Car.objects.all()
    context = {'cars': cars}
    return render(request, template_name, context)  # передайте необходимый контекст


def car_details_view(request, car_id):
    # получите авто, если же его нет, выбросьте ошибку 404
    template_name = 'main/details.html'
    try:
        number = int(car_id) - 1
        car = Car.objects.all()[number]
        context = {'car': car}
        return render(request, template_name, context)
        # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')

def sales_by_car(request, car_id):
    # получите авто и его продажи
    template_name = 'main/sales.html'

    try:
        number = int(car_id)
        sales_all = Sale.objects.filter(car_id=number)
        id_clients_all = [sale.client_id for sale in sales_all]
        clients = Client.objects.filter(id__in=id_clients_all)
        # создаем список словарей,
        # предусматривая возможность нескольких продаж
        sales = []
        for client in clients:
            created = Sale.objects.get(car_id=number, client_id=client)
            sale = {'sale': {'client': {
                'last_name': client.last_name,
                'name': client.name,
                'middle_name': client.middle_name,
                'phone_number': client.phone_number,
                 },
                'created_at': created.created_at
            }}
            sales.append(sale)

        # создаем словарь, в котором зачения полей - список,
        # в случае нескольких продаж

        # sales = { 'client': {
        #     'last_name': [client.last_name for client in clients],
        #     'name': [client.name for client in clients],
        #     'middle_name': [client.middle_name for client in clients],
        #     'phone_number': [client.phone_number for client in clients],
        #      },
        #     'created_at': [sale.created_at for sale in sales_all]
        #     }

        context = {'sales': sales}


        return render(request, template_name, context)
        # передайте необходимый контекст
    except Car.DoesNotExist:
        raise Http404('Car not found')
