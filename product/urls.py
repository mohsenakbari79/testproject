from django.urls import path

from product.views import (
    PhoneListView,
    PhoneCreateView,
    PhoneUpdateView,
    PhoneDeleteView,
)

urlpatterns = [
    path("", PhoneListView.as_view(), name="phone_list"),
    path("create/", PhoneCreateView.as_view(), name="phone_create"),
    path("up/<int:pk>", PhoneUpdateView.as_view(), name="update_url"),
    path("del/<int:pk>", PhoneDeleteView.as_view(), name="delete_url"),
]
