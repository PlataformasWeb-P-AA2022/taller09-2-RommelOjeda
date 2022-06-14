from django.db import models

# Create your models here.
class Equipo(models.Model):

    nombre = models.CharField(max_length=30)
    siglas = models.CharField(max_length=30) 
    twitter = models.CharField(max_length=30)

    def __str__(self):
        return "%s - %s - %s" % (self.nombre, 
                self.siglas,
                self.twitter)


class Jugador(models.Model):
    """
    """

    nombre = models.CharField(max_length=30) 
    posicion = models.CharField(max_length=30) 
    camisa = models.IntegerField("Numero de Camisa") 
    sueldo = models.IntegerField("Sueldo") 
    equipo_futbol = models.ForeignKey(Equipo, related_name='losjugadores', 
            on_delete=models.CASCADE) 

    # estudiantes = models.ManyToManyField(Estudiante, through='Matricula')

    def __str__(self):
        return "%s - %s - Camisa: %d  - Sueldo: %d  - %s" % (self.nombre,self.posicion,
        self.camisa,self.sueldo,self.equipo_futbol)


class Campeonato(models.Model):
    """
    """
    nombre = models.CharField(max_length=30) 
    auspiciante = models.CharField(max_length=30) 

    def __str__(self):
        return "%s - %s" % (self.nombre, 
                self.auspiciante)


class CampeonatoEquipo(models.Model):
    """
    """
    anio = models.IntegerField("año") 
    equipo = models.ForeignKey(Equipo, related_name='campeonatoequipo', 
            on_delete=models.CASCADE) 
    campeonato = models.ForeignKey(Campeonato, related_name='campeonatoaustpisiante', 
            on_delete=models.CASCADE) 

    def __str__(self):
        return "%s - %s - %s" % (self.anio, 
                self.equipo,self.campeonato)
