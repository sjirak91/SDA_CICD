from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import pandas as pd

def load_and_process_data():
    # Load the iris dataset
    iris = load_iris()
    X, y = iris.data, iris.target
    
    # Convert to pandas DataFrame
    X = pd.DataFrame(X, columns=iris.feature_names)
    y = pd.Series(y, name='target')

    # Split the data into training and test sets (80% train, 20% test)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Standardize the features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    return X_train_scaled, X_test_scaled, y_train, y_test
