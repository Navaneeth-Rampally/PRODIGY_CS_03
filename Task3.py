import random
import string
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

def create_dataset(num_samples=1000):
    """
    Generates a synthetic dataset of passwords and their corresponding strength labels.

    Args:
        num_samples: The number of samples to generate (default: 1000).

    Returns:
        A tuple containing:
            - passwords: A list of passwords.
            - labels: A list of corresponding strength labels (0: Weak, 1: Strong).
    """

    passwords = []
    labels = []

    # Generate weak passwords
    for _ in range(num_samples // 2):
        password = ''.join(random.choices(string.ascii_lowercase, k=random.randint(4, 7)))
        passwords.append(password)
        labels.append(0)  # Weak

    # Generate strong passwords
    for _ in range(num_samples // 2):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=random.randint(8, 15)))
        passwords.append(password)
        labels.append(1)  # Strong

    return passwords, labels

def preprocess_data(passwords):
    """
    Preprocesses the passwords for machine learning.

    Args:
        passwords: A list of passwords.

    Returns:
        A sparse matrix representing the feature vectors of the passwords, 
        and the fitted CountVectorizer object.
    """

    vectorizer = CountVectorizer(analyzer='char', ngram_range=(1, 3))  # Consider single characters and character pairs
    features = vectorizer.fit_transform(passwords)
    return features, vectorizer

def train_model(X_train, y_train):
    """
    Trains a Logistic Regression model on the given data.

    Args:
        X_train: Training features.
        y_train: Training labels.

    Returns:
        A trained Logistic Regression model.
    """

    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    return model

def evaluate_model(model, X_test, y_test):
    """
    Evaluates the model's performance on the test data.

    Args:
        model: The trained model.
        X_test: Test features.
        y_test: Test labels.

    Returns:
        The accuracy of the model.
    """

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

if __name__ == "__main__":
    # Generate synthetic dataset
    passwords, labels = create_dataset(num_samples=1000)

    # Preprocess data
    X, vectorizer = preprocess_data(passwords)  # Store the vectorizer
    y = np.array(labels)

    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = train_model(X_train, y_train)

    # Evaluate the model
    accuracy = evaluate_model(model, X_test, y_test)
    print(f"Model Accuracy: {accuracy:.2f}")

    # Predict strength of a new password
    while True:
        new_password = input("Enter a password to check (or 'q' to quit): ")
        if new_password.lower() == 'q':
            break
        new_password_features = vectorizer.transform([new_password]) 
        predicted_strength = model.predict(new_password_features)[0]
        if predicted_strength == 1:
            print(f"The entered password is predicted to be Strong.")
        else:
            print(f"The entered password is predicted to be Weak.")