from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView

from transaction.forms import TransactionForm
from transaction.models import Transaction




class TransactionListView(ListView):
    model = Transaction
    context_object_name = 'transactions'
    ordering = ['-transaction_time']  


class TransactionCreateView(CreateView):
    model = Transaction
    form_class = TransactionForm
    # template_name = "transaction_form.html"
    success_url = reverse_lazy("transaction_list")

    def form_valid(self, form):
        transaction = form.instance
        product = transaction.product

        if transaction.entrance:
            product.inventory += transaction.inventory
        else:
            product.inventory -= transaction.inventory

        product.save()
        return super().form_valid(form)



