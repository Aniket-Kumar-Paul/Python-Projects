# --------------------------------------------------------
# Using below just to not show the logging errors/warnings
from silence_tensorflow import silence_tensorflow
silence_tensorflow()
#---------------------------------------------------------

import tensorflow as tf
import numpy as np
from tensorflow import keras
import matplotlib.pyplot as plt

# Load a pre-defined dataset (70k of 28x28)
fashion_mnist = keras.datasets.fashion_mnist

# Pull out data from dataset
# (60k images,labels for training), (10k images,labels for testing)
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

# Define the neural net structure
# Using a sequential structure
# 1. Input Layer
# 2. Hidden Layers(can be multiple)
# 3. Output layer 
model = keras.Sequential([

    # Input Layer - is a 28x28 image ("Flatten"->flattens the 28x28 into a single 784x1 layer/column)
    # One node = One pixel in the flattened layer
    keras.layers.Flatten(input_shape=(28,28)),

    # Hidden Layer - is 128x1 layer. relu reurns the value, or 0 if -ve(works good enough, much faster)
    # Activation function acts like a filter in the layer
    keras.layers.Dense(units=128, activation=tf.nn.relu),

    # https://keras.io/api/datasets/fashion_mnist/
    # Output Layer - is a 10x1 layer (depending on what piece of clothing it is), return the one having maximum probablity(softmax)
    # Dense -> every node in each column is connected to every other node in other columns
    keras.layers.Dense(units=10, activation=tf.nn.softmax)

])

# Compile the model
model.compile(optimizer=tf.optimizers.Adam(), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Train the model using the training data
# epochs - no. of cycles/passes through the neural network
model.fit(train_images, train_labels, epochs=5)

# Test the model using testing data
test_loss = model.evaluate(test_images, test_labels)

# print(train_labels[5])
plt.imshow(test_images[0], cmap='gray', vmin=0, vmax=255)
print(test_labels[0])
plt.show()

# Make predictions
predictions = model.predict(test_images)
# will print the 10 probabilities in a list for the first image in test_images
# print(prediction[0]) 
print('\nTrained Model answer: ',list(predictions[0]).index(max(predictions[0])))

# print the correct answer
print('\nCorrect answer: ',test_labels[0])