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

@admin.register(models.UserSeguroInfo)
class UserSeguroInfoAdmin(admin.ModelAdmin):
    change_list_template = 'admin/user_seguro_info_list.html'
    # date_hierarchy = 'created_at'

    def changelist_view(self, request, extra_context=None):
        response = super().changelist_view(
            request,
            extra_context=extra_context,
        )

        try:
            qs = response.context_data['cl'].queryset
            qs = qs.exclude(account__isnull=True)
        except (AttributeError, KeyError):
            return response

        data = []

        for elem in qs:
            data.append({
                "id": elem.id,
                "tipo": elem.tipo,
                "fecha": elem.created_at.strftime("%H:%M %d/%m/%Y"),
                "nombre": elem.account.nombre,
                "apellido": elem.account.apellido,
                "codigo": elem.account.cod_area,
                "telefono": elem.account.telefono,
                "email": elem.account.email,
                "medio": elem.account.medio_cotizacion,
                "datos": f'/admin/seguros/{elem.tipo.replace("_", "")}seguro/{elem.data_id}/change'
            })

        response.context_data['data'] = data

        return response