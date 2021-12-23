from django.db import models
from .choices import tipodocumento, sexos , estado

class Turno(models.Model):
    
    nombres = models.CharField(max_length=50,verbose_name='Nombre')
    tipodocumento = models.CharField(verbose_name='Tipo Documento',max_length=20,choices=tipodocumento, default='CC')
    documento = models.CharField(max_length=20,verbose_name='Numero de Documento')
    imagen = models.ImageField("Imagen", upload_to='Fotosusuario/', null=True, max_length=255 )
    estado = models.CharField(verbose_name='Estado',max_length=20,choices=estado, default='IGN')
    
    
    def __str__(self):
        texto = "{0} ({1}) {2}"
        return texto.format(self.nombres, self.tipodocumento, self.documento)
    
    
    class Meta:
        verbose_name = 'Turno'
        verbose_name_plural = 'Turnos'
        db_table = 'turno'
        ordering = ['id', '-documento']
    
    
    

class Funcionario(models.Model):
    apellidos=models.CharField(max_length=30,verbose_name='Apellidos:', null=True)
    nombres=models.CharField(max_length=30,verbose_name='Nombres')
    fecha_nacimiento=models.DateField(verbose_name='Fecha de Nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default='F')
    telefono=models.CharField(max_length=10,verbose_name='Telefono',null=True)
    correo=models.CharField(max_length=30,verbose_name='Correo Electronico',null=True)
        
    def nombre_completo(self):
        return "{} , {}".format(self.apellidos, self.nombres)
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        db_table = 'funcionario'
        ordering = ['apellidos', '-nombres']
        
        

class Administrador(models.Model):
    apellidos=models.CharField(max_length=30,verbose_name='Apellidos:', null=True)
    nombres=models.CharField(max_length=30,verbose_name='Nombres')
    fecha_nacimiento=models.DateField(verbose_name='Fecha de Nacimiento')
    sexo=models.CharField(max_length=1, choices=sexos, default='F')
    telefono=models.CharField(max_length=10,verbose_name='Telefono',null=True)
    correo=models.CharField(max_length=30,verbose_name='Correo Electronico',null=True)
        
    def nombre_completo(self):
        return "{} , {}".format(self.apellidos, self.nombres)
    
    def __str__(self):
        return self.nombre_completo()
    
    class Meta:
        verbose_name = 'Administrador'
        verbose_name_plural = 'Administradores'
        db_table = 'administrador'
        ordering = ['apellidos', '-nombres']