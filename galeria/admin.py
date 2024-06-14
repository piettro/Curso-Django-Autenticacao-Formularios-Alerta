from django.contrib import admin
from .models import *

class ListandoFotografia(admin.ModelAdmin):
    list_display = ('id','nome','legenda','publicada')
    list_display_links = ('id','nome')
    search_fields = ('id', 'nome')
    list_filter = ('categoria',)
    list_per_page = 10
    list_editable = ("publicada",)
    sortable_by = ("data_fotografia",)

# Register your models here.
admin.site.register(Fotografia, ListandoFotografia)