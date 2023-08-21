#Ejercicio 1. 
'''Definir una función es_par(n) que devuelva True si el número es par y False en
caso contrario.'''

def es_par(n):
    return n%2 == 0

print(5, "¿es par?", es_par(5))

#Ejercicio 2
'''Definir una función dos_pertenece(lista) que tome una lista de enteros y
devuelva True si la lista tiene al 2 y False en caso contrario.'''

def dos_pertenece(lista):
    return 2 in lista

lista_1 = [3,4,5,6,7]

print ("¿2 está en la lista?", dos_pertenece(lista_1))

#Ejercicio 3

'''Definir una función pertenece(lista, elem) que tome una lista y un elemento,
y devuelva True si la lista tiene al elemento dado y False en caso contrario.'''

def pertence(lista,elem):
    return elem in lista

#Ejercicio 4
'''Definir una función mas_larga(lista1, lista2) que tome dos listas y
devuelva la más larga.'''

def mas_larga(lista1, lista2):
    listaRes = lista1
    if (len(lista1) < len(lista2)):
        listaRes = lista2
    return listaRes

lista_2 = [2,3,4,5,6,7,8]

print("¿Que lista es mas larga", lista_1, "o", lista_2, "?", mas_larga(lista_1, lista_2))

#Ejercicio 5
'''Definir una función cant_e que tome una lista de caracteres y devuelva la cantidad
de letras ‘e’ que tiene la misma.'''

def cant_e(lista):
    acc = 0
    for i in range(len(lista)):
        if lista[i] == 'e':
            acc += 1
    return acc
    
lista_3 = ['e','a','b','o', 'e']    

print("La cantidad de caracteres e de", lista_3,"es", cant_e(lista_3))
    
    
#Ejercicio 6
'''Definir una función sumar_unos que tome una lista de enteros, les sume 1 a todos
sus elementos, y devuelva la misma lista, pero modificada.'''

def sumar_unos(lista):
    for i in range (len(lista)):
        lista[i] +=  1
    return lista

print ("Si a", lista_2, "le sumo 1 a todos sus valores obtengo:", sumar_unos(lista_2))


#Ejercicio 7
'''Definir la función mezclar(cadena1, cadena2) que tome dos strings y devuelva
el resultado de intercalar elemento a elemento. Por ejemplo: si intercalamos Pepe
con Jose darıá PJeopsee. En el caso de Pepe con Josefa daría PJeopseefa'''


def mezclar(cadena1, cadena2):
    cadenaRes = ''
    cadenaMasCorta = cadena1
    cadenaMasLarga = cadena2
    if len(cadena1) > len(cadena2):
        cadenaMasCorta = cadena2
        cadenaMasLarga = cadena1
    i = 0
    while i < len(cadenaMasCorta):
        cadenaRes += (cadenaMasCorta[i]+cadenaMasLarga[i])
        i += 1
    while i < len(cadenaMasLarga):
        cadenaRes += cadenaMasLarga[i]
        i += 1
    return cadenaRes



print("Si intercalamos Pepe con Josefa darıá", mezclar('Pepe','Josefa'))