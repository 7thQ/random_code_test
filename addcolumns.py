

import pandas as pd

def add_columns(file_path):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)
        
        # Add new columns for phone number and email
        df['Phone Number'] = ''  # Empty values
        df['Email'] = ''  # Empty values
        
        # Save the updated DataFrame back to the same file
        df.to_excel(file_path, index=False)
        
        print("Columns 'Phone Number' and 'Email' have been added successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

# File path
data_file = "data/finished/allpnc_out.xlsx"

# Call the function
add_columns(data_file)
