import pandas as pd
from sklearn.tree import DecisionTreeClassifier 
from sklearn.model_selection import train_test_split 
from sklearn import metrics
import numpy as np
from sklearn import *
from sklearn import tree
import matplotlib.pyplot as plt


# Features in vehicle dataset
col_names = ['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age','label']

filepath = r'E:/Swapnil_Thakare/ESDS-Academia/Sandip/Python-ML/practicals/GroupB/Decision Tree/diabetes.csv'
graph_filepath = r'E:/Swapnil_Thakare/ESDS-Academia/Sandip/Python-ML/practicals/GroupB/Decision Tree/diabetes.jpg'

# Read data
pima = pd.read_csv(filepath, header=None, names=col_names)

# Show top 5 records
pima.head()

# Split dataset in features and target variable
feature_cols =['pregnant','glucose','bp','skin','insulin','bmi','pedigree','age']

# Features
features = pima[feature_cols] 

# Target variable
label = pima.label 

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size=0.3, random_state=1) 


# Create Decision Tree classifer model
clf = DecisionTreeClassifier()

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

# test instance
test_label_custom = np.array([10,101,76,48,180,32.9,0.171,63])

# Predict the response for test instance
y_pred = clf.predict([test_label_custom])

print(y_pred)

tree.plot_tree(clf, filled=True)

fig = plt.figure(figsize=(25,20))

#fig.savefig(graph_filepath)

