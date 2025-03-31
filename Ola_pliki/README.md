# Generator Umów o Pracę

Program do automatycznego generowania umów o pracę na podstawie danych z pliku Excel.

## Funkcjonalność

- Odczytuje dane pracowników z arkusza Excel
- Generuje indywidualne umowy o pracę na podstawie szablonu Word
- Automatycznie wstawia dane w odpowiednie miejsca w dokumencie
- Zapisuje wygenerowane dokumenty w oddzielnym folderze

## Wymagania

- Python 3.6 lub nowszy
- Biblioteki: pandas, openpyxl, python-docx

```
pip install pandas openpyxl python-docx
```

## Jak korzystać z programu

1. Przygotuj plik Excel z danymi pracowników (domyślnie: "Nadgodziny_nieobecności_pracownicy.xlsx")
2. Przygotuj szablon umowy w formacie .docx (domyślnie: "UMOWA O PRACĘ NA OKRES PRÓBNY.docx")
3. Uruchom skrypt generatora:

```
python generator_umow.py
```

lub skrypt konfigurowalny:

```
python generator_umow_konfig.py
```

4. Wygenerowane umowy znajdziesz w katalogu "Wygenerowane_umowy"

## Struktura danych w Excelu

Program oczekuje określonej struktury danych w arkuszu "pracownicy":

- Pierwsza kolumna powinna zawierać nazwy pól (np. "data urodzenia", "stanowisko")
- Pozostałe kolumny to dane poszczególnych pracowników
- Miejsca do uzupełnienia w szablonie umowy powinny być oznaczone nawiasami kwadratowymi [...]

## Pliki w projekcie

- `generator_umow.py` - główny skrypt generujący umowy
- `generator_umow_konfig.py` - wersja skryptu z możliwością konfiguracji przez użytkownika
- `analiza_plikow.py` - skrypt do analizy struktury plików Excel i Word
- `analiza_dokumentu.py` - skrypt do szczegółowej analizy dokumentu Word
