# Import necessary libraries
import tensorflow as tf
import cv2
import numpy as np
import os

# Define model architecture
model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(32, (3,3), activation='relu', input_shape=(100,100,3)),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Conv2D(64, (3,3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2,2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(1, activation='sigmoid')
])

# Compile model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

# Load dataset
dataset_path = 'path/to/dataset'
X_train = []
y_train = []
for file in os.listdir(dataset_path):
    img = cv2.imread(os.path.join(dataset_path, file))
    X_train.append(cv2.resize(img, (100, 100))) # Resize image to (100, 100)
    y_train.append(1 if 'moving' in file else 0)
X_train = np.array(X_train)
y_train = np.array(y_train)

# Train model
model.fit(X_train, y_train, epochs=10, batch_size=32)

# Save model
model.save('moving_object_detection_model.h5')
