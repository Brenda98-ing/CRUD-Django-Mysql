from django.db import models

# Create your models here.
# EL MODELO DE NUESTRA BASE DE DATOS


class Dispositivo(models.Model):
    dispositivo_id = models.AutoField(primary_key=True)
    nombre_de_equipo = models.CharField(max_length=200, blank=True, null=True)
    tiposdispositivo = models.ForeignKey('Tiposdispositivo', models.DO_NOTHING, blank=True, null=True)
    fecha_de_alta = models.DateField(blank=True, null=True)
    fecha_de_actualizacion = models.DateField(blank=True, null=True)
    potencia_actual = models.DecimalField(max_digits=10, decimal_places=0, blank=True, null=True)
    statusdispositivo = models.ForeignKey('Statusdispositivo', models.DO_NOTHING, db_column='statusDispositivo_id', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'dispositivo'


class Lecturas(models.Model):
    dispositivo = models.ForeignKey(Dispositivo, models.DO_NOTHING, blank=True, null=True)
    tiposdispositivo = models.ForeignKey('Tiposdispositivo', models.DO_NOTHING, blank=True, null=True)
    potenciaactual = models.DecimalField(db_column='potenciaActual', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    timestamp = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'lecturas'


class Statusdispositivo(models.Model):
    statusdispositivo_id = models.AutoField(db_column='statusDispositivo_id', primary_key=True)  # Field name made lowercase.
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'statusdispositivo'


class Tiposdispositivo(models.Model):
    tiposdispositivo_id = models.AutoField(primary_key=True)
    nombre_de_tipo = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tiposdispositivo'