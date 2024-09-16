from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import joblib
import json
import pandas as pd

class SQCTrainer:
    """
    This class is designed to detect SQL injection attempts in SQL queries using machine learning techniques.
    It reads data from a JSON file, processes the data, trains a model, evaluates the model's performance,
    and saves the trained model and vectorizer for future use.
    """
    def __init__(self, json_file):
        """
        Initializes the SQC with data from a JSON file.
        
        Parameters:
            json_file (str): Path to the JSON file containing the dataset with SQL queries and labels.
        
        Attributes:
            self.df (pd.DataFrame): DataFrame containing the SQL queries and their corresponding labels.
            self.vectorizer (TfidfVectorizer): Vectorizer for transforming SQL queries into TF-IDF features.
            self.model (RandomForestClassifier): Machine learning model for classifying SQL queries.
        """
        with open(json_file, 'r') as f:
            data = json.load(f)
        self.df = pd.DataFrame(data)
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def preprocess_data(self):
        """
        Preprocesses the data by transforming SQL queries into TF-IDF features and splitting the data into training and testing sets.
        
        Attributes:
            self.X_vectorized (sparse matrix): TF-IDF features of the SQL queries.
            self.X_train (sparse matrix): Training features.
            self.X_test (sparse matrix): Testing features.
            self.y_train (pd.Series): Training labels.
            self.y_test (pd.Series): Testing labels.
        """
        X = self.df['query']
        y = self.df['label']
        self.X_vectorized = self.vectorizer.fit_transform(X)
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(self.X_vectorized, y, test_size=0.2, random_state=42)

    def train_model(self):
        """
        Trains the RandomForestClassifier model using the preprocessed training data.
        """
        self.model.fit(self.X_train, self.y_train)

    def evaluate_model(self):
        """
        Evaluates the trained model on the test data, printing the accuracy and classification report.
        
        Outputs:
            Accuracy (float): The accuracy of the model on the test data.
            Classification Report (str): Detailed performance metrics including precision, recall, and F1-score.
        """
        y_pred = self.model.predict(self.X_test)
        accuracy = accuracy_score(self.y_test, y_pred)
        report = classification_report(self.y_test, y_pred)
        print(f'Accuracy: {accuracy:.2f}')
        print('Classification Report:')
        print(report)

    def save_model(self, model_filename, vectorizer_filename):
        """
        Saves the trained model and the vectorizer to files for later use.
        
        Parameters:
            model_filename (str): Path to the file where the trained model will be saved.
            vectorizer_filename (str): Path to the file where the vectorizer will be saved.
        
        Outputs:
            Prints a confirmation message indicating where the model and vectorizer have been saved.
        """
        joblib.dump(self.model, model_filename)
        joblib.dump(self.vectorizer, vectorizer_filename)
        print(f"Model and vectorizer saved to '{model_filename}' and '{vectorizer_filename}'.")
