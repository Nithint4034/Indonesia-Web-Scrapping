import pandas as pd
from tkinter import filedialog
import tkinter as tk

# Create a Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user to select a file
file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

# Check if a file was selected
if file_path:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Check for duplicates in the 'POI_NAME' column
    poi_duplicates = df[df.duplicated('POI_NAME', keep=False)]

    # Check for duplicates in the 'BUILD_LATE' column
    build_date_duplicates = df[df.duplicated('BUILD_LATE', keep=False)]

    # Check for duplicates in the 'BUILD_LONE' column
    build_long_duplicates = df[df.duplicated('BUILD_LONE', keep=False)]

    # Combine duplicates from all columns
    all_duplicates = pd.concat([poi_duplicates, build_date_duplicates, build_long_duplicates]).drop_duplicates()

    # Print the duplicate entries including PHOTO_ID
    if not all_duplicates.empty:
        print("Duplicate Entries:")
        print(all_duplicates[['POI_NAME', 'BUILD_LATE', 'BUILD_LONE', 'PHOTO_ID']])
    else:
        print("No duplicate entries found.")
else:
    print("No file selected.")

