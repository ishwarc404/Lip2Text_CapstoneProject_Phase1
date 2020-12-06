from numpy import loadtxt
from keras.models import Sequential
from keras.layers import Dense
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from sklearn import preprocessing
from sklearn.preprocessing import MinMaxScaler
from sklearn import metrics
from sklearn.metrics import confusion_matrix
import itertools
from keras.utils import to_categorical
import h5py
import pickle


#pre preprocessing - joining all the datasets
df1 = pd.read_csv("./datasets/hellodata.csv")
df2 = pd.read_csv("./datasets/byedata.csv")
results = df1.append(df2)
results = results.drop(columns=["Unnamed: 0"]) #dropping the initial indexing column
results.to_csv("combined.csv")


#preprocessing 
#encoding - one hot
df = pd.read_csv("combined.csv")
df = df.drop(columns=["Unnamed: 0"]) #dropping the initial indexing column
df.iloc[:,90].replace("hello", 0,inplace=True)
df.iloc[:,90].replace("bye", 1,inplace=True)
df = df.astype(float)

data = np.array(df.iloc[:,90])

def encode(data):
    print('Shape of data (BEFORE encode): %s' % str(data.shape))
    encoded = to_categorical(data)
    print('Shape of data (AFTER  encode): %s\n' % str(encoded.shape))
    return encoded

encoded_data = encode(data)
coded = pd.DataFrame(encoded_data)
df = df.drop(columns=["90"])
coded.columns = ['1', '2'] #renaming it
df["90"] = coded["1"]
df["91"] = coded["2"]


df = df.sample(frac=1) 

df.to_csv("TOBETRAINED.csv")


names = df.columns[0:90]
scaler = MinMaxScaler() 
scalerfile = 'scaler.sav'
pickle.dump(scaler, open(scalerfile, 'wb'))
scaled_df = scaler.fit_transform(df.iloc[:,0:90]) 
scaled_df = pd.DataFrame(scaled_df, columns=names)



x=scaled_df.iloc[0:370,0:90] #.values.transpose()
y=df.iloc[0:370,90:93] #.values.transpose()

 

model = Sequential()

#2 hidden layers with the first input of 90
#one last hidden layer
model.add(Dense(12, input_dim=90, activation='relu')) #input_dim is the number of cols in the inputs
model.add(Dense(8, activation='relu'))
model.add(Dense(2, activation='softmax'))

# compile the keras model
model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

#fit the keras model on the dataset
model.fit(x, y, epochs=30, batch_size=2)

model.save('my_model.h5')

