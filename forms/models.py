from django.db import models
# Create your models here.


class SitemaOperativo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.nombre

class Ofimatica(models.Model):
    # office /opciones/libreoffice
    nombre = models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.nombre
    
class TipoDispositivo(models.Model):
    # impresora/ impresora / camara / scanner (descripcion)
    tipo = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.tipo
    
class Dispositivo(models.Model):
    tipo = models.ForeignKey(TipoDispositivo, on_delete=models.CASCADE)
    descripcion = models.CharField(max_length=50)
    fecha_fabricacion = models.DateField()
    def __str__(self) -> str:
        return f'{self.id} {self.tipo} {self.descripcion} {self.fecha_fabricacion}'

class Nivel(models.Model):
    #    ninguno/básico/medio/alto
    tipo = models.CharField(max_length=10)
    def __str__(self) -> str:
        return self.tipo


class Cargo(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nombre

class Unidad(models.Model):
    nombre = models.CharField(max_length=100)
    def __str__(self) -> str:
        return self.nombre

class Encuesta(models.Model):
    descripcion_caracteristicas = models.CharField(max_length=500, blank=True)
    otros = models.CharField(max_length=50, blank=True)
    # Nivel
    software_libre = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='software_libre')
    # Nivel
    estandares_abiertos = models.ForeignKey(Nivel, on_delete=models.CASCADE, related_name='estandares_abiertos')
    
    ofimatica = models.ForeignKey(Ofimatica, on_delete=models.CASCADE)
    
    sistema_operativo = models.ForeignKey(SitemaOperativo, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.id} {self.descripcion_caracteristicas} {self.otros} {self.software_libre} {self.estandares_abiertos} {self.ofimatica} {self.sistema_operativo}'
    
class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.IntegerField()
    carnet = models.CharField(max_length=10)
    extension = models.CharField(max_length=5, blank=True)
    
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE)
    encuesta = models.ForeignKey(Encuesta, on_delete=models.CASCADE, blank=True, null=True)
    unidad  = models.ForeignKey(Unidad, on_delete=models.CASCADE)
    dispositivos = models.ManyToManyField(Dispositivo, blank=True)
    
    def __str__(self) -> str:
        return f'{self.id} {self.nombre} {self.cargo} {self.carnet} {self.extension}'
    