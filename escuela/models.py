from django.db import models

# Create your models here.


class Talumnos(models.Model):
    """Alumnos"""
    id_t_usuarios = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80)
    ap_paterno = models.CharField(max_length=80)
    ap_materno = models.CharField(max_length=80)
    activo = models.IntegerField(blank=True, null=True)


class Tmaterias(models.Model):
    """materia"""
    id_tmaterias = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    activo = models.IntegerField(blank=True, null=True)


class Tcalificaciones(models.Model):
    """calificaciones"""
    id_tcalificaciones = models.AutoField(primary_key=True)
    id_tmaterias = models.ForeignKey(
        Tmaterias,
        on_delete=models.CASCADE,
        verbose_name="materias",
    )
    id_t_usuarios = models.ForeignKey(
        Talumnos,
        on_delete=models.CASCADE,
        verbose_name="alumnos",
    )
    calificacion = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    fecha_registro = models.DateField(blank=True, null=True)
    objects = models.Manager()
