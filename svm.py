import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

filepath = r'C:\PGDACC Section\Sem 2\Python\Practicals\vehicle_csv.csv'


# Read data
vehicle = pd.read_csv(filepath)

# Show top 5 records
vehicle.head()

# features in vehicle dataset
feature_cols = ['COMPACTNESS','CIRCULARITY','DISTANCE_CIRCULARITY','RADIUS_RATIO','PR.AXIS_ASPECT_RATIO',\
				'MAX.LENGTH_ASPECT_RATIO','SCATTER_RATIO','ELONGATEDNESS','PR.AXIS_RECTANGULARITY','MAX.LENGTH_RECTANGULARITY'\
				,'SCALED_VARIANCE_MAJOR','SCALED_VARIANCE_MINOR','SCALED_RADIUS_OF_GYRATION','SKEWNESS_ABOUT_MAJOR',\
				'SKEWNESS_ABOUT_MINOR','KURTOSIS_ABOUT_MAJOR','KURTOSIS_ABOUT_MINOR','HOLLOWS_RATIO']

# Features
features = vehicle[feature_cols] 

# Target variable
label =vehicle.Class
 
# Split dataset in features and target variable
X_train, X_test, y_train, y_test = train_test_split(features, label, test_size = 0.30)


# Build svm model
svclassifier = SVC(kernel='linear')
svclassifier.fit(X_train, y_train)

# Calculate inference
test_label_custom = np.array([111,58,105,183,51,6,265,26,29,174,285,1018,255,85,4,8,181,220])

# Predict label of test instance
y_pred = svclassifier.predict([test_label_custom])

print(y_pred)








