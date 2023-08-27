# Clase 3
## Contenidos

1. Numpy
2. Pandas
3. Ejercicios

## Numpy

* Colección de módulos de código abierto
* Lo usan muchas bibliotecas
* Provee matrices multidimensionales por medio del tipo nd.array y permite operar sobre matrices de formas eficientes

### Algunas funciones útiles

#### Creación de arrays

* Crear un array: ```np.array()```
    * Para crear vectores hacemos ```np.array([])```
    * Para crear matrices hacemos ```np.array([[][][]])```
        * Esto crea una matriz de una dimensión pero podemos tener de más como 
        ```
        array_ejemplo = np.array( [
                    [[0,1,2,3],[4,5,6,7]],
                    [[3,8,10,-1],[0,1,1,0]],
                    [[3,3,3,3],[5,5,5,5]]
                ] ) #Matriz de 3 dimensiones
        ```
* Array de 0s y array de 1s:  ```np.zeros(()) & np.ones(()) ```
* Crear un array de elementos crecientes y ordenados arrancando de 0: ```np.arange()``` 
    * Si el número es negativo lo crea vacío 
    * Podemos explicitarle comienzo, final (no lo incluye) y el salto: ```np.arrange(inicio, fin, paso)```
* Crear un vector de números equiespaciados: ```np.linspace(inicio, fin, cantidad de números)```
    * En este caso el fin es incluido
    * Herramienta potente para graficar

#### Manipulación de arrays
* Para concatenar dos arrays: ```np.concatenate(())```
    * Si son vectores pega uno después del otro
    * Si son matrices cambia la cosa
        * Para pegar una matriz debajo de otra: ```np.concatenate((), axis = 0)```
        * Para pegar una al lado de la otra: ```np.concatenate((), axis = 1)```

* Para obtener la dimensión de un array: ```array_name.ndim```
* Para obtener la distancia en cada eje: ```arra_name.shape```
    * Devuelve una tupla
* Para obtener la cantidad total de elementos: ```array_name.size```

* Para cambiar la forma del array: ```array_name.reshape((filas,col))```
    * Si alguno de los parámetros es -1 entonces le estamos indicando que para esa cantidad de filas o columnas haga lo que corresponda

* Para iterar:
    * ```enumerate(M)``` devuelve tupla (índice de la fila, vector que representa fila)
    * ```enumerate(fila)``` devuelve tupla (indice de la fila, elem)

## Pandas 

* Es una extensión de numpy para manipular y analizar datos
* Ofrece estructuras de datos y operaciones para manipular **tablas de datos** y **series temporales**
* Data frames = almacenan tablas de datos
* Series temporales = almacenan secuencias de datos

```
import panda as pd
```

### Abrir archivos 

```
import pandas as pd
import os

archivo = 'arbolado-en-espacios-verdes.csv'
directorio = './Descargas/'

fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)
```
### Algunas funciones de data frames

* Para conocer las n primeras filas: ```df.head(n)```
* Para conocer las últimas n filas: ```df.tail(n)```
* Para conocer las columnas (es decir, las categorías): ```df.columns```
* Para conocer ciertas características de las columnas: ```df[[columna1, columna2,...]].describe```
* Supongamos el data frame del ejemplo
    * ```df['nombre_com'] == 'Ombú'``` devuelve una lista con True y False donde True representa a los ombúes
        * Se puede usar para cualquier dataframe siempre que sepamos el nombre de la columna y la variable a buscar
    * ```(df['nombre_com'] == 'Ombú').sum()``` suma todos los ombúes
        * Se puede generalizar
    * ```df['nombre_com'].unique()``` devuelve todas las especies
        * Se puede generalizar
* A partir de nuestro data frame podemos generarnos otros y podemos generar series temporales
    * En el ejemplo ```cant_ejemplares = df['nombre_com'].value_counts()``` nos devuelve todas las especies con su cantidad de ejemplares. Es una serie temporal donde los índices son los nombres de las especies y los significados la cantidad de cada una
        * Se puede generalizar y valen algunas operaciones que ya vimos como: ```cant_ejemplares.head(10)```
        * En general, **AL TOMAR UNA SOLA COLUMNA SE OBTIENE UNA SERIE TEMPORAL** 
    * En el ejemplo ```df_jacarandas = df[df['nombre_com'] == 'Jacarandá']``` crea un data frame pero solo acerca de los jacarandás
        * Con ```cols = ['altura_tot', 'diametro', 'inclinacio'] df_jacarandas = df_jacarandas[cols]``` lo filtramos todavía más
        * Sin embargo, esto es una referencia no una copia
            * Para copiar ```df_jacarandas = df[df['nombre_com'] == 'Jacarandá'][cols].copy()```
* También podemos trabajar con índices en el data frame:
    * ```df.iloc[index]``` nos permite acceder a los elementos como en un array. Cuando se crea el data frame se numera de 0 a n las posiciones en la memoria interna por lo tanto lo puedo indexar como un array
    * ```df.loc[clave]``` en el data frame se generan una especie de índices que pueden ser alfa numéricos o no 
    * Podemos también hacer un slice 
        * ```df_jacarandas.iloc[0:2,1:3]```
* Podemos renombrar columnas: ```dataframe.rename({columnas_orig : columna_nueva}, inplace = True)```
    * ```Inplace = True ``` modifica el nombre de la columna del dataframe de nuestra memoria
* Podemos insertar columnas en el dataframe de nuestra memoria: ```dataframe.inser(index, 'nombre', 'elemento a contener')``` donde el indice debe ser un número entre 0 y la cantidad de columnas que tenemos
* Podemos concatenar 2 dataframes: ```pd.concat(dataframe, dataframe)``` 

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

### Ejercicio 3

A partir del dataset ’arbolado-en-espacios-verdes.csv’ que contiene datos relacionados con el censo de arbolado realizado
durante el año 2011 en la Ciudad de Bs. As. (también lo pueden descargar del campus), hacer lo siguiente:
1. Cargar la información del archivo csv en un dataframe denominado data_arboles_parques
2. Armar un dataframe que contenga las filas de los Jacarandás
3. Armar un dataframe que contenga las filas de los Palos Borrachos
4. Para cada uno de estos dos dataframes calcular:
    * Cantidad de árboles;
    * altura máxima, mínima y promedio;
    * diámetro máximo, mínimo y promedio
5. Definir las siguientes funciones:
    * cantidad_arboles(parque) que dado el nombre de un parque calcule la cantidad de árboles que tiene
    * cantidad_nativos(parque) que dado el nombre de un parque calcule la cantidad de árboles nativos.
```
data_jacarandas = data_arboles_parque[data_arboles_parque['nombre_com'] == 'Jacarandá'].copy()
data_palos_borrachos = data_arboles_parque[data_arboles_parque['nombre_com'] == 'Palo borracho'].copy()

# Para saber la cantidad de jacarandás puedo o ir al data frame original y contar
# O tomar el data frame preguntar su dimensión y tomar la cantidad de filas
cantidad_jacarandas = data_jacarandas.shape[0]
cantidad_palo_borrachos = data_palos_borrachos.shape[0]

data_jacarandas[['altura_tot', 'diametro']].describe()
data_palos_borrachos[['altura_tot', 'diametro']].describe()

def cantidad_arboles(parque):
    df_parque = data_arboles_parque[data_arboles_parque['espacio_ve'] == parque]
    return df_parque.shape[0]

print(cantidad_arboles('GENERAL PAZ'))

def cantidad_nativos(parque):
    df_parque = data_arboles_parque[data_arboles_parque['espacio_ve'] == parque]
    df_nativos = df_parque[df_parque['origen'] == 'Nativo/Autóctono']
    return df_nativos.shape[0]

```

### Ejercicio 4
A partir del dataset 'arbolado-publico-lineal-2017-2018.csv', que contiene datos relacionados con el arbolado público,
localizado en la traza de la Ciudad de Bs. As. (también lo pueden descargar del campus), hacer lo siguiente:

1. Cargar la información del archivo csv en un dataframe denominado data_arboles_veredas . El dataset debe tener solamente las siguiente columnas: ```cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']```
2. Imprimir las diez especies más frecuentes con sus respectivas cantidades
3. Trabajaremos con las siguientes especies seleccionadas: ```especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']```. 
Una forma de seleccionarlas es la siguiente: ```df_lineal_seleccion = df_lineal[df_lineal['nombre_cientifico'].isin(especies_seleccionadas)```

```
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
data_arboles_veredas = data_veredas[cols_sel].copy()
cant_arboles = data_arboles_veredas['nombre_cientifico'].value_counts()
cant_arboles.head(10)
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = data_arboles_veredas[data_arboles_veredas['nombre_cientifico'].isin(especies_seleccionadas)]

```

### Ejercicio 5

Proponemos los siguientes pasos para comparar los diámetros a la altura del pecho de las tipas en ambos tipos de
entornos (datasets):
1. Para cada dataset armar uno nuevo (denominarlos df_tipas_parques y df_tipas_veredas, respectivamente) seleccionando sólo las filas correspondientes a las tipas y las columnas correspondientes al diámetro, a la altura del pecho y alturas. Importante. Hacerlo como copias (usando .copy() como aprendimos previamente) para poder trabajar en estos nuevos dataframes sin modificar los dataframes grandes originales.
2. Renombrar las columnas que muestran la altura y el diámetro a la altura del pecho para que se llamen igual en ambos dataframes. Ayuda. Explorar el comando rename.
3. Agregar a cada dataframe (df_tipas_parques y df_tipas_veredas) una columna llamada 'ambiente', que en un caso valga siempre 'parque' y en el otro caso siempre 'vereda'.
4. Juntar ambos datasets con el comando df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques]). De esta forma tendremos en un mismo dataframe la información de las tipas distinguidas por ambiente

```

df_tipas_parques = data_arboles_parque[data_arboles_parque['nombre_cie'] == 'Tipuana Tipu'][['altura_tot', 'diametro']].copy()
df_tipas_veredas = df_lineal_seleccion[df_lineal_seleccion['nombre_cientifico'] == 'Tipuana tipu'][['diametro_altura_pecho', 'altura_arbol']].copy()
df_tipas_veredas.rename(columns={'diametro_altura_pecho' : 'diametro', 'altura_arbol' : 'altura_tot'}, inplace = True)
# inplace = True modifica nuestra variable
df_tipas_parques.insert(2, 'ambiente', 'parque')
df_tipas_veredas.insert(2, 'ambiente', 'vereda')
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])


```