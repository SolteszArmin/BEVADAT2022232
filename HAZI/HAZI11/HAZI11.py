import tensorflow as tf
import numpy as np
from tensorflow.keras import datasets, layers, models

def cifar100_data():
    return tf.keras.datasets.cifar100.load_data()

def cifar100_model() ->tf.keras.Sequential:
    model = models.Sequential()
    model.add(layers.Conv2D(32, (3, 3), activation='relu', input_shape=(32, 32, 3)))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.MaxPooling2D((2, 2)))
    model.add(layers.Conv2D(64, (3, 3), activation='relu'))
    model.add(layers.Flatten())
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(100))
    return model

def model_compile(model:tf.keras.Sequential)->tf.keras.Sequential:
    model.compile(optimizer='adam',
              loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])
    return model

def model_fit(model,epochs, train_images, train_labels) ->tf.keras.Sequential:
    model.fit(train_images, train_labels, epochs=epochs)
    return model

def model_evaluate(model, test_images, test_labels)->(float and float):
    return model.evaluate(test_images,  test_labels)
