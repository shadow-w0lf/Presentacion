import numpy as np

import tensorflow.keras as kr

dataset = np.loadtxt("posturas.csv", delimiter=";")
lr = 0.05
# X caracterítsticas, Y labels
X = dataset[:,0:16]
Y = dataset[:,16]

print("Forma de X", X.shape)
print("Forma de Y", Y.shape)
print(X[0,:])
print(Y[0])

# creación

model = Sequential()
model.add(Dense(27, input_dim = 16))
model.add(Activation("relu"))
model.add(Dense(18))
model.add(Activation("relu"))
model.add(Dense(3))
model.add(Activation("sigmoid"))

# compilanción
model.compile(loss='mse', optimizer= kr.optimizers.SGD(lr=lr), metrics=['acc'])

# entrenamiento
model.fit(X, Y, epochs=250)

# evaluación
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))