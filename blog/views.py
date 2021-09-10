from django.shortcuts import render, get_object_or_404
from blog.models import Categoria, Post 
from django.contrib.auth.decorators import login_required

#Importar libreria para autenticar antes de acceder a este views
# Create your views here.
#Decorador para acceder mendiante Auth 

@login_required(login_url='/accounts/login/')
def blog(request):
    posts = Post.objects.all().order_by('-created') #Importar todos los objectos guardo en Post
    return render(request, "blog/blog.html", {"posts":posts})

@login_required
def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id) #Se usa como un where para traer solo esa categoria
    posts=Post.objects.filter(categorias = categoria)
    return render(request, "blog/categoria.html",{'categoria':categoria,'posts':posts})