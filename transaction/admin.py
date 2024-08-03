from django.contrib import admin

from transaction.models import Transaction

# Register your models here.


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("product", "inventory")
    search_fields = ("product",)


admin.site.register(Transaction, TransactionAdmin)