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

# Fetch data from the first Kaggle API (first dataset)
try:
    path1 = kagglehub.dataset_download("philiphyde1/nfl-stats-1999-2022")  # Downloads the first Kaggle dataset
    print("Data downloaded from Kaggle to:", path1)
except Exception as e:
    print(f"Failed to download data from Kaggle: {e}")
   
downloaded_files1 = os.listdir(path1)

dataframes1 = []

for file_name in downloaded_files1:
    # Skip non-CSV files like .DS_Store
    if not file_name.endswith('.csv'):
        print(f"Skipping non-CSV file: {file_name}")
        continue
    
    file_path = os.path.join(path1, file_name)
    try:
        df = pd.read_csv(file_path)
        dataframes1.append(df)
        print(f"Data loaded successfully from: {file_path}")
    except Exception as e:
        print(f"Failed to load data from {file_path}: {e}")

# Combine all dataframes from the first Kaggle dataset into one
if dataframes1:
    try:
        kaggle_combined_data1 = pd.concat(dataframes1, ignore_index=True)
        print("All data from first Kaggle dataset combined successfully.")
    except Exception as e:
        print(f"Failed to combine first Kaggle dataset: {e}")
else:
    print("No data from first Kaggle dataset available to combine.")

# Fetch data from the second Kaggle API (second dataset)
try:
    path2 = kagglehub.dataset_download("aryashah2k/beginners-sports-analytics-nfl-dataset")  # Downloads the second Kaggle dataset
    print("Data downloaded from Kaggle to:", path2)
except Exception as e:
    print(f"Failed to download data from Kaggle: {e}")
   
downloaded_files2 = os.listdir(path2)

dataframes2 = []

for file_name in downloaded_files2:
    # Skip non-CSV files like .DS_Store
    if not file_name.endswith('.csv'):
        print(f"Skipping non-CSV file: {file_name}")
        continue
    
    file_path = os.path.join(path2, file_name)
    try:
        df = pd.read_csv(file_path)
        dataframes2.append(df)
        print(f"Data loaded successfully from: {file_path}")
    except Exception as e:
        print(f"Failed to load data from {file_path}: {e}")

# Combine all dataframes from the second Kaggle dataset into one
if dataframes2:
    try:
        kaggle_combined_data2 = pd.concat(dataframes2, ignore_index=True)
        print("All data from second Kaggle dataset combined successfully.")
    except Exception as e:
        print(f"Failed to combine second Kaggle dataset: {e}")
else:
    print("No data from second Kaggle dataset available to combine.")

# Combine the GitHub data with both Kaggle datasets (if all are available)
if 'offensive_data' in locals() and 'kaggle_combined_data1' in locals() and 'kaggle_combined_data2' in locals():
    try:
        # Combine the data from all sources
        df = pd.concat([offensive_data, kaggle_combined_data1, kaggle_combined_data2], ignore_index=True)
        print("All data combined successfully from GitHub and both Kaggle datasets.")
        print(df.head())  # Display the first few rows of the combined data
    except Exception as e:
        print(f"Failed to combine data from GitHub and Kaggle: {e}")
else:
    print("No data available for combining from one or more sources.")
