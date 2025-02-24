import json
import time
import os
import subprocess

def execute_adb_commands(username, password):
    commands = [
        ['adb', 'shell', 'am', 'start', '-n', 'com.pnc.ecommerce.mobile/com.pnc.mbl.android.application.legacy.ui.MainActivity'],
        ['sleep', '1'],
        ['adb', 'shell', 'input', 'tap', '500', '760'],
        ['adb', 'shell', 'input', 'text', username],
        ['adb', 'shell', 'input', 'tap', '930', '880'],
        ['adb', 'shell', 'input', 'tap', '500', '1000'],
        ['adb', 'shell', 'input', 'text', password],
        ['adb', 'shell', 'input', 'tap', '500', '1200']
    ]
    
    for cmd in commands:
        if cmd[0] == 'sleep':
            time.sleep(float(cmd[1]))
        else:
            subprocess.run(cmd)

def watch_json_file(json_file):
    last_modified = 0
    
    while True:
        try:
            # Check if file exists and has been modified
            if os.path.exists(json_file):
                current_modified = os.path.getmtime(json_file)
                
                if current_modified > last_modified:
                    with open(json_file, 'r') as file:
                        data = json.load(file)
                        
                    if 'username' in data and 'password' in data:
                        print("Found credentials, executing commands...")
                        execute_adb_commands(data['username'], data['password'])
                        
                        # Clear the file
                        with open(json_file, 'w') as file:
                            json.dump({}, file)
                        print("Credentials processed and file cleared")
                    
                    last_modified = current_modified
            
            time.sleep(1)  # Check every second
            
        except KeyboardInterrupt:
            print("\nStopping watch...")
            break
        except json.JSONDecodeError:
            print("Invalid JSON format")
            time.sleep(1)
        except Exception as e:
            print(f"Error: {e}")
            time.sleep(1)

if __name__ == "__main__":
    JSON_FILE = "credentials.json"  # Your JSON file name
    print(f"Starting to watch {JSON_FILE} for credentials...")
    watch_json_file(JSON_FILE)