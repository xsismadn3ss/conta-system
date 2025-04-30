from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import PartidaRegistro, Detalles
from .forms import PartidaForm, DetallesForm
from django.contrib.auth.mixins import LoginRequiredMixin


# Partida views
@login_required
def partida_list_view(request):
    partidas = PartidaRegistro.objects.all()
    return render(request, "partidas/partidas_list.html", {"partidas": partidas})


@login_required
def partida_create_view(request: HttpRequest):
    if request.method == "POST":
        form = PartidaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("partidas:partida_list")
    else:
        form = PartidaForm()
    return render(request, "partidas/partida_form.html", {"form": form})


@login_required
def partida_detail_view(request, pk):
    try:
        partida = PartidaRegistro.objects.get(pk=pk)
        return render(request, "partidas/partida_detail.html", {"partida": partida})
    except PartidaRegistro.DoesNotExist:
        return render(request, "partidas/partida_not_found.html")


@login_required
def partida_update_view(request, pk):
    try:
        partida = PartidaRegistro.objects.get(pk=pk)
        if request.method == "POST":
            form = PartidaForm(request.POST, instance=partida)
            if form.is_valid():
                form.save()
                return redirect("partidas:partida_list")
        else:
            form = PartidaForm(instance=partida)
        return render(request, "partidas/partida_form.html", {"form": form})
    except PartidaRegistro.DoesNotExist:
        return render(request, "partidas/partida_not_found.html")


@login_required
def partida_delete_view(request: HttpRequest, pk):
    try:
        partida = PartidaRegistro.objects.get(pk=pk)
        if request.method == "POST":
            partida.delete()
            return redirect("partidas:partida_list")
        return render(
            request, "partidas/partida_confirm_delete.html", {"object": partida}
        )
    except PartidaRegistro.DoesNotExist:
        return render(request, "partidas/partida_not_found.html")


# Detalles views
@login_required
def detalles_by_partida(request: HttpRequest, pk):
    try:
        partida = PartidaRegistro.objects.get(pk=pk)
        detalles = Detalles.objects.filter(partida=partida)
        return render(
            request,
            "detalles/detalle_list.html",
            {"detalles": detalles, "partida": partida},
        )
    except PartidaRegistro.DoesNotExist:
        return render(request, "partidas/partida_not_found.html")

@login_required
def detalles_create_view(request: HttpRequest, pk):
    if request.method == "POST":
        form = DetallesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("partidas:partida_detalles", pk=pk)
    else:
        form = DetallesForm()
    return render(request, "detalles/detalle_form.html", {"form": form, "pk": pk})


@login_required
def detalles_detail_view(request, detalle_id, pk):
    try:
        detalle = Detalles.objects.get(pk=detalle_id)
        print(detalle.partida.id)
        return render(request, "detalles/detalle_detail.html", {"detalle": detalle})
    except Detalles.DoesNotExist:
        return render(request, "detalles/detalle_not_found.html", {"pk": pk})


@login_required
def detalles_update_view(request: HttpRequest, detalle_id, pk):
    try:
        detalle = Detalles.objects.get(pk=detalle_id)
        if request.method == "POST":
            form = DetallesForm(request.POST, instance=detalle)
            if form.is_valid():
                form.save()
                return redirect("partidas:detalles_list")
        else:
            form = DetallesForm(instance=detalle)
        return render(request, "detalles/detalle_form.html", {"form": form, "pk": pk})
    except Detalles.DoesNotExist:
        return render(request, "detalles/detalle_not_found.html", {"pk": pk})


@login_required
def detalles_delete_view(request: HttpRequest, detalle_id, pk):
    try:
        detalle = Detalles.objects.get(pk=detalle_id)
        if request.method == "POST":
            detalle.delete()
            return redirect("partidas:detalles_list")
        return render(
            request,
            "detalles/detalle_confirm_delete.html",
            {"object": detalle, "pk": pk},
        )
    except Detalles.DoesNotExist:
        return render(request, "detalles/detalle_not_found.html", {"pk": pk})