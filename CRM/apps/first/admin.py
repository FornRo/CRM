from django.contrib import admin
from .models import CompanyAddress, Record, Project, \
    Interaction, Descriptin, Communication
# Register your models here.
admin.site.register(CompanyAddress)
admin.site.register(Record)
admin.site.register(Project)
admin.site.register(Interaction)
admin.site.register(Communication)
admin.site.register(Descriptin)
