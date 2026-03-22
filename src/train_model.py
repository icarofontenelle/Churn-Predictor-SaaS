import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def train_model():
    # Paths
    raw_data_path = os.path.join('data', 'raw', 'churn_data.csv')
    model_dir = 'models'
    model_path = os.path.join(model_dir, 'churn_model.pkl')
    
    # Ensure directory exists
    os.makedirs(model_dir, exist_ok=True)

    # Load data
    if not os.path.exists(raw_data_path):
        print(f"Error: {raw_data_path} not found.")
        return

    try:
        df = pd.read_csv(raw_data_path)
    except Exception as e:
        print(f"Error reading dataset: {e}")
        return

    # Prepare features and target
    # columns: tenure, monthly_charges, support_calls, churn
    X = df.drop('churn', axis=1)
    y = df['churn']

    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train model
    print(f"Training RandomForestClassifier on {len(X_train)} samples...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predict and Evaluate
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    
    print(f"\nModel Accuracy: {accuracy:.4f}")
    print("\nConfusion Matrix:")
    print(cm)
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))

    # Save model
    try:
        joblib.dump(model, model_path)
        print(f"\nModel successfully saved to {model_path}")
    except Exception as e:
        print(f"Error saving model: {e}")

if __name__ == "__main__":
    train_model()
