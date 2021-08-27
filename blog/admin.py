from django.contrib import admin
from django.db import models
#Importar el modelo categoria y post
from .models import Categoria,Post
# Register your models here.

#Agregar las clases creada hacia el panel de administración

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields=('created','updated')
    

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)