from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from data_loading import load_and_process_data

def train_model():
    # Load and process the data
    X_train, X_test, y_train, y_test = load_and_process_data()
    
    # Initialize a RandomForestClassifier
    model = RandomForestClassifier(random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions on the test set
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Test Accuracy: {accuracy:.4f}")
    
    return model, accuracy
