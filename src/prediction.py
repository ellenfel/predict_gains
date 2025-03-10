from sklearn.externals import joblib
import pandas as pd
from data_preprocessing import preprocess_input_data

def load_model(model_path):
    """Load the trained model from the specified path."""
    model = joblib.load(model_path)
    return model

def make_prediction(model, input_data):
    """Make predictions using the trained model."""
    processed_data = preprocess_input_data(input_data)
    predictions = model.predict(processed_data)
    return predictions

if __name__ == "__main__":
    # Example usage
    model_path = 'path/to/your/trained/model.pkl'  # Update with the actual model path
    input_data = pd.DataFrame({
        'exercise': ['squat', 'bench press'],
        'sets': [3, 4],
        'reps': [10, 8],
        'weight': [100, 80]
    })  # Replace with actual user input data

    model = load_model(model_path)
    predictions = make_prediction(model, input_data)
    print("Predicted muscle gains:", predictions)