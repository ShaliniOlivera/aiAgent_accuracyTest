import os
import pandas as pd
from sentence_transformers import util
from config import model, df, save_results,similarity, SIMILARITY_THRESHOLD  
from api_helper import send_request  
from expected_results import expected_results  


test_results = []  

# Run tests
for index, row in df.iterrows():
    test_name = row["Test Name"]
    test_input = row["Input"]
    expected_key = row["Expected"]

    # Fetch expected value from dictionary
    expected = expected_results.get(expected_key, "Unknown expected key")
    print(f"\n🔹 Running test: {test_name} | Input: {test_input}")

    # Call the API helper function
    actual = send_request(test_input)

    if actual:
        actual_cleaned = actual.split("available:")[-1].strip()
        actual_cleaned = actual_cleaned.replace("\n", ", ")

        embedding1 = model.encode(actual_cleaned, convert_to_tensor=True)
        embedding2 = model.encode(expected, convert_to_tensor=True)
        similarity = util.pytorch_cos_sim(embedding1, embedding2).item() * 100

    # Determine test status
    test_result = "Passed" if similarity >= SIMILARITY_THRESHOLD else "Failed"

    # Store results
    test_results.append([test_name, test_input, expected, actual, f"{similarity:.2f}%", test_result])

# Save test results
save_results(test_results)
