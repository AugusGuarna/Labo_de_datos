# -*- coding: utf-8 -*-
"""
Materia     : Laboratorio de datos - FCEyN - UBA
Clase       : Clase Regresion Lineal
Detalle     : Modelo de Regresion Lineal Simple
Autores     : Maria Soledad Fernandez y Pablo Turjanski
Modificacion: 2023-10-13
"""

# Importamos bibliotecas
import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt
import seaborn as sns
from inline_sql import sql, sql_val

# Modelos categóricos: arboles de decisión

# Modelos contínuos: regresión lineal simple 

# Población = todos los individuos posibles, observamos una muestra solamente
# Estimadores estiman parámetros reales de la ecuación
# Mejor recta = residuos casi iguales para todos los puntos 
# Es al cuadrado para que sea derivable y porque va a tener minimo

#%%
####################################################################
########  DEFINICION DE FUNCIONES AUXILIARES
####################################################################

# Dibuja una recta. Toma como parametros pendiente e intercept
def plotRectaRegresion(slope, intercept):
    """Plot a line from slope and intercept"""
    axes = plt.gca()
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, color="red")

#%%

####################################################################
########  MAIN
####################################################################
# Cargamos el archivo 
carpeta = '~/Descargas/'
data_train = pd.read_csv(carpeta+"datos_roundup.txt", sep=" ", encoding='utf-8')

""" CAMBIAR ALGO QUE NO ES TXT A CSV, SE HACE ASÍ """


# ----------------------------------
# ----------------------------------
#       Modelo Lineal Simple (rls)
# ----------------------------------
# ----------------------------------
#  X = RU (variable predictora) [Dosis de Roundup]
#  Y = ID (variable a predecir) [Damage Index]
########################
## Generacion del modelo
########################
# Declaramos las variables

X = data_train[['RU']]
Y = data_train[['ID']]
""" DOBLE CORCHETE TE LO ARMA COMO DF Y NO COMO SERIE """

# Declaramos el tipo de modelo

rls = linear_model.LinearRegression()

# Entrenamos el modelo

rls.fit(X, Y)

""" Con fit se entrena """

# Observamos los valores obtenidos (pendiente e intercept)
print("Coeficientes")
print("----------")
print("intercept :", rls.intercept_[0])
print("intercept :", rls.coef_[0][0])

###############################################
## Visualizacion del modelo vs valores de TRAIN
###############################################
# Graficamos una dispersion de pu12906ntos de ID en funcion de la Dosis de RU
ax = sns.scatterplot(data = data_train, x = 'RU', y = 'ID', s=40, color = 'black')
""" s=40 es el size del punto """

ax.set_xlabel('Dosis de RU (ug/huevo)', fontsize=12)
ax.set_ylabel('Índice de daño', fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])

# Ordenada al origen = valor medio del índice de daño cuando el valor es 0

#####################################
## Prediccion
#####################################
# Cargamos el archivo (no posee valores para ID)
carpeta = '~/Descargas/'
data_a_predecir = pd.read_csv(carpeta+"datos_a_predecir.txt", sep=" ", encoding='utf-8')

# Realizamos la prediccion de ID utilizando el modelo y
# la asignamos a la columna ID

data_a_predecir[['ID']] = rls.predict(data_a_predecir[['RU']])
# Se puede hacer para un solo valor con una consulta de SQL
# Para árboles es la misma


# Graficamos una dispersion de puntos de ID en funcion de la Dosis de RU
# Graficamos tanto los puntos de entrenamiento del modelo como los predichos

ax = sns.scatterplot(data = data_train, x = 'RU', y = 'ID', s=40, color = 'black')
ax = sns.scatterplot(data = data_a_predecir, x = 'RU', y = 'ID', s=40, color = 'blue')
# Para agregar otros puntos de otro DF
ax.set_xlabel('Dosis de RU (ug/huevo)', fontsize=12)
ax.set_ylabel('Índice de daño', fontsize=12)
plotRectaRegresion(rls.coef_[0][0], rls.intercept_[0])

#####################################
## Evaluacion del modelo contra TRAIN
#####################################
#  R2

y_pred1 = rls.predict(X)
print('R2(TRAIN) : %.2f' % r2_score(Y,y_pred1))

""" LE PASAMOS LOS Y OBSERVADOS VS LOS QUE PREDIJO """

rls.score(X,Y)
""" CON ESTE SOLO LE PASAS LOS VALORES """



###################################################################################
# EJ CLASE

experimento = pd.read_csv('./datos_libreta_24822.txt', sep= " ", encoding = 'utf-8')

exgraf = sns.scatterplot(data = experimento, x = 'RU', y = 'ID')
exgraf.set_xlabel('Dosis de RU (ug/huevo)')
exgraf.set_ylabel('Índice de daño')
plotRectaRegresion(rlsex.coef_[0][0], rlsex.intercept_[0])

rlsex = linear_model.LinearRegression()
rlsex.fit(experimento[['RU']],experimento[['ID']] )
print(rlsex.intercept_[0], rlsex.coef_[0][0])
rlsex.score(experimento[['RU']],experimento[['ID']] )


















