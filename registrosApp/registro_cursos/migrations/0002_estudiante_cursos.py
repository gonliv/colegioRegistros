# Generated by Django 4.2.11 on 2024-05-09 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_cursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='cursos',
            field=models.ManyToManyField(related_name='estudiantes', to='registro_cursos.curso'),
        ),
    ]