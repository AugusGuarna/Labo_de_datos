# 2da clase

## Contenidos

1. Python desde la terminal
2. Correr archivos.py
3. IDE-Spyder
4. Funciones
5. Diccionarios
6. Módulos
7. Manejo de archivos
8. Ejercicios
------------------------------------

## Python desde la terminal
Para salir se utiliza el comando ```exit()```
## Correr archivos.py

Tenemos que crear un archivo de texto .py y luego en consola se ejecutan los comandos

```
python3 archivo_texto.py
```

Sobre el directorio donde se haya creado el archivo. Para cambiar directorios usamos

```
cd (nombre de directorio o .. si queremos salir de ese directorio)
```

Si utilizamos este comando al finalizar la ejecución sale de python, pero si usamos

```
python3 -i archivo_texto.py
```

Nos quedamos dentro del intérprete de python lo que nos permite consultar el estado final de las variables.

## IDE-Spyder

Para usar Spyder tenemos que copiar la función a la consola y apretar dos veces ```enter```.

## Funciones

Para declarar las funciones se utiliza

```
def function(parameters):
```

## Copias

Las listas tienen un método para hacer copias

```
a = [2,3,[100,101],4]
b = a.copy()
b == a # True
b is a # False ya que al ser una copia ocupa una posición de memoria distinta

c = a
c == a # True
c is a # True ya que le estamos asignando al espacio de memoria otro nombre posible. De esta forma una misma posición de memoria pasa a tener dos nombres distintos

a.append(5) # Modificamos la lista a
print(b) # b no se modifica ya que es una copia del estado previo de a
print(c) # C se modifica porque apunta a la misma posición de memoria que a

```
Sin embargo, si hacemos
```
a[2].append(102) #Modificamos la lista interna de a
print(b) #Se modifica b ya que la lista esta es la misma para b. b es una copia de a pero que tiene el mismo puntero a esta lista interna entonces se modifica también
print(c)
```

De todos modos tenemos otro comando que copia incluso la lista interna deshaciendonos de este puntero

```
import copy
a = [2,3,[100,101],4]
b = copy.deepcopy(a) #copy.deepcopy copia toda la lista y también las listas internas.
a.append(5)
print(b)
a[2].append(102)
print(b)
```

## Diccionarios

* Se construyen con llaves ```{ }```
* Se declaran 
    ```
    {clave1: valor1, clave2: valor2, … }
    ```
* Tanto las claves como los valores pueden ser de distintos tipos de objetos pero **las claves deben ser de tipo inmutable**
* Para acceder a un valor asociado a una clave se utilizan los corchetes ```[ ]```
* Podemos agregar claves utilizando corchetes e igualando esa clave a su significado, incluso haciendo esto puedo redefinir una clave
* Podemos armarlos a partir de una lista de tuplas (clave, valor) con la función ```dict()```
    ```
    >>> tuplasDeCuadrados = [(1,1), (2,4), (3,9), (4,16)]
    >>> cuadrados = dict(tuplasDeCuadrados)
    >>> cuadrados[2]
    ```
* Si tenemos dos listas y queremos armar tuplas a partir de ellas podemos usar la función  ```zip()```
    ```
    >>> basesCuadrado = [1,2,3,4]
    >>> resulCuadrado = [1,4,9,16]
    >>> cuadrados = dict(zip(basesCuadrado,resulCuadrado))

    ```

## Módulos

Si bien Python tiene muchas funciones que se pueden usar directamente, hay muchas otras que
están disponibles dentro de módulos.\
Un **módulo** es una **colección de funciones** que alguien (o una comunidad) desarrollaron y
empaquetaron para que estén disponibles para todo el mundo.\
Para que las funciones estén disponibles para ser utilizadas en mi programa, tengo que usar la
instrucción **import**.

```
random.random() # devuelve números aleatorios

random.seed() # devuelve los números que se generaron a partir de esa seed. A partir de esta se generan varios números al azar y se guardan en un conjunto. Estos números reaparecen
random.randint(desde, hasta) # devuelve un entero al azar

```

## Manejo de archivos

1. Debemos crear una variable de tipo archivo y especificar el nombre y como lo vamos a leer.
2. Tenemos que pedirle que lea los datos
3. Cerramos el archivo

```
f = open(nombre_archivo, 'rt' ) # abrir para lectura ('r' de read, 't' de text)
data = f.read()
f.close()
data
print(data)
```
```data``` imprime sin formato\
```print(data)``` imprime con formato

Otra forma de abrir archivos es con 

```
with open(nombre_archivo, 'rt') as f: # otra forma de abrir archivos
data = f.read()
# 'data' es una cadena con todo el texto en el archivo y con el with el archivo se cierra solo
data
print(data)
```

Para leer una archivo línea por línea, usá
un ciclo for como éste:
```
with open(nombre_archivo, 'rt') as f:
for l in f:
# Procesar la línea
print(“->”,l)
```

### Archivos .csv
* csv = comma separated values
* Son planillas guardadas como texto en un archivo
* Cada linea de texto es una fila de la planilla
* Las comas separan columnas

Formas de leer el .csv

```
import csv
f = open(nombre_archivo)
filas = csv.reader(f) #Se usa para leer el archivo. Este comando devuelve un iterador sobre el cual podemos iterar dentro
for fila in filas:
    instrucciones
f.close()
```

Si la primera fila son encabezados, podemos leerlo así:

```
f = open(nombre_archivo)
filas = csv.reader(f)
encabezado = next(filas) # un paso del iterador
for fila in filas: # ahora el iterador sigue desde la segunda fila
    instrucciones
f.close()


## Ejercicios

### Ejercicio 1

Definir una función maximo(a,b) que tome dos parámetros numéricos y devuelva el máximo.

```
def max(a,b):
    max = b
    if a > b:
        max = a
    return max
```

### Ejercicio 2

Definir una función tachar_pares(lista) que tome una lista de números y devuelva una similar
pero donde los números pares estén reemplazados por ‘x’.

```
def tachar_pares(l):
    for i in range(len(l)):
        if l[i] % 2 == 0:
            l[i] = "x"
```

### Ejercicio 3

Construí una función traductor_geringoso(lista) que, a partir de una lista de palabras, devuelva un
diccionario geringoso.
Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso.
Por ejemplo:
```
lista = ['banana', 'manzana', 'mandarina']

traductor_geringoso(lista) =
{'banana': 'bapanapanapa', 'manzana': 'mapanzapanapa', 'mandarina': 'mapandaparipinapa'}
```
Código:
```
def geringoso (s):
	vocales = "aeiouAEIOU"
	capadepenapa = ''
	for c in s:
	    capadepenapa += c;
	    if c in vocales:
	        capadepenapa += "p"+ c
	return capadepenapa

def traductor_geringoso (lista):
    map = { }
    for i in lista:
        map[i] = geringoso(i)
```

### Ejercicio 4

Escribir una función generala_tirar() que simule una tirada de dados para el juego de la generala. Es decir, debe devolver una lista aleatoria de 5 valores de dados . Por ejemplo, si sale 2,1,1,2,2 debe imprimir [2,1,1,2,2]

```
import random

random.seed(69)

def generala_tirar():
    l = []
    for i in range(5):
        l.append(random.randint(1,6))
    return l

print (generala_tirar())
```


### Ejercicio 5

scribir un programa que recorra las líneas del archivo ‘datame.txt’ e imprima solamente las líneas que contienen la palabra ‘estudiante’

```
nombre_archivo = "./datame.txt"
with open(nombre_archivo, 'rt') as f:
    for l in f:
        if "estudiantes" in l:
            print("->",l)
```

### Ejercicio 6

A partir del archivo cronograma_sugerido.csv armar una lista con todas las asignaturas del
cronograma

```
nombre_archivo = "./cronograma_sugerido.csv"
lista = []
with open(nombre_archivo, 'rt') as f:
    for l in f:
        intermedia = l.split(",")
        lista.append(intermedia[1])
    
    lista.remove("Asignatura")
print(lista)        
```

### Ejercicio 7



```
def cuantas_materias(n):
    nombre_archivo = "./cronograma_sugerido.csv"
    lista = []
    with open(nombre_archivo, 'rt') as f:
        for l in f:
            intermedia = l.split(",")
            if intermedia[0] != "Cuatrimestre":
                if n == int(intermedia[0]):
                    lista.append(intermedia[1])
    return len(lista)
```

### Ejericicio 8

Definimos registros(nombre_archivo) que recorre el archivo indicado, conteniendo por ejemplo la
información de un cronograma sugerido de cursada, y devuelve la información como una lista de diccionarios.
Las claves de los diccionarios son las columnas del archivo, y los valores son las entradas de cada fila para esa
columna.\
Definir una función materias_cuatrimestre(nombre_archivo, n) que recorra el archivo
indicado, conteniendo información de un cronograma sugerido de cursada, y devuelva una lista
de diccionarios con la información de las materias sugeridas para cursar el n-ésimo cuatrimestre.
Debe funcionar así:

```
materias_cuatrimestre('cronograma_sugerido.csv', 3):
[{'Cuatrimestre': '3',
'Asignatura': 'Álgebra I',
'Correlatividad de Asignaturas': 'CBC'},
{'Cuatrimestre': '3',
'Asignatura': 'Algoritmos y Estructuras de Datos I',
'Correlatividad de Asignaturas': 'CBC'}]
```

Código:
```
def registros(nombre_archivo):
    lista = []
    with open(nombre_archivo, 'rt') as f:
            filas = csv.reader(f)
            encabezado = next(filas)
            for fila in filas:
                registro = dict(zip(encabezado,fila)) # Arma el diccionario de cada fila
                lista.append(registro) # Agrega el diccionario a la lista
    return lista

def materias_cuatrimestre(nombre_archivo, n):
    datos = registros(nombre_archivo)
    res = []
    for d in datos:
        if int(d[cuatrimestre]) == n:
            res.append(d)
            
```