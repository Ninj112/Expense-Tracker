import json
import os

# File name to store the JSON data
FILENAME = 'data.json'

# Function to save the array to a JSON file
def save_data(data, filename=FILENAME):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
    print("Data saved successfully.")

# Function to load the array from a JSON file
def load_data(filename=FILENAME):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            return json.load(file)
    else:
        print("File not found. Returning an empty array.")
        return []

# Function to append an array to the existing data
def append_data(new_array, filename=FILENAME):
    data = load_data(filename)
    data.append(new_array)
    save_data(data, filename)
    print("Data appended successfully.")

# Example usage
if __name__ == "__main__":
    # Load existing data
    data = load_data()
    print("Current Data:", data)

    # # Example of appending a new array
    # new_array = [1, 2, 3, 4]
    # append_data(new_array)
    #
    # # Verify data after appending
    # updated_data = load_data()
    # print("Updated Data:", updated_data)

    # array = []
    # save_data(array)
