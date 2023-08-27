import pandas as pd
import os

archivo1 = 'arbolado-en-espacios-verdes.csv'
archivo2 = 'arbolado-publico-lineal-2017-2018.csv'
directorio = '/Users/augus/OneDrive/Escritorio/Exactas/2do_ano/2c2023/Labo de datos'

fname1 = os.path.join(directorio,archivo1)
data_arboles_parque = pd.read_csv(fname1)

fname2 = os.path.join(directorio, archivo2)
data_veredas = pd.read_csv(fname2)

# Ejercicio 1
###############################################################################
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
#################################################################################

# Ejercicio 2
################################################################################
cols_sel = ['nombre_cientifico', 'ancho_acera', 'diametro_altura_pecho', 'altura_arbol']
data_arboles_veredas = data_veredas[cols_sel].copy()
cant_arboles = data_arboles_veredas['nombre_cientifico'].value_counts()
cant_arboles.head(10)
especies_seleccionadas = ['Tilia x moltkei', 'Jacaranda mimosifolia', 'Tipuana tipu']

df_lineal_seleccion = data_arboles_veredas[data_arboles_veredas['nombre_cientifico'].isin(especies_seleccionadas)]



################################################################################

#Ejercicio 3
################################################################################

df_tipas_parques = data_arboles_parque[data_arboles_parque['nombre_cie'] == 'Tipuana Tipu'][['altura_tot', 'diametro']].copy()
df_tipas_veredas = df_lineal_seleccion[df_lineal_seleccion['nombre_cientifico'] == 'Tipuana tipu'][['diametro_altura_pecho', 'altura_arbol']].copy()
df_tipas_veredas.rename(columns={'diametro_altura_pecho' : 'diametro', 'altura_arbol' : 'altura_tot'}, inplace = True)
# inplace = True modifica nuestra variable
df_tipas_parques.insert(2, 'ambiente', 'parque')
df_tipas_veredas.insert(2, 'ambiente', 'vereda')
df_tipas = pd.concat([df_tipas_veredas, df_tipas_parques])


