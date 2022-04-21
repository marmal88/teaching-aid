import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

class PreprocessData:
    def __init__(self, path):
        """Read data into preprocess file"""
        self.data = pd.read_csv(path)

    def split(self):
        """Split data into train and holdout set"""
        X = self.data
        Y = X["Class"]
        X.drop(columns=["Class"], axis=1, inplace=True)
        X_train, X_test, y_train, y_test = train_test_split(X, Y, random_state=101, test_size=0.3)

        # Change current X values to np.nan
        X.replace(0, np.nan, inplace=True)

        # Identifying numeric columns for pre-processing
        numeric_col = list(X.select_dtypes(np.number))

        # Create preprocessing step to both Impute and Scale in Series
        numeric_trans = Pipeline([  ("Impute", SimpleImputer(missing_values=np.nan, strategy="median")),
                                    ("Scale", MinMaxScaler(), )])

        # Create column transformer object with preprocessing workflow for use on later pipeline
        CT = ColumnTransformer([("numeric trans", numeric_trans, numeric_col)], remainder="passthrough")

        # Fit and transform X_train data
        X_trans_train = CT.fit_transform(X_train)
        X_trans_train = pd.DataFrame(X_trans_train, columns=X.columns)
        # Only apply the prefitted values to X_test col
        X_trans_test = CT.transform(X_test)
        X_trans_test = pd.DataFrame(X_trans_test, columns=X.columns)

        return X_train, X_test, y_train, y_test, X_trans_train, X_trans_test