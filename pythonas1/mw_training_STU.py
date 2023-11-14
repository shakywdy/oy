

# '''
# Author: shaky shaky
# Date: 2023-11-07 17:13:52
# LastEditors: shaky shaky
# LastEditTime: 2023-11-07 20:03:32
# FilePath: \undefinedc:\Users\46058\Desktop\python as1\mw_training_STU.py
# Description: 

# Copyright (c) 2023 by ${git_name_email}, All Rights Reserved. 
# '''
# -*- coding: utf-8 -*-
# """
# Student ID:s235458		
# Name:Wangdongyang
# """


# save the final model to file


from keras.applications.vgg16 import VGG16
from keras.models import Model
from keras.layers import Dense, Flatten
from keras.optimizers import SGD
from keras.preprocessing.image import ImageDataGenerator


# define cnn model
def define_model():
	# load model
	model = VGG16(include_top=False, input_shape=(224, 224, 3))
	# mark loaded layers as not trainable
	for layer in model.layers:
		layer.trainable = False
	# add new classifier layers
	flat1 = Flatten()(model.layers[-1].output)
	class1 = Dense(128, activation='relu', kernel_initializer='he_uniform')(flat1)
	output = Dense(1, activation='sigmoid')(class1)
	# define new model
	model = Model(inputs=model.inputs, outputs=output)
	# compile model 
	opt = SGD(lr=0.001, momentum=0.9)
	model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])
	return model

# Training.

def train():
    # define model
	model = define_model()
	# create data generator
	datagen = ImageDataGenerator(featurewise_center=True)
	# specify imagenet mean values for centering
	datagen.mean = [123.68, 116.779, 103.939]
	# prepare training data
    #
	train_data = datagen.flow_from_directory('training',    # <=== MODIFY TO YOUR MODEL THAT CONTAINS THE TRAINING DATA FOLDERS****    
		class_mode='binary', batch_size=32, target_size=(224, 224))
	# fit model
	model.fit_generator(train_data, steps_per_epoch=len(train_data), epochs=3, verbose=1)  #Increase epoch for better training, if necessary
	# save model
    #    
	model.save('s235458.h8')    # <=== MODIFY TO YOUR MODEL FILE NAME **** #

# entry point, run the test harness
train()
