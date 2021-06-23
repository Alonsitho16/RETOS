temp_1 = float(input()) 
temperatura=(temp_1 * 9/5) + 32
while temperatura >= 1:
    print (temperatura)
    temperatura = temperatura - 1
    if temperatura <= 203.0:
        break