# conditionals
dato1 = int (input('Ingresa un numero:'))
dato2 = int (input('Ingresa otro numero:'))
dato3 = int (input('Ingresa otro numero mas:'))
tipo = input('Ingresa Cualquiera de los siguientes simbolos "+" "-" "*" "/": ')
#conditional
if(dato1==dato1==dato3):
    print('Los numeros ingresados son iguales')

if(tipo=='+'):
    res = dato1+dato2
elif(tipo=='-'):
    res = dato1-dato2
elif(tipo=='*'):
    res = dato1*dato2
elif(tipo=='/'):
    res = dato1/dato2
else:
    print('Ingrese una operacion valida')

print('resultado es:',res)