import joblib
import pandas as pd
import os
import warnings

# Suppress sklearn warnings about feature names (already handled by DataFrame)
warnings.filterwarnings("ignore", category=UserWarning)

def predict_churn(tenure, monthly_charges, support_calls):
    # Path to model
    model_path = os.path.join('models', 'churn_model.pkl')
    
    if not os.path.exists(model_path):
        print(f"Error: Model not found at {model_path}. Please run src/train_model.py first.")
        return

    # Load model
    try:
        model = joblib.load(model_path)
    except Exception as e:
        print(f"Error loading model: {e}")
        return
    
    # Create a DataFrame for prediction (must match training feature order/names)
    data = pd.DataFrame([[tenure, monthly_charges, support_calls]], 
                        columns=['tenure', 'monthly_charges', 'support_calls'])
    
    # Predict
    prediction = model.predict(data)[0]
    
    # Get probability for the "Churn" class (1)
    if hasattr(model, 'predict_proba'):
        probability = model.predict_proba(data)[0][1]
        prob_str = f" (Churn Probability: {probability:.2%})"
    else:
        prob_str = ""
    
    result = "CHURN (Likely to cancel)" if prediction == 1 else "NO CHURN (Likely to stay)"
    
    print(f"Input Data: tenure={tenure}, monthly_charges={monthly_charges}, support_calls={support_calls}")
    print(f"Prediction: {result}{prob_str}")
    print("-" * 50)

if __name__ == "__main__":
    print("="*50)
    print("CHURN PREDICTOR - Inference Loop")
    print("="*50)
    
    # Test case 1: High risk (Churn probable)
    print("\n[Test Case 1: High Risk Instance]")
    predict_churn(2, 100, 8)
    
    # Test case 2: Low risk (No Churn probable)
    print("\n[Test Case 2: Healthy Instance]")
    predict_churn(24, 50, 1)
