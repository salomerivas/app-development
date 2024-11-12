import pandas as pd
import kagglehub
import os

# Load data from GitHub
github_url = "https://raw.githubusercontent.com/salomerivas/app-development/refs/heads/main/nfl_offensive_stats.csv"

try:
    offensive_data = pd.read_csv(github_url)
    print("Data loaded successfully from GitHub.")
except Exception as e:
    print("Failed to load data from GitHub:", e)

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
    except Exception as e:
        print(f"Failed to combine Kaggle data: {e}")
else:
    print("No data from Kaggle available to combine.")

# Combine the GitHub data with the Kaggle data (if both are available)
if 'offensive_data' in locals() and 'kaggle_combined_data' in locals():
    try:
        # Combine the data from both sources
        final_combined_data = pd.concat([offensive_data, kaggle_combined_data], ignore_index=True)
        print("All data combined successfully from both GitHub and Kaggle.")
        print(final_combined_data.head())  # Display the first few rows of the combined data
    except Exception as e:
        print(f"Failed to combine data from GitHub and Kaggle: {e}")
else:
    print("No data available for combining from one or both sources.")
