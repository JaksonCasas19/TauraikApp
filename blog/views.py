from django.shortcuts import render
from blog.models import Categoria, Post 

# Create your views here.
def blog(request):
    posts = Post.objects.all() #Importar todos los objectos guardo en Post
    return render(request, "blog/blog.html", {"posts":posts})


def categoria(request,categoria_id):
    categoriaOk=Categoria.objects.get(id=categoria_id) #Se usa como un where para traer solo esa categoria
    post=Post.objects.filter(categoria=categoriaOk)
    return render(request, "blog/categoria.html",{'categoria':categoria,'post':post})