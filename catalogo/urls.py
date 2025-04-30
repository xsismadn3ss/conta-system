from django.urls import path
from . import views

app_name = 'catalogo'

urlpatterns = [
    # URLS para el inicio
    path('', views.index, name='index'),
    # URLs para Jerarquía
    path('jerarquias/', views.JerarquiaListView.as_view(), name='jerarquia_list'),
    path('jerarquias/nueva/', views.JerarquiaCreateView.as_view(), name='jerarquia_create'),
    path('jerarquias/<int:pk>/', views.jerarquia_detail_view, name='jerarquia_detail'),
    path('jerarquias/<int:pk>/editar/', views.jerarquia_update_view, name='jerarquia_update'),
    path('jerarquias/<int:pk>/eliminar/', views.jerarquia_delete_view, name='jerarquia_delete'),
    
    # URLs para Tipo
    path('tipos/', views.TipoListView.as_view(), name='tipo_list'),
    path('tipos/nuevo/', views.TipoCreateView.as_view(), name='tipo_create'),
    path('tipos/<int:pk>/', views.tipo_detail_view, name='tipo_detail'),
    path('tipos/<int:pk>/editar/', views.tipo_update_view, name='tipo_update'), # type: ignore
    path('tipos/<int:pk>/eliminar/', views.tipo_delete_view, name='tipo_delete'),
    
    # URLs para Cuenta
    path('cuentas/', views.CuentaListView.as_view(), name='cuenta_list'),
    path('cuentas/nueva/', views.CuentaCreateView.as_view(), name='cuenta_create'),
    path('cuentas/<int:pk>/', views.cuenta_detail_view, name='cuenta_detail'),
    path('cuentas/<int:pk>/editar/', views.cuenta_update_view, name='cuenta_update'),
    path('cuentas/<int:pk>/eliminar/', views.cuenta_delete_view, name='cuenta_delete'),
]