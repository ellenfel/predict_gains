import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_data(file_path):
    """Load workout schedule data from a CSV file."""
    data = pd.read_csv(file_path)
    return data

def handle_missing_values(data):
    """Handle missing values in the dataset."""
    # Example: Fill missing values with the mean of the column
    return data.fillna(data.mean())

def normalize_data(data):
    """Normalize the dataset using StandardScaler."""
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data)
    return pd.DataFrame(scaled_data, columns=data.columns)

def split_data(data, target_column, test_size=0.2, random_state=42):
    """Split the dataset into training and testing sets."""
    X = data.drop(columns=[target_column])
    y = data[target_column]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    return X_train, X_test, y_train, y_test

def preprocess_data(file_path, target_column):
    """Load, clean, normalize, and split the data."""
    data = load_data(file_path)
    data = handle_missing_values(data)
    data = normalize_data(data)
    X_train, X_test, y_train, y_test = split_data(data, target_column)
    return X_train, X_test, y_train, y_test