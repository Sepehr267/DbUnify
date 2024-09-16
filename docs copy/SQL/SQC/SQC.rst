SQC
=================

This document provides examples demonstrating the use of the `SQC` class for predicting the suspiciousness of SQL queries using a pre-trained model and vectorizer.

1. **Initialize the SQC Class**

   Create an instance of the `SQC` class by providing the paths to the saved model and vectorizer files.

   .. code-block:: python

      from DbUnify.SQL.SQC import SQC

      sqc = SQC(
          model_filename='model.pkl',
          vectorizer_filename='vectorizer.pkl'
      )

2. **Predict Suspiciousness for a Single Query**

   Use the `predict` method to determine if a single SQL query is suspicious.

   .. code-block:: python

      query = 'SELECT * FROM users WHERE username = \'admin\''
      result = sqc.predict(query)
      print(f'The query is {result}.')

   Output (example):

   .. code-block::

      The query is Suspicious.

3. **Predict Suspiciousness for Multiple Queries**

   Use the `predict_multiple` method to evaluate a list of SQL queries.

   .. code-block:: python

      queries = [
          'SELECT * FROM orders WHERE order_id = 123',
          'SELECT * FROM users WHERE user_id = 1 OR 1=1'
      ]
      results = sqc.predict_multiple(queries)
      for query, result in results:
          print(f'The query "{query}" is {result}.')

   Output (example):

   .. code-block::

      The query "SELECT * FROM orders WHERE order_id = 123" is Not Suspicious.
      The query "SELECT * FROM users WHERE user_id = 1 OR 1=1" is Suspicious.
