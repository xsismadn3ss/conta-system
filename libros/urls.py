from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    # URLS para el inicio
    path('', views.index, name='index'),

    # URLS para Libros Mayores
    path('libros/', views.LibroMayorListView.as_view(), name='libros_list'),
    path('libros/nuevo/', views.LibroMayorCreateView.as_view(), name='libros_create'),
    path('libros/<int:pk>', views.libro_detail_view, name='libros_detail'),
    path('libros/<int:pk>/editar/', views.libro_update_view, name='libros_update'),
    path('libros/<int:pk>/eliminar/', views.libro_delete_view, name='libros_delete'),

    # URLS para Tipo
    path('tipos/', views.TipoListView.as_view(), name='tipo_list'),
    path('tipos/nueva/', views.TipoCreateView.as_view(), name='tipo_create'),
    path('tipos/<int:pk>', views.tipo_detail_view, name='tipo_detail'),
    path('tipos/<int:pk>/editar/', views.tipo_update_view, name='tipo_update'),
    path('tipos/<int:pk>/eliminar/', views.tipo_delete_view, name='tipo_delete'),
]
