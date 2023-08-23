# Clase 3
## Contenidos

1. Numpy
2. Pandas
3. Ejercicios

## Numpy

* Colección de módulos de código abierto
* Lo usan muchas bibliotecas
* Provee matrices multidimensionales por medio del tipo ndarray y permite operar sobre matrices de formas eficientes
```
import numpy as np

import numpy as np 

a = np.array([1,2,3,4,5,6])
b = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

print(a[0])
print(b[0])
print(b[0][1])
print(b[0,1])

c = np.zeros((2,3)) #Array de 0 elementos
d = np.ones((2,3)) 

e = np.arange(4) # Vector de 4 elementos creciente que arranca en 0
f = np.arange(-2) # Vacío
g = np.arange(2,9,2) # Vector de los elementos del 2 al 9 saltando de 2 en 2. El 9 no lo incluye. Es exclusive porque sería como la "longitud"
h = np.linspace(0,10, num = 5) # Vector de 5 números equiespaciados que van del 0 al 10. El 10 lo incluye. Es inclusive. Se usa para hacer gráficos


a = np.array([1,2,3,4])
b = np.array([5,6,7,8])
c = np.concatenate((a,b))

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])
z = np.concatenate((x,y), axis = 0) # Pega la matriz una debajo de la otra
t = np.concatenate((x,y), axis = 1) # Pega una al lado de la otra


array_ejemplo = np.array( [
                    [[0,1,2,3],[4,5,6,7]],
                    [[3,8,10,-1],[0,1,1,0]],
                    [[3,3,3,3],[5,5,5,5]]
                ] ) #Matriz de 3 dimensiones

array_ejemplo.ndim # Dimensión
array_ejemplo.shape # Distancia en cada eje
array_ejemplo.size # Cantidad de elementos

nueva1 = array_ejemplo.reshape((12,2)) #Paso los elementos a una matriz de 12x2
nueva2 = array_ejemplo.reshape((3,-1)) #El -1 es una manera de decirle hace lo que corresponda

enumerate (M) devuelve tupla (índice de la fila, vector que representa fila)
enumerate(fila) devuelve tupla (indice de la fila, elem)
```
## Pandas 

* Es una extensión de numpy para manipular y analizar datos
* Ofrece estructuras de datos y operaciones para manipular **tablas de datos** y **series temporales**
* Data frames = almacenan tablas de datos
* Series temporales = almacenan secuencias de datos

```
import panda as pd
```

Poniendolo a prueba

```
import pandas as pd
import os

archivo = 'arbolado-en-espacios-verdes.csv'
directorio = './Descargas/'

fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)


df.head(5)
df.columns
df[['altura_tot','diametro']].describe()
df['nombre_com'] == 'Ombú' #Devuelve una lista con true y false donde true es ombú y donde false no
(df['nombre_com'] == 'Ombú').sum()
df['nombre_com'].unique() #Devuelve todas las especies

cant_ejemplares = df['nombre_com'].value_counts() #Devuelve todas las especies con su cantidad de ejemplares
#Es como unique y sum
cant_ejemplares.head(10) #Devuelve el top 10 

df_jacarandas = df[df['nombre_com'] == 'Jacarandá'] #Solo va a agarrar los jacarandás
#"Data frame" de jacarandás pero más chico que el original
cols = ['altura_tot', 'diametro', 'inclinacio']
df_jacarandas = df_jacarandas[cols]
#Filtro más todavía el data frame
df_jacarandas.tail()

#Sin embargo, esto es una referencia. No es una copia

df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()
#Ahora sí lo copie

#Al registro podemos accederlo tanto por posición con iloc (como hacíamos con los arrays) como por
#índice con loc (especie de clave)
#El índice se genera cuando levantamos el data frame 

df_jacarandas.iloc[0]
#De mi nuevo data frame numera de 0 a n las posiciones en la memoria interna por lo tanto lo puedo indexar como un array

df_jacarandas.loc[165]
#En mi nuevo data frame se generan índices que pueden ser o no numéricos 

#También podemos acceder a un slice

df_jacarandas.iloc[0:2,1:3]

#Se puede seleccionar una sola columna especificando su nombre.
#Importante. Al tomar una sola columna se obtiene una serie en lugar de un DataFrame

diametros = df_jacarandas['diametro']
type(df_jacarandas) #pandas.core.frame.DataFrame
type(diametros) # pandas.core.series.Series

```

Con `df.head()` podés ver las primeras líneas de datos. Si a head le pasás un número como argumento podés seleccionar cuántas líneas querés ver. Análogamente con `df.tail(n)` verás las últimas n líneas de datos.

Con `df.columns` vemos las columnas.

Con `df[columnas (si es más de una es lista de listas)]`.describe() nos da una tabla con ciertas características

## Ejercicios
### Ejercicio 1

Generá un vector que contenga los números impares entre el 1 y el 19 inclusive usando arange() y linspace()
```
numerosImpares1 = np.arange(1,20,2)
numerosImpares2 = np.linspace(1,19,num = 10)
```

### Ejercicio 2

Definir una función pisar_elemento(M,e) que tome una matriz de enteros M y un entero e y devuelva una matriz similar a M donde las entradas coincidentes con e fueron cambiadas por -1.

```
def pisar_elemento(M,e):
    nlin, ncol = M.shape
    for i in range(nlin):
        for j in range(ncol):
            if M[i][j] == e:
               M[i][j] = -1 
    return M
```

Sin embargo, si no sabemos la dimensión de la matriz podemos convertirla primero en un vector con flatten o reshape, luego la recorremos y finalmente le devolvemos su forma.


```
import pandas as pd
import numpy as np
import os

archivo = 'arbolado-en-espacios-verdes.csv'
directorio = './Descargas/'

fname = os.path.join(directorio,archivo)
data_arboles_parques = pd.read_csv(fname)

data_arboles_parques['nombre_com'].unique()
data_arboles_parques.columns
data_jacarandas = data_arboles_parques[data_arboles_parques['nombre_com'] == 'Jacarandá'].copy()
data_palos_borrachos= data_arboles_parques[data_arboles_parques['nombre_com'] == 'Palo borracho'].copy()
cantidad_jacarandás = (data_arboles_parques['nombre_com'] == 'Jacarandá').sum()#data_jacarandas[0].shape()
cantidad_palos_borrachos = (data_arboles_parques['nombre_com'] == 'Palo borracho').sum()
cols = ['altura_tot', 'diametro']
data_jacarandas = data_jacarandas[cols]
data_jacarandas.describe()
data_palos_borrachos = data_palos_borrachos[cols]
data_palos_borrachos.describe()


def cantidad_arboles(parque):
    data_parque = data_arboles_parques[data_arboles_parques['espacio_ve'] == parque]
    return data_parque.shape[0] #Shape me da el tamaño del eje. Por lo tanto con tomar el 0 ya está
print(cantidad_arboles('GENERAL PAZ'))

def cantidad_nativos(parque):
    data_parque = data_arboles_parques[data_arboles_parques['espacio_ve'] == parque]
    data_parque = data_parque[]
```