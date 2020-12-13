from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, MaxPooling2D, Dropout, Activation, Cropping2D
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
import numpy as np

X_train = np.load('/opt/center_1/X_center.npy')
X_train = np.append(X_train, np.load('/opt/center_2/X_center.npy'), 0)
#X_train = np.append(X_train, np.load('/opt/bridge/X_center.npy'), 0)
X_train = np.append(X_train, np.load('/opt/recovery_1/X_center.npy'), 0)
y_train = np.load('/opt/center_1/y.npy')
y_train = np.append(y_train, np.load('/opt/center_2/y.npy'), 0)
#y_train = np.append(y_train, np.load('/opt/bridge/y.npy'), 0)
y_train = np.append(y_train, np.load('/opt/recovery_1/y.npy'), 0)

# augmenting data by fliping
X_train = np.append(X_train, np.flip(X_train,2), 0)
y_train = np.append(y_train, -y_train, 0)

model = Sequential()

# preprocessing data
model.add(Cropping2D(cropping=((70,25), (0,0)), input_shape=(160,320,3)))
model.add(Lambda(lambda x: x / 255.0 - 0.5))

model.add(Convolution2D(6,5,5, activation='relu'))
model.add(MaxPooling2D())
#model.add(Dropout(.5))

model.add(Convolution2D(6,5,5, activation='relu'))
model.add(MaxPooling2D())
#model.add(Dropout(.5))

model.add(Flatten())
model.add(Dense(120))
model.add(Dense(84))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
model.fit(X_train, y_train, validation_split=0.2, shuffle=True, nb_epoch=2)

model.save('model.h5')
