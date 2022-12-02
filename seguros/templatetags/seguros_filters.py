from django import template
  
register = template.Library()

TIPO_IMAGE_TEXT_MAP = {
    "auto": "Cotizá online el seguro<br>que estás buscando",
    "moto": "Seguro para Moto<br>Cotizá y obtén la mejor cobertura",
    "accidentes": "Seguro de Accidentes Personal<br>Adaptado a tu necesidad",
    "hogar": "Seguro Combinado Familiar<br>Tu hogar merece la mejor cobertura",
    "comercio": "Seguro Integral de Comercio<br>Protege tu fuente de ingreso",
    "bici": "Seguro para Bicicleta<br>y Monopatín",
    # "monopatin": "",
    "camion": "Seguro para Camión<br>El mejor respaldo. ¡Aprovecha y ahorra!",
    "flota": "Seguro para Flota<br>Para empresas, pymes y particulares",
    "vida": "Seguro de Vida<br>Pensado para dar respaldo y tranquilidad",
    "praxis_medica": "Seguro Praxis Médica<br>Respaldo para profesionales de la salud",
    "caucion": "Seguro de Caución<br>Una garantía para cada necesidad",
    "celular": "¿Tenés tu celular asegurado?",
    # "account": ""
}
  
@register.filter("image_text_filter")
def image_text_filter(value):
    return TIPO_IMAGE_TEXT_MAP[value]