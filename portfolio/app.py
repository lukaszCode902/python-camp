from flask import Flask, render_template, request, jsonify, send_file
import json
from datetime import datetime
import os

app = Flask(__name__)

# Wczytaj dane projektów z pliku JSON
def load_projects():
    try:
        with open('data/site_data.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data.get('projects', [])
    except FileNotFoundError:
        return []

# Zapisz nowy projekt
def save_project(project):
    projects = load_projects()
    projects.append(project)
    site_data = {
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "projects": projects,
        "meta": {
            "title": "Moje Portfolio",
            "description": "Portfolio projektów i umiejętności",
            "author": "Twoje Imię"
        }
    }
    with open('data/site_data.json', 'w', encoding='utf-8') as file:
        json.dump(site_data, file, ensure_ascii=False, indent=4)

@app.route('/')
def home():
    projects = load_projects()
    return render_template('index.html', projects=projects)

# API dla projektów
@app.route('/api/projects', methods=['GET'])
def get_projects():
    projects = load_projects()
    return jsonify(projects)

@app.route('/api/projects', methods=['POST'])
def add_project():
    project = request.json
    save_project(project)
    return jsonify({"message": "Projekt został dodany pomyślnie!"})

@app.route('/api/projects/<int:project_id>', methods=['DELETE'])
def delete_project(project_id):
    projects = load_projects()
    if 0 <= project_id < len(projects):
        projects.pop(project_id)
        site_data = {
            "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "projects": projects,
            "meta": {
                "title": "Moje Portfolio",
                "description": "Portfolio projektów i umiejętności",
                "author": "Twoje Imię"
            }
        }
        with open('data/site_data.json', 'w', encoding='utf-8') as file:
            json.dump(site_data, file, ensure_ascii=False, indent=4)
        return jsonify({"message": "Projekt został usunięty pomyślnie!"})
    return jsonify({"error": "Nie znaleziono projektu"}), 404

# API dla formularza kontaktowego
@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # Zapisz wiadomość do pliku
    messages = []
    try:
        with open('data/messages.json', 'r', encoding='utf-8') as file:
            messages = json.load(file)
    except FileNotFoundError:
        pass
    
    messages.append({
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "name": data.get('name'),
        "email": data.get('email'),
        "message": data.get('message')
    })
    
    with open('data/messages.json', 'w', encoding='utf-8') as file:
        json.dump(messages, file, ensure_ascii=False, indent=4)
    
    return jsonify({
        "message": "Dziękujemy za wiadomość! Odpowiemy najszybciej jak to możliwe.",
        "status": "success"
    })

# API dla statystyk
@app.route('/api/stats', methods=['GET'])
def get_stats():
    projects = load_projects()
    try:
        with open('data/messages.json', 'r', encoding='utf-8') as file:
            messages = json.load(file)
    except FileNotFoundError:
        messages = []
    
    stats = {
        "total_projects": len(projects),
        "total_messages": len(messages),
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    return jsonify(stats)

# API dla wyszukiwania projektów
@app.route('/api/projects/search', methods=['GET'])
def search_projects():
    query = request.args.get('q', '').lower()
    projects = load_projects()
    
    filtered_projects = [
        project for project in projects
        if query in project['title'].lower() or
           query in project['description'].lower() or
           any(query in tech.lower() for tech in project['technologies'])
    ]
    
    return jsonify(filtered_projects)

if __name__ == '__main__':
    # Upewnij się, że katalog data istnieje
    os.makedirs('data', exist_ok=True)
    app.run(debug=True) 