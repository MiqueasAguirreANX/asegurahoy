from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Terms(models.Model):
    terms = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

class Privacidad(models.Model):
    privacidad = models.TextField(blank=True, null=True)
    updated = models.DateTimeField(auto_now=True)

class Account(models.Model):
    cod_postal          = models.CharField(max_length=20)
    nombre              = models.CharField(max_length=250)
    apellido            = models.CharField(max_length=250)
    cod_area            = models.CharField(max_length=5)
    telefono            = models.CharField(max_length=20)
    email               = models.EmailField(unique=True)
    medio_cotizacion    = models.CharField(max_length=50, choices=[
        ("WP","WhatsApp"),
        ("LL","LLamado")
    ])

class UserSeguro(models.Model):
    tipo        = models.CharField(max_length=250)
    uuid        = models.CharField(max_length=200, unique=True)
    data_id     = models.IntegerField()
    account     = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    completed   = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

USOS = (
    ("P","Personal"),
    ("C","Comercial"),
)

class AutoList(models.Model):
    marca   = models.CharField(max_length=250)
    modelo  = models.CharField(max_length=250)
    version = models.CharField(max_length=250)

class AutoSeguro(models.Model):
    marca   = models.CharField(max_length=250)
    año     = models.PositiveIntegerField(validators=[MinValueValidator(1953)])
    modelo  = models.CharField(max_length=250)
    version = models.CharField(max_length=250)
    uso     = models.CharField(max_length=25, choices=USOS)
    gnc     = models.BooleanField()
    cero_km = models.BooleanField()


class MotoList(models.Model):
    marca   = models.CharField(max_length=250)
    modelo  = models.CharField(max_length=250)
    version = models.CharField(max_length=250)

class MotoSeguro(models.Model):
    marca   = models.CharField(max_length=250)
    año     = models.PositiveIntegerField(validators=[MinValueValidator(1970)])
    modelo  = models.CharField(max_length=250)
    version = models.CharField(max_length=250)
    uso     = models.CharField(max_length=25, choices=USOS)
    cero_km = models.BooleanField()


LINDEROS = (
    ("SB","Sin baldio"),
    ("BA","Baldio abandonado"),
    ("BM","Baldio con medianera"),
)

TIPOS_BICI_HOGAR = (
    ("RDYF", "Robo dentro y fuera del domicilio"),
    ("NO", "No agrego bicicleta"),
    ("AMBOS", "Cotizar ambos presupuestos"),
)

class HogarSeguro(models.Model):
    construccion        = models.CharField(max_length=250)
    material_techo      = models.CharField(max_length=250)
    m2                  = models.IntegerField()
    valor               = models.FloatField()
    rejas               = models.CharField(max_length=250)
    linderos            = models.CharField(max_length=25, choices=LINDEROS)
    tipo_bici           = models.CharField(max_length=40, choices=TIPOS_BICI_HOGAR)
    marca_modelo_bici   = models.CharField(max_length=250)
    valor_bici          = models.FloatField()

class ComercioSeguro(models.Model):
    descripcion     = models.CharField(max_length=250)
    construccion    = models.CharField(max_length=250)
    material_techo  = models.CharField(max_length=250)
    m2              = models.IntegerField()
    valor           = models.FloatField()
    rejas           = models.CharField(max_length=250)
    linderos        = models.CharField(max_length=25, choices=LINDEROS)


BICIS = (
    ("MB","Mountain Bike"),
    ("R","Rutera"),
    ("BMX","BMX"),
    ("P","Paseo"),
)

MATERIALES_BICI = (
    ("AC","Acero"),
    ("AL","Aluminio"),
    ("CA","Carbon"),
    ("TI","Titanio"),
)

class BiciSeguro(models.Model):
    año             = models.PositiveIntegerField(validators=[MinValueValidator(2017)])
    marca_modelo    = models.CharField(max_length=250)
    tipo            = models.CharField(max_length=25, choices=BICIS)
    valor           = models.FloatField()
    color           = models.CharField(max_length=100)
    material        = models.CharField(max_length=25, choices=MATERIALES_BICI)
    rodado          = models.PositiveSmallIntegerField()


MONOPATINES = (
    ("B","Bateria"),
    ("E","Electrico"),
)

class MonopatinSeguro(models.Model):
    año             = models.PositiveIntegerField(validators=[MinValueValidator(2017)])
    marca_modelo    = models.CharField(max_length=250)
    tipo            = models.CharField(max_length=25, choices=MONOPATINES)
    valor           = models.FloatField()
    color           = models.CharField(max_length=100)

class CamionList(models.Model):
    marca   = models.CharField(max_length=250)
    modelo  = models.CharField(max_length=250)
    version = models.CharField(max_length=250)

RADIOS = (
    ("U","Urbano"),
    ("N","Nacional"),
)

class CamionSeguro(models.Model):
    marca                   = models.CharField(max_length=250)
    año                     = models.PositiveIntegerField(validators=[MinValueValidator(1953)])
    modelo                  = models.CharField(max_length=250)
    version                 = models.CharField(max_length=250)
    radio                   = models.CharField(max_length=25, choices=RADIOS)
    gnc                     = models.BooleanField()
    cero_km                 = models.BooleanField()
    acoplado                = models.BooleanField()
    marca_modelo_acoplado   = models.CharField(max_length=250)
    año_acoplado            = models.PositiveIntegerField(validators=[MinValueValidator(1953)])

class FlotaSeguro(models.Model):
    cantidad = models.PositiveIntegerField(validators=[MinValueValidator(2)])

class AutoFlotaSeguro(models.Model):
    marca   = models.CharField(max_length=250)
    año     = models.PositiveIntegerField(validators=[MinValueValidator(1953)])
    modelo  = models.CharField(max_length=250)
    version = models.CharField(max_length=250)
    uso     = models.CharField(max_length=25, choices=USOS)
    gnc     = models.BooleanField()
    cero_km = models.BooleanField()
    flota   = models.ForeignKey(FlotaSeguro, on_delete=models.CASCADE)

PERIODOS = (
    ("1","1 mes"),
    ("2","2 meses"),
    ("3","3 meses"),
    ("4","4 meses"),
    ("5","5 meses"),
    ("6","6 meses"),
    ("+6","+6 meses"),
)

class AccidentesSeguro(models.Model):
    actividad = models.CharField(max_length=250)
    personas  = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    periodo   = models.CharField(max_length=25, choices=PERIODOS)


VIDA_TIPOS = (
    ("V","Vida"),
    ("S","Sepelio"),
)

class VidaSeguro(models.Model):
    fecha_nacimiento    = models.DateField()
    tipo                = models.CharField(max_length=25, choices=VIDA_TIPOS)

class PraxisMedicaSeguro(models.Model):
    especialidad = models.CharField(max_length=250)

class CaucionSeguro(models.Model):
    descripcion     = models.CharField(max_length=250)
    suma_asegurada  = models.FloatField()