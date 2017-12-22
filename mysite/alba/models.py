from django.db import models
from django.utils.text import slugify

class Categorias(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    categoria = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Deputados(models.Model):
    id_deputado = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=100)
    partido = models.IntegerField(blank=True, null=True)
    slug = models.SlugField(unique=True, max_length=25)
    biografia = models.TextField(null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    telefone = models.CharField(max_length=400, blank=True,null=True)
    email = models.CharField(max_length=200, blank=True,null=True)
    twitter = models.CharField(max_length=200, blank=True,null=True)
    facebook = models.CharField(max_length=200, blank=True,null=True)
    site = models.CharField(max_length=200, blank=True,null=True)
    instagram = models.CharField(max_length=200, blank=True,null=True)

    class Meta:
        managed = True
        db_table = 'deputados'
        verbose_name = 'deputado'
        verbose_name_plural = 'deputados'

class GastoMensal(models.Model):
    mes = models.IntegerField(primary_key=True)
    ano = models.IntegerField()
    id_categoria = models.ForeignKey(Categorias, models.DO_NOTHING, db_column='id_categoria')
    valor = models.DecimalField(max_digits=65535, decimal_places=2, blank=True, null=True)
    id_deputado = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'gasto_mensal'
        unique_together = (('mes', 'ano', 'id_categoria', 'id_deputado'),)


class Partidos(models.Model):
    id_partido = models.IntegerField(primary_key=True)
    id_deputado = models.IntegerField()
    nome_partido = models.CharField(max_length=256, blank=True, null=True)
    sigla = models.CharField(max_length=48, blank=True, null=True)
    numero_legenda = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'partidos'
        verbose_name = 'partido'
        verbose_name_plural = 'partidos'
