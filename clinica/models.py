from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    municipio = models.ForeignKey('Municipio', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Municipio(models.Model):
    DEPARTAMENTO_CHOICES = (
        ('Huila', 'huila'),
        ('Antioquia', 'antioquia'),
        ('Cundinamarca', 'cundinamarca'),
        ('Santander', 'santander'),
    )
    nombre = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100, choices=DEPARTAMENTO_CHOICES, default='huila')

    def __str__(self):
        return f"{self.nombre}, {self.departamento}"

class Diagnostico(models.Model):
    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return f"({self.codigo}) {self.nombre}"

class Historial(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    diagnostico = models.ForeignKey(Diagnostico, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Historial de {self.paciente} - Diagnóstico: {self.diagnostico} - Fecha: {self.fecha}"