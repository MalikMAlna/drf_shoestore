from rest_framework.viewsets import ModelViewSet

from api.serializers import ManufacturerSerializer, ShoeColorSerializer, ShoeTypeSerializer, ShoeSerializer
from shoestore.models import Manufacturer, ShoeColor, ShoeType, Shoe


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    basename = 'manufacturer'
    queryset = Manufacturer.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    basename = 'color_name'
    queryset = ShoeColor.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    basename = 'type'
    queryset = ShoeType.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    basename = 'shoe'
    queryset = Shoe.objects.all()
