import json

def load_data(file_path: str) -> list:
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def generate_html_content(animals_data: list) -> str:
    output = ''
    for animal in animals_data:
        output += f"<p><strong>Name:</strong> {animal['name']}<br>\n"
        output += f"<strong>Diet:</strong> {animal['characteristics']['diet']}<br>\n"
        output += f"<strong>Location:</strong> {animal['locations'][0]}<br>\n"
        if "type" in animal["characteristics"]:
            output += f"<strong>Type:</strong> {animal['characteristics']['type']}<br>\n"
        output += "</p>\n"
    return output


def save_html(output_file: str, html_template_file: str, content: str) -> None:
    with open(html_template_file, 'r', encoding="utf-8") as file:
        html_template = file.read()

    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", content)

    with open(output_file, 'w', encoding="utf-8") as file:
        file.write(html_content)


def main():
    animals_data = load_data('animals_data.json')
    html_content = generate_html_content(animals_data)
    save_html('animals.html', 'animals_template.html', html_content)
    print("HTML-Datei 'animals.html' wurde erfolgreich erstellt.")


if __name__ == "__main__":
    main()
