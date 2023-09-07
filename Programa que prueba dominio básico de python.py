#He subido este programa para probar mi dominio de los elementos básicos de python.
#Este programa indica todos los números que son primos desde 1 al número ingresado en la consola.
#Nota: Los números primos son aquellos que solo son divisibles por 1 y por si mismos.

def es_primo(numero):

    contador=0
    numeros_divisores=list(range(1,int(numero)+1))
    
    #Este ciclo for recuenta cuantos números positivos menores o iguales al número ingresado
    #en la función tienen resto cero al dividirlo.
    for divisor in numeros_divisores:
        if int(numero)%int(divisor)==0:
            contador=contador+1

    #Si es divisible solo por dos números(1 y si mismo), es primo.
    if contador==2:
        return True  
    #Si hay más de dos números que lo pueden dividir, entonces el número no es primo.
    if contador>2:
        return False

     
print("Ingrese un número mayor que 1, la consola le indicará que números son primos desde 1 a ese número:")
numero=input()
lista_numeros=[x for x in range(2,int(numero)+1)] #No se incluye 1 por que no es primo
lista_primos=list(filter(es_primo,lista_numeros))

for numero_primo in lista_primos:
    print(f"{numero_primo} es primo")