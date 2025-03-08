from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from data_loading import load_and_process_data

def tune_hyperparameters():
    # Load and process the data
    X_train, X_test, y_train, y_test = load_and_process_data()

    # Initialize a RandomForestClassifier
    model = RandomForestClassifier(random_state=42)
    
    # Define hyperparameters and their possible values
    param_grid = {
        'n_estimators': [50, 100, 200],
        'max_depth': [None, 10, 20, 30],
        'min_samples_split': [2, 5, 10]
    }
    
    # Initialize GridSearchCV
    grid_search = GridSearchCV(estimator=model, param_grid=param_grid, cv=5, verbose=1, n_jobs=-1)
    
    # Perform grid search
    grid_search.fit(X_train, y_train)
    
    # Print the best parameters
    print(f"Best Parameters: {grid_search.best_params_}")
    
    # Return the best model
    return grid_search.best_estimator_
