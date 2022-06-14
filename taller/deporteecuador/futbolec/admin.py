from django.contrib import admin

# Register your models here.
from futbolec.models import Equipo, Jugador, Campeonato,CampeonatoEquipo
"""""
class EstudianteAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('nombre', 'apellido', 'cedula', 'edad', 'tipo_estudiante')
    search_fields = ('nombre', 'cedula')
    exclude = ("modulos",)
# admin.site.register se lo altera
# el primer argumento es el modelo (Estudiante)
# el segundo argumento la clase EstudianteAdmin

# admin.site.register(Matricula)

class MatriculaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    # listado de atributos que se mostrará
    # por cada registro
    # se deja de usar la representación (str) 
    # de la clase 
    list_display = ('estudiante', 'modulo', 'comentario')
    search_fields = ('estudiante__nombre', 'modulo__nombre')
"""""
admin.site.register(Equipo)
admin.site.register(Jugador)
admin.site.register(Campeonato)
admin.site.register(CampeonatoEquipo)
