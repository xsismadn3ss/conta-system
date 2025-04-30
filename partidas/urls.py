from django.urls import path
from . import views

app_name = 'partidas'

urlpatterns = [
    # partidas
    path('', view=views.partida_list_view, name='partida_list'),
    path('nueva/', view=views.partida_create_view, name='partida_create'),
    path('<int:pk>', view=views.partida_detail_view, name='partida_detail'),
    path('<int:pk>/editar', view=views.partida_update_view, name='partida_update'),
    path('<int:pk>/eliminar', view=views.partida_delete_view, name='partida_delete'),

    # detalles
    path('<int:pk>/detalles/nueva/', view=views.detalles_create_view, name='detalles_create'),
    path('<int:pk>/detalles/<int:detalle_id>', view=views.detalles_detail_view, name='detalles_detail'),
    path('<int:pk>/detalles/<int:detalle_id>/editar', view=views.detalles_update_view, name='detalles_update'),
    path('<int:pk>/detalles/<int:detalle_id>/eliminar', view=views.detalles_delete_view, name='detalles_delete'),
    path('<int:pk>/detalles', view=views.detalles_by_partida, name='partida_detalles'),
]
