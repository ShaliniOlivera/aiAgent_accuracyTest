import os
from datetime import datetime
import pandas as pd
from sentence_transformers import SentenceTransformer

# API URL for webhook
API_URL = "https://ce54-2001-fd8-f514-ea52-1547-40f2-4175-ba97.ngrok-free.app/google-chat/webhook"

SIMILARITY_THRESHOLD = 85 
# paths
base_path = os.path.dirname(os.path.abspath(__file__))
parent_path = os.path.dirname(base_path)
test_cases_path = os.path.join(base_path, "test_cases.xlsx")

# tes results
results_folder = os.path.join(parent_path, "test_results")
os.makedirs(results_folder, exist_ok=True)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
results_path = os.path.join(results_folder, f"test_results_{timestamp}.xlsx")

# Load transformer model
model = SentenceTransformer("paraphrase-MiniLM-L6-v2")

# Read test cases from Excel
df = pd.read_excel(test_cases_path, usecols=["Test Name", "Input", "Expected"])

# Function to save test results
def save_results(test_results):
    results_df = pd.DataFrame(test_results, columns=["Test Name", "Input", "Expected", "Actual", "Similarity", "Test Result"])
    results_df.to_excel(results_path, index=False)
    print(f"\n✅ Test execution completed. Results saved to {results_path}")
