from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.throttling import UserRateThrottle
from rest_framework.throttling import AnonRateThrottle


from advertisements.permissions import IsOwnerOrReadOnly

from advertisements.models import Advertisement
from advertisements.filters import AdvertisementFilter
from advertisements.serializers import AdvertisementSerializer



class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    #   сериализаторов и фильтров

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]
    filterset_class = AdvertisementFilter
    filterset_fields = ['created_at', 'status', 'creator']
    search_fields = ['created_at',]
    throttle_classes = [UserRateThrottle, AnonRateThrottle]


    """Получение прав для действий."""
    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAuthenticated()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []