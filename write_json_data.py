import json


def write_json_data(filename, data):
    try:
        with open(filename, 'w') as json_file:
            json.dump(data, json_file, indent=4)
        print(f"Data successfully written to {filename}")
    except Exception as e:
        print(f"Error writing to {filename}: {e}")
