from django.db import models

from django.db import models

class Turno(models.Model):
    fecha = models.DateField()
    nombre_paciente = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.fecha.strftime('%Y-%m-%d')
