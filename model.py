from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, MaxPooling2D, Dropout, Activation
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
import numpy as np

X_train = np.load('/opt/1/X_center.npy')
y_train = np.load('/opt/1/y.npy')

model = Sequential()
model.add(Lambda(lambda x: x / 255.0 - 0.5, input_shape=(160,320,3)))

model.add(Convolution2D(6,5,5, activation='relu'))
model.add(MaxPooling2D())
# model.add(Dropout(.5))

model.add(Convolution2D(6,5,5, activation='relu'))
model.add(MaxPooling2D())
# model.add(Dropout(.5))

model.add(Flatten())
model.add(Dense(120))
model.add(Dense(84))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=5)

model.save('model.h5')
