Self Learning SQC
=======================

This document provides examples demonstrating the use of the `SelfLearningSQC` class for retraining and evaluating a SQL query classification model with new data.

1. **Initialize the SelfLearningSQC Class**

   Create an instance of the `SelfLearningSQC` class by providing the paths to the saved model, vectorizer, and old data files.

   .. code-block:: python

      from DbUnify.SQL.SQC import SelfLearningSQC

      self_learning_sqc = SelfLearningSQC(
          model_filename='model.pkl',  # Generate From SQCTrainer
          vectorizer_filename='vectorizer.pkl',
          old_data_filename='old_data.json'
      )

2. **Retrain the Model with New Data**

   Retrain the model with new SQL query data and save the updated model and vectorizer.

   .. code-block:: python

      new_data = [
          {'query': 'SELECT * FROM users WHERE username = \'admin\'', 'label': 1},
          {'query': 'SELECT * FROM products WHERE price > 100', 'label': 0}
      ] # You can Generate use DatasetGenerator

      self_learning_sqc.retrain_model(
          new_data=new_data,
          model_filename='retrained_model.pkl',
          vectorizer_filename='retrained_vectorizer.pkl'
      )

   Output:

   .. code-block::

      Model and vectorizer updated and saved to 'retrained_model.pkl' and 'retrained_vectorizer.pkl'.

3. **Evaluate the Retrained Model**

   Evaluate the performance of the retrained model using a separate test dataset.

   .. code-block:: python

      test_data = [
          {'query': 'SELECT * FROM orders WHERE order_id = 123', 'label': 0},
          {'query': 'SELECT * FROM users WHERE user_id = 1 OR 1=1', 'label': 1}
      ]

      self_learning_sqc.evaluate_model(test_data=test_data)

   Output (example):

   .. code-block::

      Accuracy after retraining: 0.90
      Classification Report after retraining:
                   precision    recall  f1-score   support

                0       0.92      0.88      0.90         50
                1       0.88      0.92      0.90         50

         accuracy                           0.90        100
        macro avg       0.90      0.90      0.90        100
     weighted avg       0.90      0.90      0.90        100
