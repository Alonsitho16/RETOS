#python compiler
salario = int(input())
alimentos = salario*0.20
pasajes = salario*0.15
cine = salario*0.10
alquiler = salario*0.15
gastos = alimentos + pasajes + cine + alquiler
libre = salario - gastos
print(libre)