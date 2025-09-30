import json

def load_data(file_path):
    """Load JSON data from file"""
    with open(file_path, "r") as handle:
        return json.load(handle)

def serialize_animal(animal):
    """Convert a single animal dictionary into HTML list item"""
    name = animal.get("name", "Unknown")
    characteristics = animal.get("characteristics", {})
    diet = characteristics.get("diet", "Unknown")
    animal_type = characteristics.get("type", "Unknown")
    locations = animal.get("locations", [])
    location = locations[0] if locations else "Unknown"

    return (
        '<li class="cards__item">\n'
        f'  <div class="card__title">{name}</div>\n'
        '  <p class="card__text">\n'
        f'      <strong>Diet:</strong> {diet}<br/>\n'
        f'      <strong>Location:</strong> {location}<br/>\n'
        f'      <strong>Type:</strong> {animal_type}<br/>\n'
        '  </p>\n'
        '</li>\n'
    )

def build_html(animals_data, template_path, output_path):
    """Generate HTML file with animal data"""
    output = ''.join(serialize_animal(animal) for animal in animals_data)

    with open(template_path, "r") as file:
        html_template = file.read()

    html_content = html_template.replace("__REPLACE_ANIMALS_INFO__", output)

    with open(output_path, "w") as file:
        file.write(html_content)

def main():
    animals_data = load_data("animals_data.json")
    build_html(animals_data, "animals_template.html", "animals.html")
    print("animals.html generated successfully")

if __name__ == "__main__":
    main()
