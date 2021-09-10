from django.shortcuts import render, get_object_or_404
from blog.models import Categoria, Post 
#Importar libreria para autenticar antes de acceder a este views
from django.contrib.auth.decorators import login_required


# Create your views here.
def blog(request):
    posts = Post.objects.all().order_by('-created') #Importar todos los objectos guardo en Post
    return render(request, "blog/blog.html", {"posts":posts})


def categoria(request,categoria_id):
    categoria=Categoria.objects.get(id=categoria_id) #Se usa como un where para traer solo esa categoria
    posts=Post.objects.filter(categorias = categoria)
    return render(request, "blog/categoria.html",{'categoria':categoria,'posts':posts})