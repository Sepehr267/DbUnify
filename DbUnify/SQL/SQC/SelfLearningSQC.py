from .SQC import SQC
from sklearn.metrics import classification_report, accuracy_score
import joblib
import pandas as pd

class SelfLearningSQC(SQC):
    def __init__(self, model_filename: str, vectorizer_filename: str, old_data_filename: str) -> None:
        """
        Initializes the SelfLearningSQC class by loading the trained model, vectorizer, and old data.

        :param model_filename: Path to the saved model file (e.g., 'model.pkl').
        :param vectorizer_filename: Path to the saved vectorizer file (e.g., 'vectorizer.pkl').
        :param old_data_filename: Path to the file where the old data is saved.
        """
        super().__init__(model_filename, vectorizer_filename)
        self.old_data = pd.read_json(old_data_filename)

    def retrain_model(self, new_data: list, model_filename: str, vectorizer_filename: str):
        """
        Retrains the model with new data and saves the updated model and vectorizer.

        :param new_data: List of dictionaries containing new SQL queries and their labels.
        :param model_filename: Path to the file where the retrained model will be saved.
        :param vectorizer_filename: Path to the file where the retrained vectorizer will be saved.
        """
        new_df = pd.DataFrame(new_data)
        
        X_new = new_df['query']
        y_new = new_df['label']
        
        X_new_vectorized = self.vectorizer.transform(X_new)
        
        X_old = self.old_data['query']
        y_old = self.old_data['label']
        
        X_old_vectorized = self.vectorizer.transform(X_old)
        
        X_combined = pd.concat([pd.DataFrame(X_old_vectorized.toarray()), pd.DataFrame(X_new_vectorized.toarray())], ignore_index=True)
        y_combined = pd.concat([y_old, y_new], ignore_index=True)
        
        self.model.fit(X_combined, y_combined)
        
        joblib.dump(self.model, model_filename)
        joblib.dump(self.vectorizer, vectorizer_filename)
        print(f"Model and vectorizer updated and saved to '{model_filename}' and '{vectorizer_filename}'.")

    def evaluate_model(self, test_data: list):
        """
        Evaluates the retrained model using a separate test dataset.

        :param test_data: List of dictionaries containing SQL queries and their labels for testing.
        """
        test_df = pd.DataFrame(test_data)
        
        X_test = test_df['query']
        y_test = test_df['label']
        
        X_test_vectorized = self.vectorizer.transform(X_test)
        
        y_pred = self.model.predict(X_test_vectorized)
        
        accuracy = accuracy_score(y_test, y_pred)
        report = classification_report(y_test, y_pred)
        print(f'Accuracy after retraining: {accuracy:.2f}')
        print('Classification Report after retraining:')
        print(report)

