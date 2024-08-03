from django.contrib import admin

from product.models.product import Brand, Phone, Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ("model", "brand")
    list_filter = ("status", "brand", "contry")
    search_fields = ("model",)


admin.site.register(Product, ProductAdmin)


class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "nationality")
    search_fields = ("name",)


admin.site.register(Brand, BrandAdmin)


class PhoneAdmin(admin.ModelAdmin):
    list_display = ("model", "brand")
    list_filter = ("status", "brand", "contry")
    search_fields = ("model", "color")


admin.site.register(Phone, PhoneAdmin)
