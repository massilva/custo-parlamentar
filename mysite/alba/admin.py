from django.contrib import admin
from .models import Deputados, Partidos, GastoMensal

class DeputadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'partido', 'id_deputado', 'slug')
    list_filter = ('nome', 'partido', 'id_deputado', 'slug')
    search_fields = ('nome','partido')

    prepopulated_fields = {'slug': ('nome',)}
    readonly_fields = ('id_deputado', )

class PartidoAdmin(admin.ModelAdmin):
    list_display = ('nome_partido',)
    search_fields = ('nome_partido',)

class GastosAdmin(admin.ModelAdmin):
    list_display = ('id_deputado','mes', 'ano', 'id_categoria', 'valor')

admin.site.register(Deputados, DeputadoAdmin, verbose_name="Deputados")
admin.site.register(Partidos, PartidoAdmin, verbose_name="Partidos")
