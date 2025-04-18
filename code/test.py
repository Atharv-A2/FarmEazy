# -*- coding: utf-8 -*-

import csv
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

dataset=pd.read_csv('code/code/regressiondb.csv')
locbased = pd.read_csv('code/metacrops.csv')

crop_Y_pred=[]
crop_name=[]

with open('code/code/metacrops11.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    #metacrops.writelines("Crop,Production\n")
    #os.remove('final.txt')
    cnt = 0
    for row in reader:
        crop=row[0]
# Importing the dataset
        metadata=dataset.loc[dataset['Crop'] == crop]
        X = metadata.iloc[:, :-2].values
        Y = metadata.iloc[:, 4].values

        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size = 0.1, random_state = 0)

        regressor = LinearRegression()

        regressor.fit(X_train, Y_train)

        abs = locbased.loc[[0]].values
        abs = abs[:, 1:4]
        Y_pred = regressor.predict(abs)
        # print("ypred - ",Y_pred)

        if Y_pred>0:
                   crop_Y_pred.append(round(Y_pred[0],3))
                   crop_name.append(crop)
# print("cyp - ",crop_Y_pred)
# print("name - ",crop_name)

def quicksort(crop_name,crop_Y_pred,start, end):
    if start < end:
        # partition the list
        pivot = partition(crop_name,crop_Y_pred, start, end)
        # sort both halves
        quicksort(crop_name,crop_Y_pred, start, pivot-1)
        quicksort(crop_name,crop_Y_pred, pivot+1, end)
    return crop_name

#partition function
def partition(crop_name,crop_Y_pred, start, end):
    pivot = crop_Y_pred[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and crop_Y_pred[left] >= pivot:
            left = left + 1
        while crop_Y_pred[right] <= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            # swap places Y_pred
            temp=crop_Y_pred[left]
            crop_Y_pred[left]=crop_Y_pred[right]
            crop_Y_pred[right]=temp
            
            # swap places Y_crop
            temp1=crop_name[left]
            crop_name[left]=crop_name[right]
            crop_name[right]=temp1
            
    # swap start with myList[right]
    temp=crop_Y_pred[start]
    crop_Y_pred[start]=crop_Y_pred[right]
    crop_Y_pred[right]=temp
    
    # swap start with myList[right] for crop 
    temp1=crop_name[start]
    crop_name[start]=crop_name[right]
    crop_name[right]=temp1
        
    return right

sorted_crops = quicksort(crop_name, crop_Y_pred, 0, len(crop_Y_pred)-1)
print(sorted_crops)       
        # print("xtrain - ",Y, "===========",cnt)
        # cnt += 1
        # print("ytrain - ",Y_train)



"""Encoding categorical data

Encoding the Independent Variable
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

labelencoder_X = LabelEncoder()
X[:, 3] = labelencoder_X.fit_transform(X[:, 3])
onehotencoder = OneHotEncoder(categorical_features = [3]) ##why str needs to be at this loc only and not first?
X = onehotencoder.fit_transform(X).toarray()

dummy var trap removal
X=X[:,1:]  ##no need to do this manually lib does it by default..written just for info.
"""


#regressor = LinearRegression()
#regressor.fit(X, Y)


#predecting test set results


# print("\n\n")

