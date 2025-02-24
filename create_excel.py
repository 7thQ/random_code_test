
import pandas as pd

# Create a simple example DataFrame
data = {
    "number": ["17029371712","12792262440","16464895460"],
    "name":["david", "329422","232324"]
}

# Convert the DataFrame to an Excel file
# file_path = "example.xlsx"
file_path = "example.xlsx"

df = pd.DataFrame(data)
df.to_excel(file_path, index=False)

print(f"Excel file created at: {file_path}")




# # Load the data from the specific sheet
# sheet_name = 'https://sikcc.ru/shop2'
# df = data.parse(sheet_name)

# # Save it to a new Excel file
# new_file_path = '/mnt/data/new_sikcc_data.xlsx'
# df.to_excel(new_file_path, index=False)

# new_file_path
