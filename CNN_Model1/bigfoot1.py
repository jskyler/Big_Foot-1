#!/usr/bin/env python
# coding: utf-8

# In[9]:


import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Activation, Dense, Flatten, BatchNormalization, Conv2D, MaxPool2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.metrics import categorical_crossentropy
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from sklearn.metrics import confusion_matrix
import itertools
import os
import shutil
import random
import glob
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
get_ipython().run_line_magic('matplotlib', 'inline')


# In[12]:


train_path ='//...Big_Foot/CNN_Model1/train/'
valid_path ='//...Big_Foot/CNN_Model1/valid/'
test_path = '//...Big_Foot/CNN_Model1/test/'


# In[13]:


train_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input)     .flow_from_directory(directory=train_path, target_size=(224,224), classes= ['bigfoot','man'], batch_size=10)
valid_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input)     .flow_from_directory(directory=valid_path, target_size=(224,224), classes= ['bigfoot','man'], batch_size=10)
test_batches = ImageDataGenerator(preprocessing_function=tf.keras.applications.vgg16.preprocess_input)     .flow_from_directory(directory=test_path, target_size=(224,224), classes= ['bigfoot','man'], batch_size=10, shuffle=False)


# In[14]:


assert train_batches.n == 900
assert valid_batches.n == 250
assert test_batches.n == 90
assert train_batches.num_classes == valid_batches.num_classes == test_batches.num_classes == 2


# In[15]:


imgs, labels = next(train_batches)


# In[16]:


def plotImages(images_arr):
    fig, axes = plt.subplots(1,10, figsize=(20,20))
    axes = axes.flatten()
    for img, ax in zip(images_arr, axes):
        ax.imshow(img)
        ax.axis('off')
    plt.tight_layout()
    plt.show()


# In[17]:


plotImages(imgs)
print(labels)


# In[18]:


model = Sequential ([
    Conv2D(filters=32, kernel_size=(3,3), activation='relu', padding='same', input_shape=(224,224,3)), 
    MaxPool2D(pool_size=(2,2), strides=2),
    Conv2D(filters=64, kernel_size=(3,3), activation='relu', padding='same'), 
    MaxPool2D(pool_size=(2,2), strides=2), 
    Flatten(), 
    Dense(units=2, activation='softmax'),
])


# In[19]:


model.summary()


# In[20]:


model.compile(optimizer=Adam(learning_rate=0.0001), loss='categorical_crossentropy', metrics=['accuracy'])


# In[21]:


model.fit(x=train_batches, validation_data=valid_batches, epochs=10, verbose=2)


# In[22]:


test_imgs, test_labels = next(test_batches)
plotImages(test_imgs)
print(test_labels)


# In[23]:


test_batches.classes


# In[24]:


predictions = model.predict(x=test_batches, verbose=0)


# In[25]:


np.round(predictions)


# In[27]:


cm = confusion_matrix(y_true=test_batches.classes, y_pred=np.argmax(predictions, axis=-1))


# In[32]:


def plot_confusion_matrix(cm, classes, 
                         normalize=False, 
                         title='Confusion Matrix',
                         cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks= np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)
    
    if normalize:
        cm = cm.astype('float')/ cm.sum(axis=1)[:, np.newaxis]
        print("Normalized Confusion Matrix")
    else:
        print('Confusion Matrix Without Normalization')
    
    print(cm)
    
    thresh = cm.max() /2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i,j],
                horizontalalignment="center",
                color="white" if cm[i,j] > thresh else "black")
    
    plt.tight_layout()
    plt.ylabel('True Label')
    plt.xlabel('Predicted Label')


# In[33]:


test_batches.class_indices


# In[34]:


cm_plot_labels = ['bigfoot', 'man']
plot_confusion_matrix(cm=cm, classes=cm_plot_labels, title='Confusion Matrix')


# In[ ]:




