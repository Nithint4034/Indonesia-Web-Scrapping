import pandas as pd
from tkinter import filedialog
import tkinter as tk
from spellchecker import SpellChecker

# Create a Tkinter window
root = tk.Tk()
root.withdraw()  # Hide the root window

# Prompt the user to select a file
file_path = filedialog.askopenfilename(title="Select CSV file", filetypes=[("CSV files", "*.csv")])

# Check if a file was selected 
if file_path:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)

    # Initialize spell checker
    spell = SpellChecker()

    # Check for spelling errors in the 'POI_NAME' column
    misspelled_poi = df['POI_NAME'].apply(lambda x: spell.unknown(x.split()))

    # Print misspelled words and their indices
    misspelled_indices = []
    for index, misspelled in misspelled_poi.items():
        if misspelled:
            misspelled_indices.append(index)
            print(f"Index: {index}, POI_NAME: {df.at[index, 'POI_NAME']}, Misspelled: {', '.join(misspelled)}")

    if not misspelled_indices:
        print("No spelling errors found in the POI_NAME column.")
else:
    print("No file selected.")
