import pandas as pd
import os

archivo = 'arbolado-en-espacios-verdes.csv'
directorio = '/Users/augus/OneDrive/Escritorio/Exactas/2do_ano/2c2023/Labo de datos'

# El punto inicial nos chingaba todo

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

