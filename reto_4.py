
def calculoCostoHuevos(cantAAA,cantAA,cantA,cantB,cantC):
    costoAAA = (cantAAA*650)
    costoAA = (cantAA*480)
    costoA = (cantA*320)
    costoB = (cantB*180)
    costoC = (cantC*85)
    costo_total = (int(costoAAA)+costoAA+costoA+costoB+costoC)
    return "costoAAA:"+str(costoAAA)+" costoAA:"+str(costoAA)+" costoA:"+str(costoA)+" costoB:"+str(costoB)+" costoC:"+str(costoC)+" costo total:"+str(costo_total)
    print(calculoCostoHuevos(5,4,3,8,10))
   
   
