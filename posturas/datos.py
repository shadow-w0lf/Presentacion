import tensorflow as tf
import tensorflow.keras as kr

from sklearn.datasets import make_circles

from IPython.core.display import display, HTML

import numpy as np

dataset = np.loadtxt("posturas.csv", delimiter=",")
# X caracterítsticas, Y labels
X = dataset[:,0:16]
Y = dataset[:,16]
print("Forma de X", X.shape)
print("Forma de Y", Y.shape)
print(X[0,:])
print(Y[0])


lr = 0.01           # learning rate
nn = [16, 32, 18, 15, 4]  # número de neuronas por capa.


# Creamos el objeto que contendrá a nuestra red neuronal, como
# secuencia de capas.
model = kr.Sequential()

# Añadimos la capa 1
l1 = model.add(kr.layers.Dense(nn[1], activation='relu'))

# Añadimos la capa 2
l2 = model.add(kr.layers.Dense(nn[2], activation='relu'))

# Añadimos la capa 3
l2 = model.add(kr.layers.Dense(nn[3], activation='relu'))

# Añadimos la capa 4
l3 = model.add(kr.layers.Dense(nn[4], activation='sigmoid'))

# Compilamos el modelo, definiendo la función de coste y el optimizador.
model.compile(loss='mse', optimizer=kr.optimizers.SGD(lr=0.05), metrics=['acc'])

# Y entrenamos al modelo. Los callbacks 
model.fit(X, Y, epochs=100)