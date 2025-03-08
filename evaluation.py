from sklearn.metrics import classification_report, confusion_matrix
from model_training import train_model, load_and_process_data


def evaluate_model():
    model, accuracy = train_model()

    # Load the test set
    _, X_test, _, y_test = load_and_process_data()

    # Make predictions
    y_pred = model.predict(X_test)

    # Generate classification report
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

    # Generate confusion matrix
    print("Confusion Matrix:")
    print(confusion_matrix(y_test, y_pred))


if __name__ == "__main__":
    evaluate_model()
