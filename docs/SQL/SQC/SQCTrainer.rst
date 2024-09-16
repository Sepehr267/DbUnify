SQCTrainer Example
==================

This document provides examples demonstrating the use of the `SQCTrainer` class for detecting SQL injection attempts in SQL queries using machine learning techniques.

1. **Initialize the SQCTrainer Class**

   Create an instance of the `SQCTrainer` class by providing the path to a JSON file containing the dataset.

   .. code-block:: python

      from DbUnify.SQL.SQC import SQCTrainer

      trainer = SQCTrainer(json_file='dataset.json') # Generate From DatasetGenerator

2. **Preprocess the Data**

   Transform SQL queries into TF-IDF features and split the data into training and testing sets.

   .. code-block:: python

      trainer.preprocess_data()

3. **Train the Model**

   Train the `RandomForestClassifier` model using the preprocessed training data.

   .. code-block:: python

      trainer.train_model()

4. **Evaluate the Model**

   Evaluate the trained model on the test data, and print the accuracy and classification report.

   .. code-block:: python

      trainer.evaluate_model()

   Output (example):

   .. code-block::

      Accuracy: 0.95
      Classification Report:
                   precision    recall  f1-score   support

                0       0.96      0.94      0.95       1600
                1       0.94      0.96      0.95       1600

         accuracy                           0.95       3200
        macro avg       0.95      0.95      0.95       3200
     weighted avg       0.95      0.95      0.95       3200

5. **Save the Model and Vectorizer**

   Save the trained model and the vectorizer to files for later use.

   .. code-block:: python

      trainer.save_model(model_filename='model.joblib', vectorizer_filename='vectorizer.joblib')

   Output:

   .. code-block::

      Model and vectorizer saved to 'model.joblib' and 'vectorizer.joblib'.
