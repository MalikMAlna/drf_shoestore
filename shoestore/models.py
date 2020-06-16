from django.db import models


# Citation: Used this for URLField
# https://www.geeksforgeeks.org/urlfield-django-models/
class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    url = models.URLField(max_length=150)

    def __str__(self):
        return self.name


class ShoeType(models.Model):
    style = models.CharField(max_length=30)


class ShoeColor(models.Model):
    RED = 'R'
    YELLOW = 'Y'
    GREEN = 'G'
    BLUE = 'B'
    INDIGO = 'I'
    VIOLET = 'V'
    WHITE = 'WH'
    BLACK = 'BL'
    COLOR_NAME_CHOICES = [
        (RED, 'Red'),
        (YELLOW, 'Yellow'),
        (GREEN, 'Green'),
        (BLUE, 'Blue'),
        (INDIGO, 'Indigo'),
        (VIOLET, 'Violet'),
        (WHITE, 'White'),
        (BLACK, 'Black'),
    ]
    color_name = models.CharField(max_length=2, choices=COLOR_NAME_CHOICES)


class Shoe(models.Model):
    size = models.IntegerField()
    brand_name = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length=25)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length=25)
