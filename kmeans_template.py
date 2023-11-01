# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Aprendizaje No Supervisado
Detalle     : Modelos KMeans
Autores     : Manuela Cerdeiro y Pablo Turjanski
Modificacion: 2023-10-31
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans


#%%
####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
carpeta = './'
data_train = pd.read_csv(carpeta+'datos_clase_clustering.csv', index_col = 0, encoding='utf-8')

#%%
# Analizamos el precio de venta (U$S) por m2 de superficie cubierta. Para ello 
# generamos la variable ppm (precio por m2 de superficie cubierta)
data_train['ppm'] = data_train['price']/data_train['surface_covered']


#%%
# ------------------------------------------
# ------------------------------------------
#       Exploracion de Datos - Propuesta 1
# ------------------------------------------
# ------------------------------------------
# Queremos ver como es la relacion entre el precio de venta por m2 de 
# superficie cubierta (U$S) y la superficie cubierta (m2)


# Para ello visualizamos el precio de venta por m2 de superficie cubierta (U$S)
# en funcion de la superficie cubierta (m2)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm') 
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio de venta por m2 de sup. cubierta (U$S)")

# Eliminamos las variables que ya no utilizamos
del ax

#%%
# ----------------------------------
# ----------------------------------
#       Modelo KMeans - Propuesta 1
# ----------------------------------
# ----------------------------------
#  X1 = surface_covered (variable predictora) [Superficie cubierta (m2)]
#  X2 = ppm             (variable predictora) [Precio por m2 de superficie cubierta (U$S)]
#  k  = Cantidad de grupos
########################
## Generacion del modelo
########################
# Declaramos las variables

Xs = data_train[['surface_covered','ppm']]
k = 3
# Declaramos el tipo de modelo
kmeansps = KMeans(n_clusters=k,random_state=0)

# Entrenamos el modelo

kmeansps.fit(Xs)
# Asignamos las etiquetas predichas a cada fila de nuestro dataset

data_train['cluster']=kmeansps.labels_

# Visualizamos los 3 clusters generados en funcion de su 
# superficie cubierta (m2) y el precio por m2 de la superficie cubierta (U$S)

ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm', hue = 'cluster', pallete='viridis') 
ax.set_xlabel(title=f'Agrupamiento con k = {k}')
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio de venta por m2 de sup. cubierta (U$S)")


# Eliminamos las variables que ya no utilizamos

del Xs, k, ax^

#%%
# ------------------------------------------
# ------------------------------------------
#       Exploracion de Datos - Propuesta 2
# ------------------------------------------
# ------------------------------------------
# Queremos ver como es la relacion entre el precio TOTAL de venta (U$S) 
# y la superficie cubierta (m2)

# Para ello visualizamos el precio total de venta (U$S)
# en funcion de la superficie cubierta (m2)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'price', palette = 'viridis') 
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio total de venta (U$S)")

# Eliminamos las variables que ya no utilizamos
del ax


#%%
# ----------------------------------
# ----------------------------------
#       Modelo KMeans - Propuesta 2
# ----------------------------------
# ----------------------------------
#  X1 = surface_covered (variable predictora) [Superficie cubierta (m2)]
#  X2 = precio          (variable predictora) [Precio total de venta (U$S)]
#  k  = Cantidad de grupos
########################
## Generacion del modelo
########################
# Declaramos las variables
Xs = data_train[['surface_covered', 'price']]
k = 3
# Declaramos el tipo de modelo

kmeansps = Kmeans(n_clusters = k, random_state = 0)

# Entrenamos el modelo

kmeansps.fit(Xs)


# Asignamos las eitquetas predichas a cada fila de nuestro dataset

data_train['cluster']=kmeansps.labels_

# Visualizamos los 3 clusters generados en funcion de su 
# superficie cubierta (m2) y el precio total de venta (U$S)

ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'price', hue = 'clusters', palette = 'viridis') 
ax.set_xlabel(title=f'Agrupamiento con k = {k}')
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio total de venta (U$S)"
# Eliminamos las variables que ya no utilizamos


del Xs,k,ax

#%%
# ------------------------------------------------------
# ------------------------------------------------------
#       Volvemos a la Exploracion de Datos - Propuesta 1
# ------------------------------------------------------
# ------------------------------------------------------
# Queremos ver como es la relacion entre el precio de venta por m2 de 
# superficie cubierta (U$S) y la superficie cubierta (m2). 


# Para ello visualizamos el precio de venta por m2 de superficie cubierta (U$S)
# en funcion de la superficie cubierta (m2)
ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm') 
ax.set_xlabel("Superficie cubierta (m2)")
ax.set_ylabel("Precio de venta por m2 de sup. cubierta (U$S)")

# Eliminamos las variables que ya no utilizamos
del ax

#%%
# ---------------------------------------------------------------
# ---------------------------------------------------------------
#       Modelo KMeans - Probamos rango de valores k - Propuesta 1
# ---------------------------------------------------------------
# ---------------------------------------------------------------
#  X1     = surface_covered (variable predictora) [Superficie cubierta (m2)]
#  X2     = ppm             (variable predictora) [Precio por m2 (U$S)]
#  k_vals = Rango de valores para k
########################
## Generacion del modelo
########################
# Declaramos las variables
Xs = data_train[['surface_covered','ppm']]
k_vals = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]


# En wcss vamos a almacenar el Within-Cluster Sum of Square
# para cada uno de los k utilizados

wcss = []
# Realizamos el modelado, visualiazcion y evaluacion para cada k
for k in k_vals:
    print('k: ', k)
    ### Modelamos 
    # Declaramos el tipo de modelo
    kmeansps = Kmeans(n_clusters = k, n_random= 0)
    # Entrenamos el modelo
    kmeansps.fit(Xs)
    # Asignamos las etiquetas predichas a cada fila de nuestro dataset
    data_train['clusters'] = kmeans.label_

    ### Visualizamos
    # Visualizamos los k clusters generados en funcion de su 
    # superficie cubierta (m2) y el precio por m2 de la superficie cubierta (U$S)
    plt.figure()
    ax = sns.scatterplot(data=data_train, x='surface_covered', y= 'ppm', hue = 'cluster', pallete='viridis') 
    ax.set_xlabel(title=f'Agrupamiento con k = {k}')
    ax.set_xlabel("Superficie cubierta (m2)")
    ax.set_ylabel("Precio de venta por m2 de sup. cubierta (U$S)")
    plt.show()
    
    ### Evaluamos
    # Almacenamos el Within-Cluster Sum of Square del modelo para el k utilizado
    wcss.append(kmeansps.inertia_)   


# Visualizamos el wcss en funcion de la cantidad de grupos (k) para el modelo 
# y los datos utilizados (superficie cubierta y ppm)
plt.plot(k_vals, wcss)
plt.xlabel('k')
plt.ylabel('wcss')
plt.xticks(np.arange(min(k_vals),max(k_vals)+1),1.0)
plt.grid()
plt.show()
# Eliminamos las variables que ya no utilizamos

