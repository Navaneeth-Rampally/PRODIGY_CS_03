# PRODIGY_CS_03
Password complexity checker

Task3: "Password Complexity Checker"

This Python code implements a machine learning model to assess the strength of passwords. It generates a synthetic dataset of passwords with varying strengths, trains a Logistic Regression model to classify them, and allows users to interactively check the strength of new passwords.

Key Components:

Data Generation (create_dataset function):

Creates a balanced dataset of 1000 passwords (default) with equal proportions of weak and strong passwords.
Weak passwords: 4-7 characters in length, consisting only of lowercase letters.
Strong passwords: 8-15 characters in length, containing a combination of uppercase letters, lowercase letters, digits, and punctuation symbols.
Data Preprocessing (preprocess_data function):

Utilizes CountVectorizer from scikit-learn to convert passwords into numerical feature vectors.
Considers both single characters and character pairs (bigrams) for richer feature representation.
Returns the feature vectors (X) and the fitted CountVectorizer object (vectorizer).
Model Training (train_model function):

Employs a Logistic Regression model for classification.
Trains the model on the preprocessed training data (X_train, y_train).
Model Evaluation (evaluate_model function):

Evaluates the trained model's performance on the test data (X_test, y_test).
Calculates and prints the model's accuracy.
Interactive Password Strength Prediction:

Prompts the user to enter a password or 'q' to quit.
Transforms the new password into a feature vector using the previously fitted vectorizer.
Predicts the strength (weak or strong) using the trained model.
Provides feedback to the user about the predicted strength.
Running the Code:

Save the code as a Python file (e.g., password_checker.py).
Install the required libraries: pip install scikit-learn
Open a terminal or command prompt and navigate to the directory where you saved the file.
Run the script: python password_checker.py
Example Usage:

Model Accuracy: 0.97  # This value may vary depending on the random data generation
Enter a password to check (or 'q' to quit): MySecretPassword123!
The entered password is predicted to be Strong.
Enter another password (or 'q' to quit): weakpassword
The entered password is predicted to be Weak.
Enter 'q' to quit.
