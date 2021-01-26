from keras.models import Sequential
from keras.layers import Flatten, Dense, Lambda, MaxPooling2D, Dropout, Activation, Cropping2D, GaussianNoise
from keras.layers.convolutional import Convolution2D
from keras.layers.pooling import MaxPooling2D
import matplotlib.pyplot as plt
import numpy as np

X_train = np.load('/opt/sample_data/X_center.npy')
X_train = np.append(X_train, np.load('/opt/center_1/X_center.npy'), 0)
X_train = np.append(X_train, np.load('/opt/center_2/X_center.npy'), 0)
#X_train = np.append(X_train, np.load('/opt/bridge/X_center.npy'), 0)
X_train = np.append(X_train, np.load('/opt/recovery_1/X_center.npy'), 0)
X_train = np.append(X_train, np.load('/opt/reverse_1/X_center.npy'), 0)
#X_train = np.append(X_train, np.load('/opt/no_border_1/X_center.npy'), 0)

y_train = np.load('/opt/sample_data/y.npy')
y_train = np.append(y_train, np.load('/opt/center_1/y.npy'), 0)
y_train = np.append(y_train, np.load('/opt/center_2/y.npy'), 0)
#y_train = np.append(y_train, np.load('/opt/bridge/y.npy'), 0)
y_train = np.append(y_train, np.load('/opt/recovery_1/y.npy'), 0)
y_train = np.append(y_train, np.load('/opt/reverse_1/y.npy'), 0)
#y_train = np.append(y_train, np.load('/opt/no_border_1/y.npy'), 0)

# augmenting data by fliping
X_train = np.append(X_train, np.flip(X_train,2), 0)
y_train = np.append(y_train, -y_train, 0)

model = Sequential()

# preprocessing data
model.add(Cropping2D(cropping=((70,25), (0,0)), input_shape=(160,320,3)))
model.add(Lambda(lambda x: x / 255.0 - 0.5))
model.add(GaussianNoise(.005))

#model.add(Convolution2D(6,5,5, activation='relu'))
#model.add(MaxPooling2D())
#model.add(Dropout(.5))

#model.add(Convolution2D(6,5,5, activation='relu'))
#model.add(MaxPooling2D())
#model.add(Dropout(.5))

model.add(Convolution2D(25,5,5, subsample=(2,2), activation='relu'))
model.add(Convolution2D(36,5,5, subsample=(2,2), activation='relu'))
model.add(Convolution2D(48,5,5, subsample=(2,2), activation='relu'))
model.add(Convolution2D(64,3,3, activation='relu'))
model.add(Convolution2D(64,3,3, activation='relu'))

model.add(Dropout(.25))
model.add(Flatten())
model.add(Dense(100))
model.add(Dense(50))
model.add(Dense(10))
model.add(Dense(1))

model.compile(loss='mse', optimizer='adam')
history_object = model.fit(X_train, y_train, validation_split=0.2, shuffle=True, epochs=3)

model.save('model.h5')

### print the keys contained in the history object
print(history_object.history.keys())

### plot the training and validation loss for each epoch
plt.plot(history_object.history['loss'])
plt.plot(history_object.history['val_loss'])
plt.title('model mean squared error loss')
plt.ylabel('mean squared error loss')
plt.xlabel('epoch')
plt.legend(['training set', 'validation set'], loc='upper right')
plt.savefig('loss.jpg')