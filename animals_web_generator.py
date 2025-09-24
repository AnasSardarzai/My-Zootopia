import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')


output = ''
for i in animals_data:
    output += '<li class="cards__item">\n'
    output += f"Name: {i['name']}<br/>\n"
    output += f"Diet: {i['characteristics']['diet']}<br/>\n"
    output += f"Location: {i['locations'][0]}<br/>\n"

    if "type" in i["characteristics"]:
        output += f"Type: {i['characteristics']['type']}<br/>\n"

    output += '</li>\n'

with open('animals_template.html', 'r') as file:
    html_template = file.read()

html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

with open('animals_template.html', 'w') as file:
    file.write(html_content)

print("HTML-Datei 'animals.html' wurde erstellt!")
