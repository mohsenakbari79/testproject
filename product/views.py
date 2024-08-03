from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from product.models.product import Phone

from .forms import PhoneForm


class PhoneListView(ListView):
    model = Phone
    paginate_by = 2

    def get_queryset(self):
        phones = Phone.objects.filter(status=True)
        return phones


class PhoneCreateView(CreateView):
    model = Phone
    form_class = PhoneForm
    success_url = reverse_lazy("phone_list")


class PhoneUpdateView(UpdateView):
    model = Phone
    fields = ["price", "status", "inventory", "color"]
    success_url = reverse_lazy("phone_list")



class PhoneDeleteView(DeleteView):
    model = Phone
    success_url = reverse_lazy("phone_list")
