from django.contrib import admin
from seguros import models

# Register your models here.
admin.site.register(models.AutoList)
admin.site.register(models.AutoSeguro)
admin.site.register(models.MotoList)
admin.site.register(models.MotoSeguro)
admin.site.register(models.CamionSeguro)
admin.site.register(models.CamionList)
admin.site.register(models.FlotaSeguro)
admin.site.register(models.AutoFlotaSeguro)
admin.site.register(models.HogarSeguro)
admin.site.register(models.ComercioSeguro)
admin.site.register(models.BiciSeguro)
admin.site.register(models.MonopatinSeguro)
admin.site.register(models.PraxisMedicaSeguro)
admin.site.register(models.CaucionSeguro)
admin.site.register(models.Account)
admin.site.register(models.UserSeguro)
admin.site.register(models.VidaSeguro)


admin.site.register(models.Terms)
admin.site.register(models.Privacidad)