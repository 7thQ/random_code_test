
#fixes data conversion from scrapper
# import pandas as pd

# # Variables to hold file paths
# input_file_path = 'data/not_started/rows.xlsx'  # Placeholder: Update with the path to your input file
# output_file_path = 'data/not_finished/2_file.xlsx'  # Placeholder: Update with the desired output file path

# # Load the Excel file
# excel_data = pd.ExcelFile(input_file_path)

# # Display available sheet names (optional, for debugging or information)
# print("Available sheets:", excel_data.sheet_names)

# # Load data from the first sheet (or specify a sheet name if known)
# sheet_name = excel_data.sheet_names[0]  # Replace with specific sheet name if needed
# data = excel_data.parse(sheet_name)

# # Write the data to a new Excel file
# data.to_excel(output_file_path, index=False)

# print(f"Data successfully rewritten to: {output_file_path}")



#removes all the columns i dont want 
import pandas as pd

# Variables to hold file paths
input_file_path = 'data/not_started/rows.xlsx'  # Placeholder: Update with the path to your input file
output_file_path = 'data/not_finished/output_file.xlsx'  # Placeholder: Update with the desired output file path

# Specify columns to remove (1-based index)
columns_to_remove = [3, -5,-4,-3,-2,-1]  # Example: 3rd column from the left, and the last column

# Load the Excel file
excel_data = pd.ExcelFile(input_file_path)

# Display available sheet names (optional, for debugging or information)
print("Available sheets:", excel_data.sheet_names)

# Load data from the first sheet (or specify a sheet name if known)
sheet_name = excel_data.sheet_names[0]  # Replace with specific sheet name if needed
data = excel_data.parse(sheet_name)

# Convert 1-based indexes to 0-based and handle negative indexing
columns_to_remove = [col - 1 if col > 0 else col for col in columns_to_remove]

# Adjust column removal to account for shifting indices
columns_to_remove_adjusted = sorted([col if col >= 0 else data.shape[1] + col for col in columns_to_remove])

# Remove specified columns
if data.shape[1] > max(columns_to_remove_adjusted):
    for idx, col in enumerate(columns_to_remove_adjusted):
        adjusted_col = col - idx  # Adjust index based on previous removals
        data = data.drop(data.columns[adjusted_col], axis=1)
else:
    print("The DataFrame has fewer columns than specified for removal.")

# Write the data to a new Excel file
data.to_excel(output_file_path, index=False)

print(f"Data successfully rewritten to: {output_file_path}")
