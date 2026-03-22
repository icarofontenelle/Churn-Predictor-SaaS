import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def visualize_data():
    # Paths
    raw_data_path = os.path.join('data', 'raw', 'churn_data.csv')
    output_path = os.path.join('notebooks', 'churn_by_support.png')
    
    # Ensure directory exists (in case it wasn't created yet)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Load data
    if not os.path.exists(raw_data_path):
        print(f"Error: {raw_data_path} not found.")
        return

    try:
        df = pd.read_csv(raw_data_path)
    except Exception as e:
        print(f"Error reading dataset: {e}")
        return

    # Create plot
    plt.figure(figsize=(10, 6))
    
    # Check if columns exist
    if 'support_calls' in df.columns and 'churn' in df.columns:
        sns.countplot(data=df, x='support_calls', hue='churn')
        plt.title('Churn by Support Calls')
        plt.xlabel('Number of Support Calls')
        plt.ylabel('Count')
        plt.legend(title='Churn', labels=['Stayed (0)', 'Canceled (1)'])
        
        # Save plot
        plt.savefig(output_path)
        plt.close() # Close to free memory
        print(f"Visualization successfully saved to {output_path}")
    else:
        print(f"Error: Required columns ('support_calls', 'churn') not found in {df.columns.tolist()}")

if __name__ == "__main__":
    visualize_data()
