from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import PartidaRegistro, Detalles
from .forms import PartidaForm, DetallesForm
from django.contrib.auth.mixins import LoginRequiredMixin

login_url='/login'

# Create your views here.
@login_required()
def index(request):
    return render(request, "partidas_index.html", status=200)

# Partida views
class PartidaListView(LoginRequiredMixin, ListView):
    model = PartidaRegistro
    template_name = 'partidas/partidas_list.html'
    context_object_name = 'jerarquias'
    login_url = '/'

class PartidaCreateView(LoginRequiredMixin, CreateView):
    model = PartidaRegistro
    template_name = 'partidas/partida_form.html'
    fields = ['titulo', 'descripcion']
    success_url = reverse_lazy('partidas:partida_list')

@login_required(login_url='/')
def partida_detail_view(request, pk):
    try:
        partida = PartidaRegistro.objects.get(pk=pk)
        return render(request, "partidas/partida_detail.html", {"partida": partida})
    except PartidaRegistro.DoesNotExist:
        return render(request, "partidas/partida_not_found.html")

@login_required(login_url='/')
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

@login_required(login_url='/')  
def jerarquia_delete_view(request: HttpRequest, pk):
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
@login_required(login_url='/')
def detalles_list_view(request):
    detalles = Detalles.objects.all()
    return render(request, 'detalles/detalle_list.html', {"detalles": detalles})

class DetallesCreateView(LoginRequiredMixin,CreateView):
    model = Detalles
    template_name = 'detalles/detalle_form.html'
    fields = ['monto_debe', 'monto_haber', 'partida', 'catalogo_cuentas']
    success_url = reverse_lazy('partidas:detalles_list')

@login_required(login_url='/')
def detalles_detail_view(request, pk):
    try:
        detalle = Detalles.objects.get(pk=pk)
        return render(request, "detalles/detalle_detail.html", {"detalle": detalle})
    except Detalles.DoesNotExist:
        return render(request, "detalles/detalle_not_found.html")

@login_required(login_url='/')   
def detalles_update_view(request: HttpRequest, pk):
    try:
        detalle = Detalles.objects.get(pk=pk)
        if request.method == 'POST':
            form = DetallesForm(request.POST, instance=detalle)
            if form.is_valid():
                form.save()
                return redirect('partidas:detalles_list')   
        else:
            form = DetallesForm(instance=detalle)
        return render(request, "detalles/detalle_form.html", {"form": form})
    except Detalles.DoesNotExist:
        return render(request, "detalles/detalle_not_found.html")
    
@login_required(login_url='/')
def detalles_delete_view(request: HttpRequest, pk):
    try:
        detalle = Detalles.objects.get(pk=pk)
        if request.method == "POST":
            detalle.delete()
            return redirect("partidas:detalles_list")
        return render(
            request, "detalles/detalle_confirm_delete.html", {"object": detalle}
        )
    except Detalles.DoesNotExist:
        return render(request, "detalles/detalle_not_found.html")