"""
Student Performance Prediction - Machine Learning Model Training Script
=====================================================================
Run this script standalone to train and save the ML model.
Usage: python predictor/ml_model.py
"""

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler
import joblib
import os


def generate_synthetic_data(n_samples=1000):
    """
    Generate synthetic student performance data for training.
    Features:
        - study_hours: Daily study hours (0-12)
        - attendance: Attendance percentage (0-100)
        - previous_score: Previous exam score (0-100)
        - sleep_hours: Daily sleep hours (0-12)
        - sample_papers: Number of sample papers practiced (0-20)
    Target:
        - performance_score: Final exam score (0-100)
    """
    np.random.seed(42)

    study_hours = np.random.uniform(0, 12, n_samples)
    attendance = np.random.uniform(30, 100, n_samples)
    previous_score = np.random.uniform(20, 100, n_samples)
    sleep_hours = np.random.uniform(4, 11, n_samples)
    sample_papers = np.random.randint(0, 20, n_samples)

    # Generate target with realistic relationships + noise
    performance_score = (
        study_hours * 3.5 +
        attendance * 0.3 +
        previous_score * 0.25 +
        sleep_hours * 1.5 +
        sample_papers * 2.0 +
        np.random.normal(0, 5, n_samples)
    )

    # Clamp to valid range
    performance_score = np.clip(performance_score, 0, 100)

    data = pd.DataFrame({
        'study_hours': study_hours,
        'attendance': attendance,
        'previous_score': previous_score,
        'sleep_hours': sleep_hours,
        'sample_papers': sample_papers,
        'performance_score': performance_score
    })

    return data


def train_and_save_model():
    """Train multiple ML models and save the best one."""
    print("Generating training data...")
    data = generate_synthetic_data(n_samples=2000)

    # Features and target
    X = data[['study_hours', 'attendance', 'previous_score', 'sleep_hours', 'sample_papers']]
    y = data['performance_score']

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    print(f"Training samples: {len(X_train)}")
    print(f"Testing samples: {len(X_test)}")

    # Scale features
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    # Train models
    models = {
        'Linear Regression': LinearRegression(),
        'Random Forest': RandomForestRegressor(n_estimators=100, random_state=42),
        'Gradient Boosting': GradientBoostingRegressor(n_estimators=100, random_state=42)
    }

    best_model = None
    best_r2 = -float('inf')
    best_name = ''

    print("\nModel Performance:")
    print("-" * 50)

    for name, model in models.items():
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)

        mse = mean_squared_error(y_test, y_pred)
        r2 = r2_score(y_test, y_pred)
        rmse = np.sqrt(mse)

        print(f"{name}:")
        print(f"  R2 Score: {r2:.4f}")
        print(f"  RMSE: {rmse:.4f}")

        if r2 > best_r2:
            best_r2 = r2
            best_model = model
            best_name = name

    print(f"\nBest Model: {best_name} (R2={best_r2:.4f})")

    # Save model and scaler
    model_dir = os.path.join(os.path.dirname(__file__), 'model')
    os.makedirs(model_dir, exist_ok=True)

    model_path = os.path.join(model_dir, 'student_model.pkl')
    scaler_path = os.path.join(model_dir, 'scaler.pkl')

    joblib.dump(best_model, model_path)
    joblib.dump(scaler, scaler_path)

    print(f"\nModel saved to: {model_path}")
    print(f"Scaler saved to: {scaler_path}")

    return best_model, scaler


if __name__ == '__main__':
    train_and_save_model()
    print("\nModel training complete! Run the Django app with: python manage.py runserver")
