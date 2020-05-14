import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
import pickle


# loading the data
cars = pd.read_csv('D:/Python/Assignments codes/3.2 Multi Linear/Cars.csv')

  # 1. VOL: Cubic feet of cab space
  # 2. HP: Engine horsepower
  # 3. MPG: Average miles per gallon
  # 4. SP: Top speed (mph)
  # 5. WT: Vehicle weight (100 lb) 
  # horsepower, average miles per gallon, cubic feet of cab space, top speed(mph), vehicle weight (1=45kg)

cars.head()

cars1=cars.drop(cars.index[[76,70]],axis=0)
cars1['WT'] = 45*cars1['WT']
x = cars1.iloc[:,[0,2,3,4]].values
x
y = cars1.iloc[:,1].values
y


mlr = LinearRegression()
mlr.fit(x,y)
mlr.predict([[80,100,120,28]])


pickle.dump(mlr, open('model.pkl','wb'))
model = pickle.load(open('model.pkl','rb'))
print(model.predict([[80,100,120,28]]))
