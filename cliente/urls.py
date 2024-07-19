from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('nosotros/', views.nosotros, name='Nosotros'),
    path('servicios/', views.servicios, name='Servicios'),
    path('registrocliente/',views.registrocliente, name='Registrocliente'),
    path('registroproveedor/',views.registroproveedor,name='Registroproveedor'),
    path('homecliente/',views.homecliente,name='homecliente'),
    path('conductores/', ConductoresListView.as_view(), name='conductores-list'),
    path('conductores/nuevo/', ConductoresCreateView.as_view(), name='conductores-create'),
    path('conductores/<int:pk>/editar/', ConductoresUpdateView.as_view(), name='conductores-update'),
    path('conductores/<int:pk>/eliminar/', ConductoresDeleteView.as_view(), name='conductores-delete'),
]