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
        if '2024_player_predictions' in file_name:
                pred_df = pd.read_csv(file_path)
                print(f"Data loaded successfully from: {file_path} (2024_player_predictions.csv)")
        elif 'weekly_player_data' in file_name:
                week_df = pd.read_csv(file_path)
                print(f"Data loaded successfully from: {file_path} (weekly_player_data.csv)")
        elif 'yearly_player_data' in file_name:
                year_df = pd.read_csv(file_path)
                print(f"Data loaded successfully from: {file_path} (yearly_player_data.csv)")
    except Exception as e:
            print(f"Failed to load data from {file_path}: {e}")

# Check if the specific dataframes are loaded correctly
if pred_df is not None:
    print("2024 Player Predictions DataFrame:")
    print(pred_df.head())
else:
    print("Failed to load 2024_player_predictions.csv")

if week_df is not None:
    print("Weekly Player Data DataFrame:")
    print(week_df.head())
else:
    print("Failed to load weekly_player_data.csv")

if year_df is not None:
    print("Yearly Player Data DataFrame:")
    print(year_df.head())
else:
    print("Failed to load yearly_player_data.csv")


