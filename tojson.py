import os
import pandas as pd
import json

# File paths
DATA_DIR = os.path.join(os.getcwd(), 'data')
NOT_FINISHED_DIR = os.path.join(DATA_DIR, 'jsonPrep')
FINISHED_DIR = os.path.join(DATA_DIR, 'Json')
INPUT_FILE = os.path.join(NOT_FINISHED_DIR, 'pnc_out.xlsx')
OUTPUT_FILE = os.path.join(FINISHED_DIR, 'readydata.json')

def convert_to_json_format(input_file, output_file):
    try:
        # Read the Excel file
        print(f"Reading file from: {input_file}")
        df = pd.read_excel(input_file)
        
        # Get column names for reference
        columns = df.columns.tolist()
        print("Processing columns:", columns)
        
        # Initialize the JSON structure
        json_data = {}
        
        # Process each row
        for index, row in df.iterrows():
            lead_number = index + 1  # Start numbering from 1
            
            # Create address string from columns 4,5,6,7
            address_parts = [
                str(row[columns[3]]) if pd.notna(row[columns[3]]) else "",  # Column 4
                str(row[columns[4]]) if pd.notna(row[columns[4]]) else "",  # Column 5
                str(row[columns[5]]) if pd.notna(row[columns[5]]) else "",  # Column 6
                str(row[columns[6]]) if pd.notna(row[columns[6]]) else ""   # Column 7
            ]
            address = " ".join(part for part in address_parts if part)
            
            # Create lead entry
            lead = {
                "NAME": str(row[columns[2]]) if pd.notna(row[columns[2]]) else "",
                "PHONE": str(row[columns[8]]) if pd.notna(row[columns[8]]) else "",
                "CARD FIRST DIGITS": str(row[columns[0]]) if pd.notna(row[columns[0]]) else "",
                "CARD Expiration date": str(row[columns[1]]) if pd.notna(row[columns[1]]) else "",
                "Address on file": address,
                "Nothing else is available for security purposes": True,
                "there is limited information and access": True
            }
            
            # Add lead to the JSON data with lead number
            json_data[f"Lead {lead_number}"] = lead
        
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        
        # Save to JSON file with proper formatting
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(json_data, f, indent=2, ensure_ascii=False)
        
        print(f"\nProcessed {len(json_data)} leads")
        print(f"JSON file saved to: {output_file}")
        
        # Print sample of first lead (with sensitive data masked)
        if json_data:
            print("\nSample of first lead (sensitive data masked):")
            first_key = list(json_data.keys())[0]
            sample = json_data[first_key].copy()
            sample["CARD FIRST DIGITS"] = "XXXX"
            sample["PHONE"] = "XXXXXXXXXX"
            print(json.dumps({first_key: sample}, indent=2))
            
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        raise

if __name__ == "__main__":
    convert_to_json_format(INPUT_FILE, OUTPUT_FILE)