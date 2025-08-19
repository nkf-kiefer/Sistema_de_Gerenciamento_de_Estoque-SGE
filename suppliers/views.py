from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from rest_framework import generics
from suppliers.serializers import SupplierSerializer
from . import models
from . import forms


class SupplierListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Supplier
    template_name = "supplier_list.html"
    context_object_name = "suppliers"
    paginate_by = 10
    permission_required = "suppliers.view_supplier"

    def get_queryset(self):
        queryset = super().get_queryset()
        name = self.request.GET.get("name")

        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset


class SupplierCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Supplier
    template_name = "supplier_create.html"
    form_class = forms.SupplierForm
    success_url = reverse_lazy("supplier_list")
    permission_required = "suppliers.add_supplier"


class SupplierUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Supplier
    template_name = "supplier_update.html"
    form_class = forms.SupplierForm
    success_url = reverse_lazy("supplier_list")
    permission_required = "suppliers.change_supplier"


class SupplierDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Supplier
    template_name = "supplier_delete.html"
    success_url = reverse_lazy("supplier_list")
    permission_required = "suppliers.delete_supplier"


class SupplierDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = models.Supplier
    template_name = "supplier_detail.html"
    permission_required = "suppliers.view_supplier"


class SupplierListCreateAPIView(generics.ListCreateAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = SupplierSerializer


class SupplierRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Supplier.objects.all()
    serializer_class = SupplierSerializer
