from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, ListView, UpdateView

from product.forms import PhoneForm, PhoneUpdateForm
from product.models import Phone


class PhoneListView(ListView):
    model = Phone
    paginate_by = 10

    def get_queryset(self):
        queryset = super().get_queryset()
        model_query = self.request.GET.get("model")
        brand_query = self.request.GET.get("brand")
        nationality_query = self.request.GET.get("nationality")
        self_sufficient = self.request.GET.get("self_sufficiency")
        if model_query:
            queryset = queryset.filter(model__icontains=model_query)
        if brand_query:
            queryset = queryset.filter(brand__name__icontains=brand_query)
        if nationality_query:
            queryset = queryset.filter(brand__nationality=nationality_query)
        if self_sufficient:
            if self_sufficient.isdigit() and int(self_sufficient) == 1:
                queryset = queryset.filter(contry=F("brand__nationality"))

        return queryset


class PhoneCreateView(CreateView):
    model = Phone
    form_class = PhoneForm
    success_url = reverse_lazy("phone_list")


class PhoneUpdateView(UpdateView):
    model = Phone
    form_class = PhoneUpdateForm
    success_url = reverse_lazy("phone_list")



class PhoneDeleteView(DeleteView):
    model = Phone
    success_url = reverse_lazy("phone_list")


