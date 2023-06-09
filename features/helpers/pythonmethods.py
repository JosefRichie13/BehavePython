# This file will contain all the helper methods which are related to python

import json


class HelperMethods:

    # This function will write to a JSON file, it takes in the JSON data and the path of the JSON file
    def WriteToFile(data, path):
        with open(path, "w") as outfile:
            json.dump(data, outfile)

    # This function will update a JSON file, it takes in the JSON data and the path of the JSON file
    def UpdateTheFile(data, path):
        with open(path, "r") as outfile:
            old_data = json.load(outfile)
            newData = old_data | data

        with open(path, "w") as outfile:
            json.dump(newData, outfile)

    # This function will read from a JSON file, it takes in the JSON data and the path of the JSON file and
    # returns the data
    def ReadFromFile(path):
        with open(path, "r") as openfile:
            data = json.load(openfile)
            return data