import pandas as pd
import kagglehub
import os

# Fetch data from Kaggle API
try:
    path = kagglehub.dataset_download("valakhorasani/mobile-device-usage-and-user-behavior-dataset")  # Downloads the dataset
    print("Data downloaded from Kaggle to:", path)
except Exception as e:
    print(f"Failed to download data from Kaggle: {e}")

# Get the list of files in the downloaded directory dynamically
downloaded_files = os.listdir(path)

# Read each file dynamically (instead of hardcoding paths)
dataframes = []

for file_name in downloaded_files:
    # Skip non-CSV files like .DS_Store
    if not file_name.endswith('.csv'):
        print(f"Skipping non-CSV file: {file_name}")
        continue
    
    file_path = os.path.join(path, file_name)



