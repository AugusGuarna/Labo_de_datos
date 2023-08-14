# 1era clase

## Contenidos

1. Python 
2. Python tutor
3. Tipos de datos básicos + operaciones
4. Tipos de datos compuestos + operaciones
5. Condicional y ciclos 
6. Ejercicios
--------------------------------------------------
## Python
* Se puede ejecutar en terminal y programar desde aquí asignando valor a variables o manipulándolas. 
* Los comentarios en Python se realizan con # o abriendo y cerrando: ´´´ .
* No hace falta explicitar el tipo de las variables. Si queremos conocerlo podemos usar el comando ```type()```.
* Incluye una función para imprimir valores que se llama ```print()``` . Podemos incluir más de un parámetro de entrada y podemos utilizar parámetros de distinto tipo. Cuando incluimos más de un parámetro los imprime con un espacio entre sí.

```
print(‘Esta clase es la número ’, 0)
```
Devuelve

``` 
Esta clase es la número 0
```

### Python tutor

Es una herramienta que permite la visualización de los procesos relacionados a la ejecución de un programa. Se accede desde [acá](https://pythontutor.com/).


## Tipos de datos básicos + operaciones

### Int
Representan los enteros.\
Entre las operaciones tenemos: ```+```, ```-```, ```*```, ```//``` (divisón entera), ```**``` (potenciación), ```%``` (módulo).

### Float
Representan los reales.\
Valen las mismas operaciones solo que para la división ahora podemos usar ```/```.
Se pueden comparar datos del tipo ```int``` con datos del tipo ```float```.

### Bool
Representan los valores de verdad: true y false.\
Se escriben ```True``` y ```False```.\
Para usar los conectores lógicos escribimos: ```and``` & ```or```.\
En el caso de la negación usamos ```not```.\
Para comparar podemos seguir utilizando ```<```, ```>```, ```<=```, ```>=```, ```==```, ```!=```.

## Tipos de datos compuestos + operaciones

### Strings
Son **_inmutables_**, es decir, una vez declaradas en una variable no podemos modificar algunos ```char```.\
Se construyen con comillas dobles o simples.

#### Operaciones
Supongamos que tenemos las siguientes strings
```
fraseDelDia = ‘Hoy es lunes’
fraseComienzo = ‘empiezo labo de datos’
```
Con ellas podemos realizar las siguientes operaciones:

* Concatenación. Usamos el operador ```+``` . Con este operador podemos agregar más elementos a una string determinada
* Acceder a un elemento en una posición determinada. Usamos el operador ```[]``` . Con este operador podemos usar números negativos siendo el ```[-1]``` el último elemento, el ```[-2]``` el anteúltimo y así.
* Acceder a elementos en un cierto rango. Usamos el operador ```[desde : hasta]``` donde el hasta es excluyente.
* Conocer si un elemento pertenece. Usamos el operador ```in``` .
* Conocer si un elemento NO pertenece. Usamos el operador ``` not in``` .
* Repetir más de una vez una string. Usamos el operador ```*``` .
* Conocer la longitud. Usamos el operador ```len()``` .
* Pasar toda una string a minúscula. Usamos el operador ```.lower()``` .
* Pasar toda una string a mayúscula. Usamos el operador ```.upper()``` .

```
s = fraseDelDia + fraseComienzo    # 'Hoy es lunesempiezo labo de datos'

fraseDelDia += "!"    # 'Hoy es lunes!' Vemos que se puede usar el += como en C++

fraseComienzo[4]    # esta operación devuelve 'e'

fraseDelDia[4:8]    # Corresponde a ‘es l’ (excluye la posición 8)

fraseDelDia[4:]    # Corresponde a ‘es lunes’

fraseDelDia[:5]    # Corresponde a ‘Hoy e’ (excluye la posición 5)

len(fraseDelDia)    # Devuelve 12

'e' in fraseDelDia    # Devuelve True

'o' not in fraseDelDia    # Devuelve False

fraseDelDia * 4    # Devuelve 'Hoy es lunesHoy es lunesHoy es lunesHoy es lunesHoy es lunes'

fraseDelDia.lower()    # Devuelve 'hoy es lunes'

fraseDelDia.upper()    # Devuelve 'HOY ES LUNES'
```

### Listas

Son **_mutables_** y pueden almacenar cualquier tipo de datos. Se construyen usando corchetes ```[]``` .

#### Operaciones
Valen las mismas operaciones a excepción de ```.upper()```,  ```.lower()``` y  ```*``` . Además agregamos las que se van a listar a continuación.\
Supongamos que tenemos las siguientes listas y un string.

```
lista_numeros = [10, 43, 22, 5, 63, 101, -5, 3]

lista_nombres = [‘Julia’, ‘Luciana’, ‘Manuel’]

frutas = 'Frambuesa,Manzana,Naranja,Mandarina,Banana,Sandía,Pera'
```
Con ellas podemos:
* Agregar un elemento al final. Usamos la operación ```.append(elem)``` .
* Agregar un elemento en una posición determinada. Usamos la operación ```.insert(pos, elem)``` .
* Ordenar la lista. Usamos la operación ```.sort()``` .
* Remover un elemento. Usamos la operación ```.remove(elem)```
* Convertir un string en una lista. Usamos la operación ```.split(criterio)```

```
lista_numeros.append (19) # Agrega el 19 al final

lista_nombres.insert(2, "Ana") # Agrega "Ana" a la posición 2 y desplaza todo una posición para la derecha

lista_numeros.sort() # La ordena

lista_nombres.remove("Julia") # Devuelve la lista sin Julia

lista_numeros[0] = 99 # Como son tipos mutables a partir de ahora en la posición 0 de la lista tendremos al número 99

lista_frutas = frutas.split(",") # Devuelve una lista cuyos elementos son los de la string. En este caso cuando encuentra el caracter "," realiza un corte y todo lo que esté por delante pasa a una posición.
```



### Matrices

Podemos utilizar listas de listas donde cada lista es una fila distinta.

#### Operaciones

Valen las operaciones mencionadas para listas. ¡El operador ```+``` concantena dos matrices ojo!

### Tuplas
Son **_inmutables_**. Son como vectores y se arman con paréntesis ```()``` .

#### Operaciones
Valen las operaciones mencionadas para listas. ¡El operador ```+``` concantena dos tuplas ojo!.

### Conjuntos

Se arman con llaves ```{}``` .

#### Operaciones

Vamos a ver las operaciones típicas utilizando una lista y un conjunto.

```
citricos = {‘Naranja’, ‘Limón’, ‘Mandarina’} 

citricos = [‘Naranja’, ‘Limón’, ‘Mandarina’]
```
Con estos podemos:
* Transformar una lista en un conjunto. Usamos la operación ```set()``` .
* Checkear pertenencia. Usamos el operador ```in``` .
* Agregar y remover elementos. Usamos las operaciones ```.add()``` y ```.remove()``` respectivamente.
* Conocer el cardinal. Usamos la operación ```len()``` .

```
citricos = set([‘Naranja’, ‘Limón’, ‘Mandarina’]) # Transforma una lsita en un conjunto

‘Naranja’ in citricos # ¿Pertenece?

citricos.add(‘Pomelo’) # Agrega un elemento

citricos.remove(‘Naranja’) # Elimina un elemento

len(citricos)
```

## Condicional y ciclos


### Condicional

Cuando hablamos de condición hablamos de condición booleana.

```
if condicion1:
 instruccion1
 instruccion2
elif condicion2:
 instruccion3
else:
 instruccion4
```

### Ciclos

#### While

```
i = x
while condicion:
    instruccion1
    instruccion2
    instrucción sobre como incrementar o decrementar i
```

##### For
```
for i in range (inicio, fin, paso):
    instrucciones
```
Cuando se habla de fin y de paso se está hablando hasta que valor (excluyente) se aumenta la variable y cuánto se aumenta respectivamente.

## Ejercicios 

### Ejercicio 1

Escribir un programa que imprima en pantalla los números enteros entre 0 y 213 que sean divisibles por 13.

```
1	for i in range(213):
2	    if i % 13 == 0:
3	        print (i)
```

### Ejercicio 2

Una mañana ponés un billete en la vereda al lado del obelisco porteño. A partir de ahí, cada día vas y duplicás la cantidad de billetes, apilándolos prolijamente. ¿Cuánto tiempo pasa antes de que la pila de billetes sea más alta que el
obelisco?\
Datos: espesor del billete: 0.11 mm, altura obelisco: 67.5 m

```
1	alturaObelisco = 67.5 * 1000;
2	espesor = 0.11;
3	dia = 0;
4	while (espesor < alturaObelisco): 
5	    dia+=1;
6	    espesor = 2*espesor;
```

### Ejercicio 3

Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

```
1	vocales = "aeiouAEIOU"
2	cadena = 'Geringoso'
3	capadepenapa = ''
4	for c in cadena:
5	    capadepenapa += c;
6	    if c in vocales:
7	        capadepenapa += "p"+ c
8	print(capadepenapa) # Geperipingoposop
```

#### Ejercicio 4

Una pelota de goma es arrojada desde una altura de 100 metros y cada vez que toca el piso salta 3/5 de la altura desde la que cayó. Escribí un programa que imprima una tabla mostrando las alturas que alcanza en cada uno de sus primeros diez rebotes.

```
1	altura = 100
2	for i in range(10):
3	    altura = altura * (3/5)
4	    print (i+1, altura)
```

#### Ejercicio 5
Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra. Como primera aproximación, completá el siguiente código para reemplazar todas las letras 'o' que figuren en el último o anteúltimo
caracter de cada palabra por una 'e'. Por ejemplo 'todos somos
programadores' pasaría a ser 'todes somes programadores'.

```
1	frase = 'todos somos programadores'
2	palabras = frase.split()
3	frase_t = ''
4	for palabra in palabras:
5	    if palabra[len(palabra) - 1] == "o" or palabra[len(palabra) - 2] == "o":
6	        for i in range(len(palabra)):
7	            if palabra[i] == "o" and (i == len(palabra) - 1 or i == len(palabra) - 2):
8	                frase_t += 'e'
9	            else:
10	                frase_t += palabra[i]
11	        frase_t += ' '
12	    else:
13	        frase_t += palabra
14	print(frase_t)
```
