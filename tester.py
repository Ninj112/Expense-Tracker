# Again, here you import the python file that has the json variables along with
# the json library
import json
import SavedData

# again its the same function, the only difference is that we type R (read) instead
# of W then we use the function load.
with open("expenses.json", "r") as file:
    load = json.load(file)

print(load)
