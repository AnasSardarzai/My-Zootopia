import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

for i in animals_data:
    print("Name:", i["name"])
    print("Diet:", i["characteristics"]["diet"])
    print("Location:", i["locations"][0])
    if "type" in i["characteristics"]:
        print("Type:", i["characteristics"]["type"])
    print("")

"""

Name: American Foxhound
Diet: Omnivore
Location: North-America
Type: Hound

"""