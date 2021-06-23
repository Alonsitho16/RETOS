p=float(input())
e=float(input())
IMC=(p)/(e*e)

if(IMC < 15.3):
    print("Bajo peso")

elif (IMC>15.4 and IMC<=21.5):
    print("Normal")

elif (IMC>21.5 and IMC<=30.2):
    print("Sobrepeso")

elif (IMC > 30.3):
    print("Obeso")