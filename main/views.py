from django.core.serializers import serialize
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework.generics import DestroyAPIView
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend

from main.serializers import BookSerializer, OrderSerializer
from main.models import Book, Order


@api_view(['GET'])
def books_list(request):
    """получите список книг из БД
     отсериализуйте и верните ответ
    """
    books = Book.objects.all()
    serializer = BookSerializer(books, many = True)

    return Response(serializer.data)


class CreateBookView(APIView):
    def post(self, request):
        # получите данные из запроса
        data = request.data
        query_book = Book.objects.filter(author = data['author'], title = data['title'])

        if query_book.exists():
            return Response({'massage': 'В библиотеке есть такая книга'})
        else:
            serializer = BookSerializer(data=data)
            #передайте данные из запроса в сериализатор
            if serializer.is_valid(raise_exception=True):
                #если данные валидны возвращаем ответ об этом
                serializer.save()
                return Response('Книга успешно создана')


class BookDetailsView(RetrieveAPIView):
    # реализуйте логику получения деталей одного объявления
    queryset = Book.objects.all()
    serializer = BookSerializer

    def get(self, request, pk):
        book = self.get_object()
        author = book.author
        title = book.title
        year = book.year
        return Response({'author': author, 'title': title,'year': year,})

class BookUpdateView(UpdateAPIView):
    # реализуйте логику обновления объявления

    def get_book(self, pk):
        return Book.objects.get(pk=pk)

    def patch(self, request, pk):
        test_book = self.get_book(pk)
        serializer = BookSerializer(test_book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response('Что-то пошло не так')


class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer = BookSerializer


class OrderViewSet(viewsets.ModelViewSet):
     # реализуйте CRUD для заказов
     queryset = Order.objects.all()
     serializer_class = OrderSerializer
     filter_backends = (filters.DjangoFilterBackend,)
     filter_fields = ('books',)



