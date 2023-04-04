from django import forms
from seguros import models 
import datetime

class AccountForm(forms.ModelForm):
    cod_postal = forms.CharField(label="C. P.")
    medio_cotizacion = forms.CharField(label="¿En qué medio prefiere recibir su cotización?", widget=forms.RadioSelect(choices=[
        ("WP","WhatsApp"),
        ("LL","Llamado")
    ]))

    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.initial["medio_cotizacion"] = "WP"

    class Meta:
        model = models.Account
        fields = "__all__"

class AccidentesSeguroForm(forms.ModelForm):
    personas = forms.IntegerField(min_value=1)

    class Meta:
        model = models.AccidentesSeguro
        fields = "__all__"

class AutoSeguroForm(forms.ModelForm):
    año = forms.ChoiceField(choices=[(x, str(x)) for x in range(1953, 2024)])
    marca = forms.ChoiceField(choices=[("OTRO","OTRO")])
    modelo = forms.CharField(widget=forms.widgets.Select())
    version = forms.CharField(label="Versión", widget=forms.widgets.Select())
    gnc = forms.ChoiceField(choices=[("Si","Si"), ("No", "No")])
    cero_km = forms.ChoiceField(label="O KM", choices=[("Si","Si"), ("No", "No")])

    def __init__(self, *args, **kwargs):
        super(AutoSeguroForm, self).__init__(*args, **kwargs)
        self.fields['marca'].choices += [(x["marca"],x["marca"]) for x in models.AutoList.objects.all().values("marca").distinct()]
        self.fields['año'].widget.attrs['max'] = datetime.datetime.now().year
        self.initial['uso'] = 'P'
        self.initial["cero_km"] = "No"
        self.initial["gnc"] = "No"


    def clean_año(self):
        año = int(self.cleaned_data['año'])
        if año > datetime.datetime.now().year:
            raise forms.ValidationError("El año es invalido")
        return año
    
    def clean_gnc(self):
        field = self.cleaned_data['gnc']
        return field == "Si"
    
    def clean_cero_km(self):
        field = self.cleaned_data['cero_km']
        return field == "Si"

    class Meta:
        model = models.AutoSeguro
        fields = "__all__"

class MotoSeguroForm(forms.ModelForm):
    año = forms.ChoiceField(choices=[(x, str(x)) for x in range(1970, 2024)])
    marca = forms.ChoiceField(choices=[("OTRO","OTRO")])
    modelo = forms.CharField(widget=forms.widgets.Select)
    version = forms.CharField(label="Versión", widget=forms.widgets.Select)
    cero_km = forms.ChoiceField(label="O KM", choices=[("Si","Si"), ("No", "No")])

    def __init__(self, *args, **kwargs):
        super(MotoSeguroForm, self).__init__(*args, **kwargs)
        self.fields['marca'].choices += [(x["marca"],x["marca"]) for x in models.MotoList.objects.all().values("marca").distinct()]
        self.fields['año'].widget.attrs['max'] = datetime.datetime.now().year
        self.initial['uso'] = 'P'
        self.initial["cero_km"] = "No"


    def clean_año(self):
        año = int(self.cleaned_data['año'])
        if año > datetime.datetime.now().year:
            raise forms.ValidationError("El año es invalido")
        return año
    
    def clean_cero_km(self):
        field = self.cleaned_data['cero_km']
        return field == "Si"

    class Meta:
        model = models.MotoSeguro
        fields = "__all__"

class HogarSeguroForm(forms.ModelForm):
    class Meta:
        model = models.HogarSeguro
        fields = "__all__"

class ComercioSeguroForm(forms.ModelForm):
    class Meta:
        model = models.ComercioSeguro
        fields = "__all__"

class BiciSeguroForm(forms.ModelForm):
    año = forms.ChoiceField(choices=[(x, str(x)) for x in range(2017, 2024)])

    def __init__(self, *args, **kwargs):
        super(BiciSeguroForm, self).__init__(*args, **kwargs)
        self.fields['año'].widget.attrs['max'] = datetime.datetime.now().year

    def clean_año(self):
        año = int(self.cleaned_data['año'])
        if año > datetime.datetime.now().year:
            raise forms.ValidationError("El año es invalido")
        return año

    class Meta:
        model = models.BiciSeguro
        fields = "__all__"

class MonopatinSeguroForm(forms.ModelForm):
    año = forms.ChoiceField(choices=[(x, str(x)) for x in range(2017, 2024)])

    def __init__(self, *args, **kwargs):
        super(MonopatinSeguroForm, self).__init__(*args, **kwargs)
        self.fields['año'].widget.attrs['max'] = datetime.datetime.now().year

    def clean_año(self):
        año = int(self.cleaned_data['año'])
        if año > datetime.datetime.now().year:
            raise forms.ValidationError("El año es invalido")
        return año

    class Meta:
        model = models.MonopatinSeguro
        fields = "__all__"

class CamionSeguroForm(forms.ModelForm):
    año = forms.ChoiceField(choices=[(x, str(x)) for x in range(1953, 2024)])
    año_acoplado = forms.ChoiceField(choices=[(x, str(x)) for x in range(1953, 2024)])
    marca = forms.ChoiceField(choices=[("OTRO","OTRO")])
    modelo = forms.CharField(widget=forms.widgets.Select)
    version = forms.CharField(label="Versión", widget=forms.widgets.Select)
    gnc = forms.ChoiceField(choices=[("Si","Si"), ("No", "No")])
    cero_km = forms.ChoiceField(label="O KM", choices=[("Si","Si"), ("No", "No")])
    acoplado = forms.ChoiceField(choices=[("Si","Si"), ("No", "No")])

    def __init__(self, *args, **kwargs):
        super(CamionSeguroForm, self).__init__(*args, **kwargs)
        self.fields['marca'].choices += [(x["marca"],x["marca"]) for x in models.CamionList.objects.all().values("marca").distinct()]
        self.fields['año'].widget.attrs['max'] = datetime.datetime.now().year
        self.fields['año_acoplado'].widget.attrs['max'] = datetime.datetime.now().year


    def clean_año(self):
        año = int(self.cleaned_data['año'])
        if año > datetime.datetime.now().year:
            raise forms.ValidationError("El año es invalido")
        return año
    
    def clean_gnc(self):
        field = self.cleaned_data['gnc']
        return field == "Si"
    
    def clean_cero_km(self):
        field = self.cleaned_data['cero_km']
        return field == "Si"


    def clean_acoplado(self):
        field = self.cleaned_data['acoplado']
        return field == "Si"
    def clean_año_acoplado(self):
        año_acoplado = self.cleaned_data['año_acoplado']
        if año_acoplado > datetime.datetime.now().year:
            raise forms.ValidationError("El año es invalido")
        return año_acoplado

    class Meta:
        model = models.CamionSeguro
        fields = "__all__"

class FlotaSeguroForm(forms.ModelForm):
    class Meta:
        model = models.FlotaSeguro
        fields = "__all__"

class AutoFlotaSeguroForm(forms.ModelForm):
    año = forms.IntegerField(min_value=1953)

    class Meta:
        model = models.AutoFlotaSeguro
        fields = "__all__"
        exclude = ["flota"]

class VidaSeguroForm(forms.ModelForm):
    class Meta:
        model = models.VidaSeguro
        fields = "__all__"

class PraxisMedicaSeguroForm(forms.ModelForm):
    class Meta:
        model = models.PraxisMedicaSeguro
        fields = "__all__"

class CaucionSeguroForm(forms.ModelForm):
    class Meta:
        model = models.CaucionSeguro
        fields = "__all__"