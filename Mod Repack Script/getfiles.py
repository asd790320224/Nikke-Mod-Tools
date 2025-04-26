import os
import json
import shutil
import re

# Define paths relative to the script's location
script_dir = os.path.dirname(os.path.abspath(__file__))  # Script directory

# Look for JSON files in the script directory
json_files = [f for f in os.listdir(script_dir) if f.endswith('.json')]

# Error handling for multiple or no JSON files
if len(json_files) == 0:
    raise FileNotFoundError("No JSON file found in the script directory.")
elif len(json_files) > 1:
    raise FileExistsError("Multiple JSON files found in the script directory. Please keep only one.")

# Open the JSON file
json_file_path = os.path.join(script_dir, json_files[0])

# Folder path to search for
target_folder_path = os.path.expandvars(r"%USERPROFILE%\AppData\LocalLow\Unity\com_proximabeta_NIKKE\aeb001dfac41dab1192aeo074efc3e21")

# Validate the target folder path
if not os.path.exists(target_folder_path) or not os.path.isdir(target_folder_path):
    print(f"Folder '{target_folder_path}' not found.")
    user_input = input("Please enter the full path to the folder (e.g., C:\\NIKKE): ")
    
    # Normalize user input
    user_input = user_input.strip().replace("/", "\\")  # Replace forward slashes with backslashes

    # Validate the user input
    if os.path.exists(user_input) and os.path.isdir(user_input):
        target_folder_path = user_input
    else:
        raise FileNotFoundError(f"Provided folder path '{user_input}' does not exist or is not a directory.")

# Set target directory within the script's directory
target_dir = os.path.join(script_dir, "Original Bundles")

# Define filename patterns
patterns = [
    r"spinecombatcharactergroup\(hd\)_assets_spine/combat/c\d{3}/\d{2}/cover_hd\.bundle",
    r"spinecombatcharactergroup\(hd\)_assets_spine/combat/c\d{3}/\d{2}/aim_hd\.bundle",
    r"spinestandingcharactergroup\(hd\)_assets_spine/standing/c\d{3}/\d{2}_hd\.bundle",
    r"icons-char-mi\(hd\)_assets_mi_c\d{3}_\d{2}_s\.bundle"
]

# Function to check if a JSON key matches any of the patterns
def matches_pattern(key):
    return any(re.match(pattern, key) for pattern in patterns)

# Load the JSON data
with open(json_file_path, 'r') as f:
    data = json.load(f)

# Iterate through each key-value pair in the JSON
for key, hash_filename in data.items():
    # Check if the key matches the required patterns
    if matches_pattern(key):
        source_path = os.path.join(target_folder_path, hash_filename)
        target_path = os.path.join(target_dir, hash_filename)
        
        # Check if the source file exists and copy it
        if os.path.exists(source_path):
            shutil.copy2(source_path, target_path)
            print(f"Copied {hash_filename} to {target_path}")
        else:
            print(f"File {hash_filename} not found in {target_folder_path}")

# Print the important message
print("IMPORTANT: Make sure to decrypt the entire Original Bundles folder using NAU by dragging it on top of it.")

# Wait for user to press Enter to close
while True:
    user_input = input("Press Enter to close...")
    if user_input == "":
        break  # Exit the loop when Enter is pressed