import joblib

class SQC:
    def __init__(self, model_filename: str, vectorizer_filename: str) -> None:
        """
        Initializes the SQC class by loading the trained model and vectorizer from the provided filenames.

        :param model_filename: Path to the saved model file (e.g., 'model.pkl').
        :param vectorizer_filename: Path to the saved vectorizer file (e.g., 'vectorizer.pkl').
        """
        self.model = joblib.load(model_filename)
        self.vectorizer = joblib.load(vectorizer_filename)

    def predict(self, query: str) -> str:
        """
        Predicts whether a given SQL query is suspicious or not by using the loaded model.

        :param query: The SQL query string to be evaluated.
        :return: A string 'Suspicious' if the query is flagged as suspicious, otherwise 'Not Suspicious'.
        """
        query_vectorized = self.vectorizer.transform([query])
        prediction = self.model.predict(query_vectorized)
        return 'Suspicious' if prediction[0] == 1 else 'Not Suspicious'

    def predict_multiple(self, queries : str) -> list:
        """
        Predicts the suspiciousness for multiple SQL queries.

        :param queries: A list of SQL query strings to be evaluated.
        :return: A list of tuples, each containing the query and its prediction ('Suspicious' or 'Not Suspicious').
        """
        results = []
        for query in queries:
            result = self.predict(query)
            results.append((query, result))
        return results