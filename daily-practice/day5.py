#Python Pandas Read JSON 
#Pandas provides a function called read_json() to read data from a JSON file and create a DataFrame. The read_json() function takes the file path as an argument and returns a DataFrame containing the data from the JSON file.
import pandas as pd

 #loading the JSON file into a DataFrame
df = pd.read_json('daily-practice\data.js')
print(df.to_string())


#dictionary as a Json is not your file:

data = {
    "Duration": {
        "0": 60,
        "1": 45,
        "2": 30
    },
    "Pulse": {
        "0": 110,
        "1": 117,
        "2": 103
    },
    "Maxpulse": {
        "0": 130,
        "1": 145,
        "2": 135
    },
    "Calories": {
        "0": 409.1,
        "1": 479.0,
        "2": 340.0
    }
}

df = pd.DataFrame(data)
print(df.to_string())