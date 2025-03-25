import json
import os
from datetime import datetime

# Przykładowe dane projektów
projects = [
    {
        "title": "Projekt Portfolio",
        "description": "Strona portfolio z wykorzystaniem HTML, CSS i JavaScript",
        "technologies": ["HTML", "CSS", "JavaScript", "Python"],
        "image": "images/portfolio.jpg",
        "link": "#"
    },
    {
        "title": "System Zarządzania",
        "description": "Aplikacja do zarządzania zadaniami i projektami",
        "technologies": ["Python", "SQL", "Flask"],
        "image": "images/task-manager.jpg",
        "link": "#"
    },
    {
        "title": "Blog Techniczny",
        "description": "Blog o programowaniu i nowych technologiach",
        "technologies": ["HTML", "CSS", "JavaScript"],
        "image": "images/blog.jpg",
        "link": "#"
    }
]

def generate_projects_html():
    """Generuje HTML dla sekcji projektów"""
    projects_html = ""
    for project in projects:
        projects_html += f"""
        <div class="project-card">
            <img src="{project['image']}" alt="{project['title']}">
            <h3>{project['title']}</h3>
            <p>{project['description']}</p>
            <div class="project-technologies">
                {''.join([f'<span>{tech}</span>' for tech in project['technologies']])}
            </div>
            <a href="{project['link']}" class="project-link">Zobacz projekt</a>
        </div>
        """
    return projects_html

def update_index_html():
    """Aktualizuje plik index.html o wygenerowaną zawartość"""
    with open('index.html', 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Znajdź miejsce do wstawienia projektów
    projects_placeholder = '<!-- Projekty będą dodawane dynamicznie przez Pythona -->'
    projects_html = generate_projects_html()
    
    # Zamień placeholder na wygenerowany HTML
    updated_content = content.replace(projects_placeholder, projects_html)
    
    # Zapisz zaktualizowany plik
    with open('index.html', 'w', encoding='utf-8') as file:
        file.write(updated_content)

def generate_site_data():
    """Generuje dane strony w formacie JSON"""
    site_data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "projects": projects,
        "meta": {
            "title": "Moje Portfolio",
            "description": "Portfolio projektów i umiejętności",
            "author": "Twoje Imię"
        }
    }
    
    # Zapisz dane do pliku JSON
    with open('data/site_data.json', 'w', encoding='utf-8') as file:
        json.dump(site_data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    # Upewnij się, że katalog data istnieje
    os.makedirs('data', exist_ok=True)
    
    # Generuj dane i aktualizuj stronę
    generate_site_data()
    update_index_html()
    print("Strona została zaktualizowana pomyślnie!") 