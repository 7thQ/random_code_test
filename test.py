






import pandas as pd
import keyboard

def display_row_navigation(file_path):
    try:
        # Load the Excel file
        df = pd.read_excel(file_path)
        total_rows = len(df)

        if total_rows == 0:
            print("The file has no rows to display.")
            return

        current_index = 0

        print("Use the UP and DOWN arrow keys to navigate rows. Press 'ESC' to exit.")
        
        while True:
            # Display the current row
            print(f"\nRow {current_index + 1} of {total_rows}:\n", df.iloc[current_index])
            
            # Wait for key press
            key = keyboard.read_event(suppress=True).name
            
            if key == 'down':
                # Move to the next row if not at the last row
                if current_index < total_rows - 1:
                    current_index += 1
                else:
                    print("Already at the last row.")

            elif key == 'up':
                # Move to the previous row if not at the first row
                if current_index > 0:
                    current_index -= 1
                else:
                    print("Already at the first row.")

            elif key == 'esc':
                # Exit the loop
                print("Exiting row navigation.")
                break

    except Exception as e:
        print(f"An error occurred: {e}")

# File path
data_file = "data/finished/caliBOA.xlsx"

# Call the function
display_row_navigation(data_file)
