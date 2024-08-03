from django.core.validators import MinValueValidator
from django.db import models

# Create your models here.


class Brand(models.Model):
    name = models.CharField("Name", max_length=25)
    nationality = models.CharField("Nationality", max_length=25)

    def __str__(self):
        return self.name


class Product(models.Model):
    model = models.CharField("Model", max_length=50, unique=True)
    price = models.IntegerField(
        "Price",
        default=1,
        validators=[
            MinValueValidator(0),
        ],
    )

    inventory = models.IntegerField(
        "Inventory",
        default=1,
        validators=[
            MinValueValidator(0),
        ],
    )
    brand = models.ForeignKey(
        "product.Brand", verbose_name="Brand", on_delete=models.CASCADE
    )
    contry = models.CharField("Contry", max_length=25)
    status = models.BooleanField("Stauts", default=True)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Productes"

    def __str__(self):
        return self.model


class Phone(Product):
    screnn_size = models.FloatField(
        verbose_name="Screen size",
        default=0,
        validators=[
            MinValueValidator(0),
        ],
    )
    color = models.CharField(verbose_name="Color", max_length=20)

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    def __str__(self):
        return super().__str__()