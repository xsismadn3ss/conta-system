from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from .models import Jerarquia, Tipo, Cuenta
from .forms import JerarquiaForm, TipoForm, CuentaForm
from django.shortcuts import redirect

# Catalogo inicio
@login_required
def index(request):
    return render(request, "catalogo_index.html")

# Jerarquia views
class JerarquiaListView(LoginRequiredMixin, ListView):
    model = Jerarquia
    template_name = "jerarquia/jerarquia_list.html"
    context_object_name = "jerarquias"

class JerarquiaCreateView(LoginRequiredMixin, CreateView):
    model = Jerarquia
    template_name = "jerarquia/jerarquia_form.html"
    fields = ["nombre"]
    success_url = reverse_lazy("catalogo:jerarquia_list")

@login_required
def jerarquia_detail_view(request, pk):
    try:
        jerarquia = Jerarquia.objects.get(pk=pk)
        return render(
            request, "jerarquia/jerarquia_detail.html", {"jerarquia": jerarquia}
        )
    except Jerarquia.DoesNotExist:
        return render(request, "jerarquia/jerarquia_not_found.html", status=404)


@login_required
def jerarquia_update_view(request, pk):
    try:
        jerarquia = Jerarquia.objects.get(pk=pk)
        if request.method == "POST":
            form = JerarquiaForm(request.POST, instance=jerarquia)
            if form.is_valid():
                form.save()
                return redirect("catalogo:jerarquia_list")
        else:
            form = JerarquiaForm(instance=jerarquia)
        return render(request, "jerarquia/jerarquia_form.html", {"form": form})
    except Jerarquia.DoesNotExist:
        return render(request, "jerarquia/jerarquia_not_found.html", status=404)

@login_required
def jerarquia_delete_view(request, pk):
    try:
        jerarquia = Jerarquia.objects.get(pk=pk)
        if request.method == "POST":
            jerarquia.delete()
            return redirect("catalogo:jerarquia_list")
        return render(
            request, "jerarquia/jerarquia_confirm_delete.html", {"object": jerarquia}
        )
    except Jerarquia.DoesNotExist:
        return render(request, "jerarquia/jerarquia_not_found.html", status=404)


# Tipo views
class TipoListView(LoginRequiredMixin, ListView):
    model = Tipo
    template_name = "tipo/tipo_list.html"
    context_object_name = "tipos"

class TipoCreateView(LoginRequiredMixin, CreateView):
    model = Tipo
    template_name = "tipo/tipo_form.html"
    fields = ["nombre"]
    success_url = reverse_lazy("catalogo:tipo_list")

@login_required
def tipo_detail_view(request, pk):
    try:
        tipo = Tipo.objects.get(pk=pk)
        return render(request, "tipo/tipo_detail.html", {"tipo": tipo})
    except Tipo.DoesNotExist:
        return render(request, "tipo/tipo_not_found.html", status=404)

@login_required # type: ignore
def tipo_update_view(request, pk):
    try:
        tipo = Tipo.objects.get(pk=pk)
        if request.method == "POST":
            form = TipoForm(request.POST, instance=tipo)
            if form.is_valid():
                form.save()
                return redirect("catalogo:tipo_list")
        else:
            form = TipoForm(instance=tipo)
            return render(request, "tipo/tipo_form.html", {"form": form})
    except Tipo.DoesNotExist:
        return render(request, "tipo/tipo_not_found.html", status=404)

@login_required
def tipo_delete_view(request, pk):
    try:
        tipo = Tipo.objects.get(pk=pk)
        if request.method == "POST":
            tipo.delete()
            return redirect("catalogo:tipo_list")
        return render(request, "tipo/tipo_confirm_delete.html", {"object": tipo})
    except Tipo.DoesNotExist:
        return render(request, "tipo/tipo_not_found.html",status=404)


# Cuenta views
class CuentaListView(LoginRequiredMixin, ListView):
    model = Cuenta
    template_name = "cuenta/cuenta_list.html"
    context_object_name = "cuentas"

class CuentaCreateView(LoginRequiredMixin, CreateView):
    model = Cuenta
    template_name = "cuenta/cuenta_form.html"
    fields = ["nombre", "tipo", "jerarquia", 'estado']
    success_url = reverse_lazy("catalogo:cuenta_list")

@login_required
def cuenta_detail_view(request, pk):
    try:
        cuenta = Cuenta.objects.get(pk=pk)
        return render(request, "cuenta/cuenta_detail.html", {"cuenta": cuenta})
    except Cuenta.DoesNotExist:
        return render(request, "cuenta/cuenta_not_found.html", status=404)

@login_required
def cuenta_update_view(request, pk):
    try:
        cuenta = Cuenta.objects.get(pk=pk)
        if request.method == "POST":
            form = CuentaForm(request.POST, instance=cuenta)
            if form.is_valid():
                form.save()
                return redirect("catalogo:cuenta_list")
        else:
            form = CuentaForm(instance=cuenta)
        return render(request, "cuenta/cuenta_form.html", {"form": form})
    except Cuenta.DoesNotExist:
        return render(request, "cuenta/cuenta_not_found.html", status=404)

@login_required
def cuenta_delete_view(request, pk):
    try:
        cuenta = Cuenta.objects.get(pk=pk)
        if request.method == "POST":
            cuenta.delete()
            return redirect("catalogo:cuenta_list")
        return render(request, "cuenta/cuenta_confirm_delete.html", {"object": cuenta})
    except Cuenta.DoesNotExist:
        return render(request, "cuenta/cuenta_not_found.html",status=404)

