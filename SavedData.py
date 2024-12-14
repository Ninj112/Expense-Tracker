# You just import the json library
import json

# This is how you declare variables in json, works exactly like python lists
userData = {
    "FirstName" : "none",
    "Age": 20
}

# This is the function used to "dump" (save) the file. you give the file
# a name "expenses.json" then put either W or R, which means Write or Read
# in this case we write the date, then dump the file
with open("expenses.json", "w") as file:
    json.dump(userData, file)