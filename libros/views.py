from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.utils import timezone
from django.http.request import HttpRequest
from .models import LibroMayor, Tipo
from .forms import LibroMayorForm, TipoForm


# Libros Mayores inicio
@login_required
def index(request: HttpRequest):
    return render(request, "libros_index.html")


@login_required
def libro_list_view(request: HttpRequest):
    libros = LibroMayor.objects.all()
    can_edit = request.user.has_perm("libros.change_libromayor")  # type: ignore
    can_create = request.user.has_perm("libros.add_libromayor")  # type: ignore
    can_delete = request.user.has_perm("libros.delete_libromayor")  # type: ignore
    context = {
        "libros": libros,
        "can_edit": can_edit,
        "can_create": can_create,
        "can_delete": can_delete,
    }
    return render(
        request=request, template_name="libros/libros_list.html", context=context
    )


class LibroMayorCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    permission_required = "libros.add_libromayor"
    model = LibroMayor
    template_name = "libros/libros_form.html"
    fields = ["saldo_anterior", "movimiento", "tipo_movimiento", "cuenta"]
    success_url = reverse_lazy("libros:libros_list")


@login_required
def libro_detail_view(request: HttpRequest, pk: int):
    try:
        libro = LibroMayor.objects.get(pk=pk)
        return render(request, "libros/libros_detail.html", {"libro": libro})
    except LibroMayor.DoesNotExist:
        return render(request, "libros/libros_not_found.html")


@login_required
@permission_required(["libros.change_libromayor"], raise_exception=True)
def libro_update_view(request: HttpRequest, pk: int):
    try:
        libro = LibroMayor.objects.get(pk=pk)
        if request.method == "POST":
            form = LibroMayorForm(request.POST, instance=libro)
            if form.is_valid():
                libro.fecha_actualizacion = timezone.now()
                form.save()
                return redirect("libros:libros_list")
        else:
            form = LibroMayorForm(instance=libro)
        return render(request, "libros/libros_form.html", {"form": form})
    except LibroMayor.DoesNotExist:
        return render(request, "libros/libros_not_found.html")


@login_required
@permission_required(["libros.delete_libromayor"], raise_exception=True)
def libro_delete_view(request: HttpRequest, pk: int):
    try:
        libro = LibroMayor.objects.get(pk=pk)
        if request.method == "POST":
            libro.delete()
            return redirect("libros:libros_list")
        return render(request, "libros/libros_confirm_delete.html", {"libro": libro})
    except LibroMayor.DoesNotExist:
        return render(request, "libros/libros_not_found.html")


# Tipo views
class TipoListView(LoginRequiredMixin, ListView):
    model = Tipo
    template_name = "tipo/libro_tipo_list.html"
    context_object_name = "tipos"


class TipoCreateView(LoginRequiredMixin, CreateView):
    model = Tipo
    template_name = "tipo/libro_tipo_form.html"
    fields = ["nombre"]
    success_url = reverse_lazy("libros:tipo_list")


@login_required
def tipo_detail_view(request: HttpRequest, pk: int):
    try:
        tipo = Tipo.objects.get(pk=pk)
        prev = request.GET.get("prev")
        return render(
            request,
            "tipo/libro_tipo_detail.html",
            {"tipo": tipo, "prev": prev},
        )
    except Tipo.DoesNotExist:
        return render(request, "tipo/libro_tipo_not_found.html")


@login_required
def tipo_update_view(request: HttpRequest, pk: int):
    try:
        tipo = Tipo.objects.get(pk=pk)
        if request.method == "POST":
            form = TipoForm(request.POST, instance=tipo)
            if form.is_valid():
                form.save()
                return redirect("libros:tipo_list")
        else:
            form = TipoForm(instance=tipo)
        return render(request, "tipo/libro_tipo_form.html", {"form": form})
    except Tipo.DoesNotExist:
        return render(request, "tipo/libro_tipo_not_found.html")


@login_required
def tipo_delete_view(request: HttpRequest, pk: int):
    try:
        tipo = Tipo.objects.get(pk=pk)
        if request.method == "POST":
            tipo.delete()
            return redirect("libros:tipo_list")
        return render(request, "tipo/libro_tipo_confirm_delete.html", {"tipo": tipo})
    except Tipo.DoesNotExist:
        return render(request, "tipo/libro_tipo_not_found.html")
