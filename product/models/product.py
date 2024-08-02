from django.db import models
from django.core.validators import MinValueValidator
# Create your models here.


class Brand(models.Model):
    name =  models.CharField("Name", max_length=25)
    nationality =  models.CharField("Nationality", max_length=25)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    model =  models.CharField("Model", max_length=50,unique=True)
    price = models.IntegerField(
        "Price",
        default=1,
        validators=[
            MinValueValidator(0),
        ])
    brand = models.ForeignKey("product.Brand", verbose_name="Natinal", on_delete=models.CASCADE)
    contry = models.CharField("Contry", max_length=25)
    status = models.BooleanField("Stauts")
    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Productes"

    def __str__(self):
        return self.name
    
    

class Phone(Product):
    screnn_size = models.FloatField(verbose_name="Screen size",default=0,validators=[
            MinValueValidator(0),
        ])
    

    class Meta:
        verbose_name = "Phone"
        verbose_name_plural = "Phones"

    def __str__(self):
        return super().__str__()

    

