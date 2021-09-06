
def importe_total_carro(request):
    total = 0
    totalAll= 0

    if request.user:
        for key, value in request.session["carro"].items():
            total = total+(float(value["precio"])*value["cantidad"])
            totalAll = totalAll + value["cantidad"]
    
    #for key, value in request.session["carro"].items():
     #   total = total+(float(value["precio"]))
     #   totalAll = totalAll + value["cantidad"]
#"importe_total_carro":total,"cantidad_general":totalAll
    return {"importe_total_carro":total,"cantidad_general":totalAll}