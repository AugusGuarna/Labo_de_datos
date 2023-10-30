#!/usr/bin/env python
# coding: utf-8

# # Evaluación de Modelos
# 
# **Objetivo:** dada los datos de una canción (una fila en nuestro dataset) poder predecir si esta en Folklore o Evermore o es de otro álbum.
# 
# **Datos:** dataset con distintas variables de las canciones de Taylor Swift.

# In[1]:


import pandas as pd 
import utils


# #### Cargamos el dataset -- la función load_dataset limpia un poco los datos

# In[2]:


df_taylor = utils.load_dataset_taylor("./taylor_album_songs.csv")
df_taylor.head()


# ### Separemos los labels y eliminamos el nombre de la canción

# In[ ]:


X = df_taylor.drop(columns = ['track_name', 'is_folklore_or_evermore'])
y = df_taylor['is_folklore_or_evermore']


# In[4]:

from sklearn.tree import DecisionTreeClassifier

arbol = DecisionTreeClassifier(criterion="entropy", max_depth = 5)
arbol.fit(X,y)  #le ponemos el dataframe sobre el cual va a laburar y el que queremos que prediga

y = arbol.predict(X)
# Complete aqui con su clasificador de preferencia!

#%%

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.1, random_state= 7, stratify= y)

#Label = lo que quiero predecir

from sklearn.model_selection import cross_val_score

cross_val_score(arbol, X, y, cv=5) # YA HACE TODO :D
# cv = cantidad de folds
from sklearn.model_selection import KFold
kf = KFold(n_splits=2, shuffle=True)
X_train, y_test = kf.split(X, y)

kf
arbol.fit()
