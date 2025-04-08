from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from main.models import Product, Review
from main.serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer


@api_view(['GET'])
def products_list_view(request):
    # """реализуйте получение всех товаров из БД
    # реализуйте сериализацию полученных данных
    # отдайте отсериализованные данные в Response"""

    products = Product.objects.all()
    pr = ProductListSerializer(products, many=True)
    data = {'product': pr.data}
    return Response(data)

class ProductDetailsView(APIView):
    # """реализуйте получение товара по id, если его нет, то выдайте 404
    # реализуйте сериализацию полученных данных
    # отдайте отсериализованные данные в Response"""
    def get(self, request, product_id):
        try:
            details = Product.objects.filter(id=product_id)
            pr = ProductDetailsSerializer(details, many=True)
            product = { 'product':  pr.data,}
            return Response(product)

        except  Product.DoesNotExist:
            raise Http404('Product not found')



# доп задание:
class ProductFilteredReviews(APIView):
    def get(self, request, product_id):
        """обработайте значение параметра mark и
        реализуйте получение отзывов по конкретному товару с определённой оценкой
        реализуйте сериализацию полученных данных
        отдайте отсериализованные данные в Response"""
        pass
