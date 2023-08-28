import pandas as pd
import os

archivo = 'Clase-04-Actividad-01-Datos.csv'
directorio = './Descargas/'

fname = os.path.join(directorio,archivo)
df = pd.read_csv(fname)

df.head(10)

df['municipio'].unique()

df1 = df[df['provincia'] == 'Buenos Aires'].copy()
df1.shape[0]
df1['municipio'].unique()
df1['ubicacion'].unique()

print('Las conclusiones son:','\n son los puntos digitales alrededor del país, tenemos cada uno identificado con ubicación exacta en coordenadas, su provincia, su municipio y tenemos tageado cada uno con su identificador', '\n son también lugares estatales')

print('Preguntar con una encuesta')
print('En general como venis:')
print('Tren, bondi, subte, bici, auto, moto')
#df[{'persona': null ,'tren':null,'bondi':null,'subte':null,'bici':null,'auto':null,'moto':null}]
#cols= ['Tren, bondi, subte, bici, auto, moto']
#df = pd.DataFrame(cols)
#print (df)
##############################################################################################

archivo2 = '2023-2C-EncuestaMovilidadRespuestas.csv'
directorio2 = './Descargas/'

fname = os.path.join(directorio2,archivo2)
df2 = pd.read_csv('/home/clinux01/Descargas/2023-2C-EncuestaMovilidadRespuestas.csv')

df2['¿Cuál es el transporte que utilizó hoy para llegar a Ciudad Universitaria? \n- En caso de utilizar más de uno responder en base al trayecto final.'].value_counts()
df2.describe()
df2['¿Cuál es el transporte que utilizó hoy para llegar a Ciudad Universitaria? \n- En caso de utilizar más de uno responder en base al trayecto final.'].describe()
