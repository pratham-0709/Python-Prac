''' Linear Regresion '''

# Import packages
import numpy as np
import matplotlib.pyplot as plot
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

filepath = r'C:\PGDACC Section\Sem 2\Python\Practicals\lr.csv'

dataset = pd.read_csv(filepath)
x = dataset.iloc[:, :-1].values
print(x)
y = dataset.iloc[:, 1].values
print(y)

# Split into training and testing sets
xTrain, xTest, yTrain, yTest = train_test_split(x, y, test_size = 1/3, random_state = 0)

# Create a linearRegressor and fit it
linearRegressor = LinearRegression()

# Calculate the optimal values of the weights 𝑏₀ and 𝑏₁, using the emilesisting input and output (miles and paid) as the arguments.
linearRegressor.fit(xTrain, yTrain)

# Predict
miles_pred = np.array([600]).reshape(-1,1)
paid_pred = linearRegressor.predict(miles_pred)
print('predicted response:', paid_pred, sep='\n')

# Plot Graph
plot.scatter(xTest, yTest, color = 'red')
plot.plot(xTrain, linearRegressor.predict(xTrain), color = 'blue')
plot.title('Miles vs Money paid (Test set)')
plot.xlabel('Distance in miles')
plot.ylabel('Money in Rs')
plot.show()



