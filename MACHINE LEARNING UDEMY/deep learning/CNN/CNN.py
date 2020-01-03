# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 17:07:00 2019

@author: DELL
"""
# building the cnn

# importing the keras
from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense

# initializing the cnn
classifier = Sequential()

# step 1 - Convulation
classifier.add(Convolution2D(32,3,3,activation = 'relu', input_shape = (64,64,3)))


#MAX POOLING
classifier.add(MaxPooling2D(pool_size=(2,2)))


# second convulation layer
classifier.add(Convolution2D(32,3,3,activation = 'relu'))
classifier.add(MaxPooling2D(pool_size=(2,2)))

# flattening
classifier.add(Flatten())

#full connection connecting the nerural network

classifier.add(Dense(output_dim= 128, activation = 'relu'))
classifier.add(Dense(output_dim= 1 ,activation='sigmoid'))

classifier.compile(optimizer='adam', loss = 'binary_crossentropy', metrics=['accuracy'])

## fitting the cnn to images
from keras.preprocessing.image import ImageDataGenerator

train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1./255)

training_set = train_datagen.flow_from_directory(
        'dataset_dogs_vs_cats/train',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')

test_set = test_datagen.flow_from_directory(
        'dataset_dogs_vs_cats/test',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')/

classifier.fit_generator(
        training_set,
        steps_per_epoch=1920,
        epochs=5,
        validation_data=test_set,
        validation_steps=1110)