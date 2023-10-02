import pandas as pd
import os
from inline_sql import sql, sql_val
from matplotlib import pyplot as plt

archivo = 'prices.csv'
directorio = '/home/clinux01/Descargas'

fname = os.path.join(directorio, archivo)
df = pd.read_csv(fname)

archivo1 = 'penguins_size.csv'
fname = os.path.join(directorio, archivo1)
df_ping = pd.read_csv(fname)


# Precio máximo histórico

consultaSQL = """ 
                SELECT d1.symbol,d1.high as Precio_max_historico, d1.date as Fecha
                FROM df as d1
                WHERE symbol = 'R' AND d1.high >=(
                                                 SELECT max(d2.high)
                                                 FROM df as d2
                                                 WHERE d2.symbol = d1.symbol 
                                                 )
                
                
               """

resultado = sql^consultaSQL

print(resultado)

# Precio mínimo histórico

consultaSQL = """ 
                 SELECT d1.symbol, d1.low as Precio_min_historico, d1.date as Fecha
                FROM df as d1
                WHERE symbol = 'R' AND d1.low <=(
                                                 SELECT min(d2.low)
                                                 FROM df as d2
                                                 WHERE d2.symbol = d1.symbol 
                                                 )
                
                
               """

resultado = sql^consultaSQL

print(resultado)

# Racha más larga de crecimiento

df2 = df[df['symbol'] == 'R']

def crecimiento(df2):
    racha = 0
    rachaHistorica = 0
    for i in range(1, len(df2['high'])+1,1):
        if df['high'][i] >= df['high'][i-1]:
            racha += 1
        else: 
            if racha > rachaHistorica:
                rachaHistorica = racha
            else:
                racha = 0
        
    return rachaHistorica

print(crecimiento(df2))

# Racha más larga de decrecimiento

def decrecimiento(df2):
    racha = 0
    rachaHistorica = 0
    for i in range(1, len(df2['high'])+1,1):
        if df['low'][i] <= df['low'][i-1]:
            racha += 1
        else: 
            if racha > rachaHistorica:
                rachaHistorica = racha
            else:
                racha = 0
        
    return rachaHistorica

print(decrecimiento(df2))
