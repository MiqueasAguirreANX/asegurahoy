from django.shortcuts import render, redirect
from django.contrib import messages
import uuid
from seguros import forms
from seguros import models

from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

TIPO_FORM_MAP = {
    "auto": forms.AutoSeguroForm,
    "moto": forms.MotoSeguroForm,
    "accidentes": forms.AccidentesSeguroForm,
    "hogar": forms.HogarSeguroForm,
    "comercio": forms.ComercioSeguroForm,
    "bici": forms.BiciSeguroForm,
    "monopatin": forms.MonopatinSeguroForm,
    "camion": forms.CamionSeguroForm,
    "flota": forms.FlotaSeguroForm,
    "vida": forms.VidaSeguroForm,
    "praxis_medica": forms.PraxisMedicaSeguroForm,
    "caucion": forms.CaucionSeguroForm,
    "celular": None,
}

TIPO_MODEL_MAP = {
    "auto": models.AutoList,
    "moto": models.MotoList,
    "camion": models.CamionList,
}

def home(request):
    context = {}
    return render(request, "home.html", context)

def tipo_form(request):
    context = {}
    tipo = request.GET.get("tipo", None)
    if not tipo or tipo not in list(TIPO_FORM_MAP.keys()):
        messages.error(request, "Tipo de seguro invalido")
        return redirect("/")

    if tipo == "bici":
        context["tipo"] = tipo
        context["account_form"] = forms.AccountForm
        context["bici_form"] = forms.BiciSeguroForm
        context["monopatin_form"] = forms.MonopatinSeguroForm
    elif tipo == "flota":
        context["tipo"] = tipo
        context["account_form"] = forms.AccountForm
        context["form"] = TIPO_FORM_MAP[tipo]
        context["auto_form"] = forms.AutoSeguroForm
    else:
        context["tipo"] = tipo
        context["account_form"] = forms.AccountForm
        context["form"] = TIPO_FORM_MAP[tipo]
    return render(request, "seguros/form.html", context)


def guardar_seguro(request):
    if request.method == "POST":
        tipo = request.GET.get("tipo", None)
        if not tipo or tipo not in list(TIPO_FORM_MAP.keys()):
            messages.error(request, "Tipo de seguro invalido")
            return redirect("/")

        request.session["tipo"] = tipo

        if tipo == "flota":
            for auto in request.POST.get("autos"):
                auto_flota_form = forms.AutoFlotaSeguroForm(auto)
                if not auto_flota_form.is_valid():
                    messages.error(request, "Datos de seguro de auto de flota invalidos")
                    return redirect("/")
                
                auto_flota = auto_flota_form.save(commit=False)
                auto_flota.flota = obj
                auto_flota.save()
                obj.save()
        elif tipo == "bici":
            tipo_bici = request.POST.get("tipo-bici")
            if tipo_bici in ["bici","monopatin"]:
                form = TIPO_FORM_MAP[tipo_bici]
                form = form(request.POST)
                if form.is_valid():
                    form.save()
            else:
                messages.error(request, "Tipo Bici/Monopatin invalido")
                return redirect("/")
        else:
            form = TIPO_FORM_MAP[tipo]
            print(request.POST)
            form = form(request.POST)
            if not form.is_valid():
                print(form.errors)
                messages.error(request, "Datos de seguro invalidos")
                return redirect("/")

            obj = form.save()
        
        myuuid = uuid.uuid4()
        request.session["uuid"] = str(myuuid)
        user_seguro = models.UserSeguro(
            tipo=tipo,
            uuid=myuuid,
            data_id=int(obj.pk),
            completed=False,
        )
        user_seguro.save()
        return render(request, "seguros/account-form.html", {
            "tipo": tipo,
            "account_form": forms.AccountForm(),
        })
        
    return redirect("/") 


def guardar_account(request):
    if request.method == "POST":
        acc_form = forms.AccountForm(request.POST)
        if not acc_form.is_valid():
            messages.error(request, "Datos de cuenta invalidos")
            return redirect("/")
        
        tipo = request.session["tipo"]
        myuuid = request.session["uuid"]
        user_seguro = models.UserSeguro.objects.filter(tipo=tipo, uuid=str(myuuid))
        if not user_seguro.exists():
            messages.error(request, "Datos de seguro no cargados")
            return redirect("/")

        user_seguro = user_seguro.first()
        account = acc_form.save()
        user_seguro.account = account
        user_seguro.completed = True
        user_seguro.save()
        messages.success(request, "Seguro Creado")
        return redirect("/")

    return redirect("/")


class GetModeloByMarca(APIView):

    def get(self, request):
        marca = request.GET.get("marca")
        tipo = request.GET.get("tipo", None)
        if not tipo or tipo not in list(TIPO_FORM_MAP.keys()):
            messages.error(request, "Tipo de seguro invalido")
            return redirect("/")

        model = TIPO_MODEL_MAP[tipo]
        return Response(data={
            "data": model.objects.filter(marca=marca).values("modelo").distinct()
        }, status=200)


class GetVersionesByModelo(APIView):

    def get(self, request):
        modelo = request.GET.get("modelo")
        marca = request.GET.get("marca")
        tipo = request.GET.get("tipo", None)
        if not tipo or tipo not in list(TIPO_FORM_MAP.keys()):
            messages.error(request, "Tipo de seguro invalido")
            return redirect("/")

        model = TIPO_MODEL_MAP[tipo]
        return Response(data={
            "data": model.objects.filter(marca=marca, modelo=modelo).values("version").distinct()
        }, status=200)