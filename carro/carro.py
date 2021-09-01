class Carro:
    def __init__(self,request):
        #Cuando el usuario agrege por primera vez un Item, esta linea se encargara de guardar los elementos en el carro
        #Si el usuario se va y vuelve debe mantener dicha información
        self.request=request
        self.session=request.session 

        carro = self.session.get("carro")

        if not carro:
            #Si no hay carro  debemos retornar vacio
            carro = self.session["carro"]={}
        else:
            #Si el usuario agrego al carro
            self.carro=carro

    def agregar(self,producto):

        #Si el Id del producto no esta en las claves de nuestro carro me lo agregas (Por primera vez)
        if(str(producto.id)not in self.carro.keys()):
            self.carro[producto.id] = {
                "producto_id":producto.id,
                "nombre":producto.nombre,
                "precio":str(producto.precio),
                "cantidad":1,
                "imagen":producto.imagen,
            }