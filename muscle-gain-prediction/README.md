# Muscle Gain Prediction Project

This project aims to build and deploy a prediction algorithm that estimates users' future muscle gains based on their current workout schedules. The model leverages historical workout data to provide personalized insights and recommendations.

## Project Structure

The project is organized into the following directories and files:

- `src/`: Contains the source code for data preprocessing, model training, and prediction.
  - `data_preprocessing.py`: Functions for cleaning and preparing workout schedule data.
  - `model_training.py`: Defines and trains the prediction model.
  - `prediction.py`: Logic for making predictions using the trained model.
  - `utils/`: A module for utility functions.
  
- `data/`: Stores datasets.
  - `raw/`: Contains raw input data (e.g., user workout logs).
  - `processed/`: Contains cleaned and processed datasets ready for training.

- `notebooks/`: Jupyter notebooks for data exploration and model evaluation.
  - `data_exploration.ipynb`: Exploratory data analysis (EDA) notebook.
  - `model_evaluation.ipynb`: Model evaluation notebook.

- `requirements.txt`: Lists Python dependencies required for the project.

- `Dockerfile`: Instructions for building a Docker image for the project.

- `.dockerignore`: Specifies files to ignore when building the Docker image.

- `.gitignore`: Lists files to ignore in Git.

- `README.md`: Documentation for the project.

## Setup Instructions

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd muscle-gain-prediction
   ```

2. **Install Dependencies**: 
   Use the following command to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Data Preparation**: 
   Place your raw workout data in the `data/raw/` directory. Use the `data_preprocessing.py` script to clean and prepare the data.

4. **Model Training**: 
   Run the `model_training.py` script to train the prediction model on the processed data.

5. **Making Predictions**: 
   Use the `prediction.py` script to load the trained model and make predictions based on new workout schedules.

6. **Jupyter Notebooks**: 
   Open the notebooks in the `notebooks/` directory for data exploration and model evaluation.

## Usage Examples

- To preprocess data:
  ```python
  from src.data_preprocessing import preprocess_data
  preprocess_data('data/raw/workout_data.csv')
  ```

- To train the model:
  ```python
  from src.model_training import train_model
  train_model('data/processed/cleaned_data.csv')
  ```

- To make predictions:
  ```python
  from src.prediction import make_prediction
  results = make_prediction('data/processed/new_workout_schedule.csv')
  ```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.