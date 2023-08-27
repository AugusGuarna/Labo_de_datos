import numpy as np


# Parte de numpy
################################################################################
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

