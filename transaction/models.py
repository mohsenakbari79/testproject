from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone


class Transaction(models.Model):
    product = models.ForeignKey(
        "product.Product", verbose_name="product", on_delete=models.CASCADE
    )
    inventory = models.IntegerField(
        "inventory",
        default=1,
        validators=[
            MinValueValidator(0),
        ],
    )
    entrance = models.BooleanField("entrance", default=True)
    transaction_time = models.DateTimeField("Transaction Time", default=timezone.now)

    class Meta:
        verbose_name = "Transaction"
        verbose_name_plural = "transactiones"
