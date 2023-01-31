from django.urls import path
from seguros import views

app_name = "seguros"

urlpatterns = [
    path("", views.home, name="home"),
    path("terms/", views.terms, name="terms"),
    path("privacidad/", views.privacidad, name="privacidad"),
    path("form/", views.tipo_form, name="tipo-form"),
    path("guardar-seguro/", views.GuardarSeguro.as_view(), name="guardar-seguro"),
    path("guardar-account/", views.guardar_account, name="guardar-account"),
    path("success/", views.success, name="success"),
    path("get-modelos-by-marca/", views.GetModeloByMarca.as_view(), name="get-modelos-by-marca"),
    path("get-versiones-by-modelo/", views.GetVersionesByModelo.as_view(), name="get-versiones-by-modelo"),
]