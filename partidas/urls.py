from django.urls import path
from . import views

app_name = 'partidas'

urlpatterns = [
    # inicio
    path('', view=views.index, name='index'),

    # partidas
    path('partidas/', view=views.PartidaListView.as_view(), name='partida_list'),
    path('partidas/nueva/', view=views.PartidaCreateView.as_view(), name='partida_create'),
    path('partidas/<int:pk>', view=views.partida_detail_view, name='partida_detail'),
    path('partidas/<int:pk>/editar', view=views.partida_update_view, name='partida_update'),
    path('partidas/<int:pk>/eliminar', view=views.jerarquia_delete_view, name='partida_delete'),

    # detalles
    path('detalles/', view=views.detalles_list_view, name='detalles_list'),
    path('detalles/nueva/', view=views.DetallesCreateView.as_view(), name='detalles_create'),
    path('detalles/<int:pk>', view=views.detalles_detail_view, name='detalles_detail'),
    path('detalles/<int:pk>/editar', view=views.detalles_update_view, name='detalles_update'),
    path('detalles/<int:pk>/eliminar', view=views.detalles_delete_view, name='detalles_delete')
]
