from django import froms
from .models import contacto

class contactoform(froms.modelform):
class Meta:
    model = contacto
    fields = '_all_'