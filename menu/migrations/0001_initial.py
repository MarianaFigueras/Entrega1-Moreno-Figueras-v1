# Generated by Django 4.1.2 on 2022-10-27 04:37

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_plato', models.CharField(max_length=50)),
                ('nombre_plato', models.CharField(max_length=50)),
                ('descripcion', ckeditor.fields.RichTextField(null=True)),
                ('precio', models.IntegerField()),
                ('fecha_creacion', models.DateField(null=True)),
            ],
        ),
    ]
