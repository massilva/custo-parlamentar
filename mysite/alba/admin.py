from django.contrib import admin
from .models import Deputado, Partido


class DeputadoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'slug', 'partido', 'sigla')
    list_filter = ('nome', 'slug', 'partido', 'sigla')
    search_fields = ('nome','partido')
    # readonly_fields = ('id',)
    # prepopulated_fields = {'slug':('title',)}
    # raw_id_fields = ('author',)
    # date_hierarchy = 'publish'
    # ordering = ['status','publish']

class PartidoAdmin(admin.ModelAdmin):
    list_display = ('nome_partido', 'sigla_partido', 'descricao')
    search_fields = ('nome_partido', 'sigla_partido')

admin.site.register(Deputado, DeputadoAdmin)
admin.site.register(Partido, PartidoAdmin)
    #
    # id_site = models.IntegerField(primary_key=True)
    # nome = models.CharField(max_length=50)
    # partido = models.CharField(max_length=50)
    # sigla = models.CharField(max_length=20)
    # slug = models.CharField(max_length=20)
    # biografia = models.TextField()
