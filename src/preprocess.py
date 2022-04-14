import pandas as pd
from sklearn.model_selection import train_test_split



# Read data into preprocess file
diabetes = pd.read_csv("..\data\Diabetes.csv")

# Split data into train and holdout set
X = diabetes.drop(columns=["Class"])
Y = diabetes["Class"]
X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=101, test_size=0.3)