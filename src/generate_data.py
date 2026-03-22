import csv
import random
import os

def generate_data():
    # Setting the output path relative to the project root
    output_path = os.path.join('data', 'raw', 'churn_data.csv')
    
    # Ensure directory exists (though it should already be there)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # Header
        writer.writerow(['tenure', 'monthly_charges', 'support_calls', 'churn'])
        
        for _ in range(1000):
            tenure = random.randint(1, 72)
            monthly_charges = round(random.uniform(20.0, 150.0), 2)
            support_calls = random.randint(0, 10)
            
            # Correlation logic:
            # If 'support_calls' > 5 or 'tenure' < 6, the chance of 'churn=1' should be higher.
            if support_calls > 5 or tenure < 6:
                # 70% probability of churn
                churn = 1 if random.random() < 0.7 else 0
            else:
                # 15% probability of churn
                churn = 1 if random.random() < 0.15 else 0
                
            writer.writerow([tenure, monthly_charges, support_calls, churn])
    
    print(f"Successfully generated 1000 rows of data in {output_path}")

if __name__ == "__main__":
    generate_data()
