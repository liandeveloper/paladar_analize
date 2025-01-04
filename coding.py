import json
import os

# JSON Files
path = 'data_sets/restaurants_bars'

# JSON List
json_list = []

# Main Path of the Folder
for folder in os.listdir(path):
    path_folder = os.path.join(path, folder)

    # Check if is a Folder
    if os.path.isdir(path_folder):
        # Check each Files in the Folder
        for file in os.listdir(path):
            if file.endswith('.json'): # Check all Files end with '.json'
                path_file = os.path.join(path, file)

                # Load JSON
                with open(path_file, 'r', encoding='utf-8') as f:
                    datas = json.load(f)
                    json_list.append(datas) # Add Datas to the List
print(json_list)