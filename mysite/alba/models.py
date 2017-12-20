# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Categorias(models.Model):
    id_categoria = models.IntegerField(primary_key=True)
    categoria = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categorias'


class Deputados(models.Model):
    id_deputado = models.IntegerField(primary_key=True)
    nome = models.TextField()
    partido = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
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
