# Projekt Portfolio

Witaj w projekcie portfolio! Ten projekt łączy wszystkie poznane technologie: HTML, CSS, JavaScript i Python w jeden spójny projekt.

## Struktura projektu

```
portfolio/
├── app.py              # Aplikacja Flask
├── templates/
│   └── index.html      # Szablon strony
├── static/
│   ├── css/
│   │   └── style.css   # Style CSS
│   ├── js/
│   │   └── main.js     # Skrypty JavaScript
│   └── images/         # Katalog na obrazy
└── data/
    └── site_data.json  # Dane generowane przez Pythona
```

## Jak to działa?

1. **Flask (Python)** - Serwer webowy obsługujący:

   - Wyświetlanie strony
   - Obsługę formularzy
   - API do dodawania projektów
   - Dynamiczne generowanie treści

2. **HTML** - Struktura strony jest zdefiniowana w szablonie `index.html`
3. **CSS** - Style i animacje są w pliku `style.css`
4. **JavaScript** - Interaktywność strony jest obsługiwana przez `main.js`

## Wymagania

- Python 3.x
- Flask (`pip install flask`)

## Jak uruchomić projekt?

1. Zainstaluj wymagane pakiety:

   ```bash
   pip install flask
   ```

2. Uruchom aplikację Flask:

   ```bash
   python app.py
   ```

3. Otwórz przeglądarkę i przejdź do:
   ```
   http://localhost:5000
   ```

## Co możesz zmodyfikować?

1. **Wygląd strony** - Edytuj plik `static/css/style.css`
2. **Interaktywność** - Modyfikuj plik `static/js/main.js`
3. **Logika serwera** - Zmień plik `app.py`
4. **Struktura** - Dostosuj plik `templates/index.html`

## Funkcjonalności

- Responsywny design
- Animacje i przejścia
- Dynamiczne dodawanie projektów
- Formularz kontaktowy
- Menu mobilne
- Płynne przewijanie
- API REST

## Zadania do wykonania

1. Dodaj własne projekty przez formularz na stronie
2. Zmień kolory i style w `style.css`
3. Dodaj nowe sekcje do strony w `index.html`
4. Zmodyfikuj animacje w `main.js`
5. Dodaj nowe endpointy API w `app.py`

## Wskazówki

- Używaj komentarzy w kodzie
- Testuj zmiany w przeglądarce
- Zapisuj zmiany w Git
- Eksperymentuj z nowymi funkcjami
- Sprawdzaj logi serwera Flask

## Technologie użyte w projekcie

- Flask (Python)
- HTML5
- CSS3 (z animacjami i responsywnością)
- JavaScript (ES6+)
- Git (do kontroli wersji)
