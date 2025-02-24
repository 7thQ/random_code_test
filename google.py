
# import pandas as pd

# # Load your dataset
# file_path = "data/finished/caliBOA.xlsx"  # Update this with the correct file path
# df = pd.read_excel(file_path)

# # Print the content of the first row (columns 4 to 7) in horizontal format
# print("Testing Data Input:")

# row_selected = 2
# # Select columns 4 to 7 from the first row and handle ZIP code formatting
# row_data = df.iloc[0].apply(lambda x: f"{int(x)}" if isinstance(x, float) else str(x))
# row_address = df.iloc[row_selected, 3:7].apply(lambda x: f"{int(x)}" if isinstance(x, float) else str(x))
# row_string = "  ".join(row_address.values)



# # Join the values into a single horizontal string
# print("  ".join(row_data.values)) # 6234 Lakev...  San Ramon  CA  94582
# # print(f"{row_data.values}") # ['6234 Lakev...' 'San Ramon' 'CA' '94582']

# print(f"{row_string}")


# import googlemaps
# import json
# import os

# # Set up Google Maps Client
# api_key = "AIzaSyAF8FGzGWlDv6aNO94aKKL4Wb2Sr7lPWEI"
# gmaps = googlemaps.Client(key=api_key)

# # Example row_string (replace with your actual data)
# # row_string = "6234 Lakev... San Ramon CA 94582"

# # Output file path
# output_file_path = "data/address/results.json"

# # Ensure the directory exists
# os.makedirs(os.path.dirname(output_file_path), exist_ok=True)

# # Query the Google Maps API with row_string
# try:
#     results = gmaps.places(query=row_string)  # Perform the API query
    
#     # Format the data for better readability
#     formatted_results = json.dumps(results, indent=4)
    
#     # Write the results to a file
#     with open(output_file_path, "w") as output_file:
#         #edit this so that the outputs first number and letter match the input with out the ... if the furst choices matches than all good write to the file
#         output_file.write(formatted_results)
    
#     print(f"Results have been written to {output_file_path}")
# except Exception as e:
#     print(f"An error occurred: {e}")





# # shows data and has button to go next
# import pandas as pd

# def load_excel_file(file_path):
#     try:
#         # Load the Excel file
#         data = pd.read_excel(file_path)
        
#         # Display one row at a time
#         print("Data loaded successfully!")
#         print(f"Number of rows: {data.shape[0]}")
#         print(f"Number of columns: {data.shape[1]}")
        
#         for index, row in data.iterrows():
#             print("\nRow:")
#             print(row)
#             input("Press Enter to view the next row...")
#     except FileNotFoundError:
#         print(f"Error: The file at {file_path} was not found.")
#     except Exception as e:
#         print(f"An error occurred: {e}")

# if __name__ == "__main__":
#     file_path = "data/finished/caliBOA.xlsx"

#     load_excel_file(file_path)



