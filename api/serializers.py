from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer

from shoestore.models import Manufacturer, ShoeColor, ShoeType, Shoe


class ManufacturerSerializer(ModelSerializer):
    class Meta:
        model = Manufacturer
        fields = ('id', 'name', 'url')


class ShoeColorSerializer(ModelSerializer):
    class Meta:
        model = ShoeColor
        fields = ('color_name')


class ShoeTypeSerializer(ModelSerializer):
    class Meta:
        model = ShoeType
        fields = ('style')


class ShoeSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Shoe
        fields = (
            'id',
            'size',
            'brand_name',
            'manufacturer',
            'color',
            'material',
            'shoe_type',
            'fasten_type',
        )
