import json


def load_data(file_path):
    with open(file_path, "r") as handle:
        return json.load(handle)

animals_data = load_data('animals_data.json')


output = ''
for animal in animals_data:
    output += '<li class="cards__item">\n'
    output += f'  <div class="card__title">{animal["name"]}</div>\n'
    output += '  <p class="card__text">\n'
    output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'
    output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'


    if "type" in animal["characteristics"]:
        output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

    output += '  </p>\n'
    output += '</li>\n'


with open('animals_template.html', 'r') as file:
    html_template = file.read()


html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)


with open('animals.html', 'w') as file:
    file.write(html_content)

print("HTML-Datei 'animals.html' wurde erstellt!")
