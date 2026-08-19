import numpy as np
marks = np.array([40, 50, 60, 70, 80]); print(marks.mean())

import pandas as pd
df = pd.DataFrame({"Hours":[1,2,3,4,5],"Marks":[40,50,60,70,80]}); print(df)

import tensorflow as tf
marks = tf.constant([40,50,60,70,80]); print(tf.reduce_mean(marks))

from keras.models import Sequential
model = Sequential(); print("Keras Model Created Successfully") 

from sklearn.linear_model import LinearRegression
X=np.array([1,2,3,4,5]).reshape(-1,1); y=np.array([40,50,60,70,80])
m=LinearRegression().fit(X,y); print("y =",m.coef_[0],"x +",m.intercept_)

x=6
print("Predicted Marks =",m.predict([[x]])[0])

import matplotlib.pyplot as plt
plt.scatter(X,y); plt.plot(X,m.predict(X)); plt.xlabel("Hours"); plt.ylabel("Marks"); plt.show()
