import json

def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')

output = ''

for i in animals_data:
    output += f"Name: {i['name']}\n"
    output += f"Diet: {i['characteristics']['diet']}\n"
    output += f"Location: {i['locations'][0]}\n"
    if "type" in i["characteristics"]:
        output += f"Type: {i['characteristics']['type']}\n\n"
    else:
        output += f"\n"

# 3. HTML-Vorlage laden
with open('animals_template.html', 'r') as file:
    html_template = file.read()

# 4. Platzhalter ersetzen
html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

# 5. Neue HTML-Datei schreiben
with open('animals_template.html', 'w') as file:
    file.write(html_content)

"""

Name: American Foxhound
Diet: Omnivore
Location: North-America
Type: Hound

"""