import os
import pandas as pd
import re

# File paths
DATA_DIR = os.path.join(os.getcwd(), 'data')
NOT_FINISHED_DIR = os.path.join(DATA_DIR, 'finished')
FINISHED_DIR = os.path.join(DATA_DIR, 'jsonPrep')
INPUT_FILE = os.path.join(NOT_FINISHED_DIR, 'allpnc_out.xlsx')
OUTPUT_FILE = os.path.join(FINISHED_DIR, 'pnc_out.xlsx')

def clean_numeric_data(value):
    """Remove commas and non-numeric characters, keeping only numbers."""
    if pd.isna(value):  # Check if the value is NaN
        return value
    # Convert to string if not already
    value = str(value)
    # Remove commas and keep only numbers
    cleaned = re.sub(r'[^0-9]', '', value)
    return cleaned if cleaned else None

def filter_and_clean_data(input_file, output_file):
    try:
        # Read the Excel file
        print(f"Reading file from: {input_file}")
        df = pd.read_excel(input_file)
        
        # Get initial row count
        initial_count = len(df)
        print(f"Initial number of rows: {initial_count}")
        
        # Find columns that contain 'phone' in their name (case insensitive)
        phone_columns = [col for col in df.columns if 'phone' in col.lower()]
        
        if not phone_columns:
            raise ValueError("No phone number columns found in the Excel file")
        
        print(f"Found phone number columns: {phone_columns}")
        
        # Clean columns 1 and 7 (index 0 and 6)
        col_1_name = df.columns[0]
        col_7_name = df.columns[6]
        
        print(f"Cleaning data in columns: {col_1_name} and {col_7_name}")
        
        # Apply cleaning to columns 1 and 7
        df[col_1_name] = df[col_1_name].apply(clean_numeric_data)
        df[col_7_name] = df[col_7_name].apply(clean_numeric_data)
        
        # Keep rows where at least one phone column has data
        mask = df[phone_columns].notna().any(axis=1)
        filtered_df = df[mask]
        
        # Get final row count
        final_count = len(filtered_df)
        removed_count = initial_count - final_count
        
        print(f"Rows removed: {removed_count}")
        print(f"Remaining rows: {final_count}")
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Save the filtered data
        filtered_df.to_excel(output_file, index=False)
        print(f"Filtered and cleaned data saved to: {output_file}")
        
        # Print sample of cleaned data
        print("\nSample of cleaned data:")
        print(f"First few rows of {col_1_name}:", filtered_df[col_1_name].head())
        print(f"First few rows of {col_7_name}:", filtered_df[col_7_name].head())
        
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    filter_and_clean_data(INPUT_FILE, OUTPUT_FILE)