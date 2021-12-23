from django.contrib import admin
from .models import Turno , Funcionario , Administrador

# Register your models here.

@admin.register(Funcionario)
class FuncionarioAdmin(admin.ModelAdmin):
      list_display=('id', 'nombre_completo', 'telefono', 'correo','sexo')
      search_fields = ('id',)
      list_display_links = ('id',)
      list_filter = ('sexo',)
      
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
      list_display=('id', 'nombre_completo', 'telefono', 'correo','sexo')
      search_fields = ('id',)
      list_display_links = ('id',)
      list_filter = ('sexo',)


@admin.register(Turno)
class TurnoAdmin(admin.ModelAdmin):
      list_display=('id', 'nombres', 'tipodocumento', 'documento','imagen','estado')
      search_fields = ('id',)
      list_display_links = ('id',)
      list_filter = ('tipodocumento',)

