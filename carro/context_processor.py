
def importe_total_carro(request):
    total = 0
    totalAll= 0

    if request.user.is_authenticated:
        for key, value in request.session["carro"].items():
            total = total+(float(value["precio"])*value["cantidad"])
    
    for key, value in request.session["carro"].items():
        total = total+(float(value["precio"]))
        totalAll = totalAll + value["cantidad"]

    return {"importe_total_carro":total,"cantidad_general":totalAll}