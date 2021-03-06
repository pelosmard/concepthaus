# Generated by Django 2.1.dev20171223092632 on 2018-03-26 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Talumnos',
            fields=[
                ('id_t_usuarios', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=80)),
                ('ap_paterno', models.CharField(max_length=80)),
                ('ap_materno', models.CharField(max_length=80)),
                ('activo', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tcalificaciones',
            fields=[
                ('id_tcalificaciones', models.AutoField(primary_key=True, serialize=False)),
                ('calificacion', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('fecha_registro', models.DateField(blank=True, null=True)),
                ('id_t_usuarios', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.Talumnos', verbose_name='alumnos')),
            ],
        ),
        migrations.CreateModel(
            name='Tmaterias',
            fields=[
                ('id_tmaterias', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(blank=True, max_length=80, null=True)),
                ('activo', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='tcalificaciones',
            name='id_tmaterias',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='escuela.Tmaterias', verbose_name='materias'),
        ),
    ]
