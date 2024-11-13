import pandas as pd
import kagglehub
import os

# Fetch data from Kaggle API
try:
    path = kagglehub.dataset_download("philiphyde1/nfl-stats-1999-2022")  # Downloads the dataset
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
    try:
        df = pd.read_csv(file_path)
        dataframes.append(df)
        print(f"Data loaded successfully from: {file_path}")
    except Exception as e:
        print(f"Failed to load data from {file_path}: {e}")

# Combine all dataframes from Kaggle dataset into one
if dataframes:
    try:
        kaggle_combined_data = pd.concat(dataframes, ignore_index=True)
        print("All data from Kaggle combined successfully.")
        print(kaggle_combined_data.head())  # Display the first few rows of the combined data
    except Exception as e:
        print(f"Failed to combine Kaggle data: {e}")
else:
    print("No data from Kaggle available to combine.")
