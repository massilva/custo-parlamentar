# Generated by Django 2.0 on 2017-12-21 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alba', '0006_auto_20171221_1326'),
    ]

    operations = [
        migrations.AddField(
            model_name='deputados',
            name='site',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
