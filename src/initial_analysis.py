import pandas as pd
import os

def perform_analysis():
    # Load the dataset
    file_path = os.path.join('data', 'raw', 'churn_data.csv')
    
    if not os.path.exists(file_path):
        print(f"Error: dataset file not found at {file_path}")
        return

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        print(f"Error reading dataset: {e}")
        return

    # 1. Print the first 5 rows
    print("--- First 5 rows of the dataset ---")
    print(df.head())
    print("\n")

    # 2. Print statistical summary (describe)
    print("--- Statistical Summary (describe) ---")
    print(df.describe())
    print("\n")

    # 3. Print total Churn count (count canceled vs remained)
    print("--- Churn Count (0 = Remained, 1 = Canceled) ---")
    if 'churn' in df.columns:
        print(df['churn'].value_counts())
    else:
        print("Column 'churn' not found in dataset columns:", df.columns.tolist())
    print("\n")

if __name__ == "__main__":
    perform_analysis()
