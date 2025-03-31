import pdfplumber
import pandas as pd
from datetime import datetime
import re

def convert_time_to_hours(time_str):
    """Konwertuje czas w formacie HH:MM:SS na liczbę godzin"""
    try:
        if not time_str or pd.isna(time_str):
            return 0
        parts = time_str.split(':')
        hours = float(parts[0])
        minutes = float(parts[1]) if len(parts) > 1 else 0
        seconds = float(parts[2]) if len(parts) > 2 else 0
        return hours + minutes/60 + seconds/3600
    except Exception:
        return 0

def extract_time_report_data(pdf_path):
    """
    Ekstrahuje dane z raportu czasu pracy, szukając konkretnych wzorców.
    """
    data = {
        'nadgodziny': [],
        'nieobecnosci': []
    }
    
    with pdfplumber.open(pdf_path) as pdf:
        print(f"\nPrzetwarzanie pliku PDF: {pdf_path}")
        print(f"Liczba stron w PDF: {len(pdf.pages)}")
        
        for page_num, page in enumerate(pdf.pages, 1):
            print(f"\nPrzetwarzanie strony {page_num}")
            
            # Ekstrahuj tabele
            tables = page.extract_tables()
            
            # Ekstrahuj cały tekst strony
            text = page.extract_text()
            print(f"Tekst strony: {text[:200]}...")  # Pokaż pierwsze 200 znaków
            
            # Szukaj podsumowania nadgodzin
            overtime_pattern = r'OVERHOURS 50% ALL MONTH.*?(\d{2}:\d{2}:\d{2})'
            overtime_matches = re.finditer(overtime_pattern, text, re.DOTALL)
            for match in overtime_matches:
                overtime_hours = match.group(1)
                print(f"Znaleziono nadgodziny: {overtime_hours}")
                data['nadgodziny'].append({
                    'hours': convert_time_to_hours(overtime_hours)
                })
            
            # Przeanalizuj tabele szukając Care Allowance
            if tables:
                for table in tables:
                    if not table:
                        continue
                    for row in table:
                        if not row:
                            continue
                        # Sprawdź czy wiersz zawiera datę i Care Allowance
                        date_pattern = r'^\d{4}-\d{2}-\d{2}$'
                        for i, cell in enumerate(row):
                            if cell and isinstance(cell, str):
                                if 'Care Allowance' in cell:
                                    # Znajdź datę z tego wiersza
                                    date = None
                                    for date_cell in row:
                                        if date_cell and isinstance(date_cell, str) and re.match(date_pattern, date_cell):
                                            date = date_cell
                                            break
                                    if date:
                                        print(f"Znaleziono Care Allowance w dniu: {date}")
                                        data['nieobecnosci'].append({
                                            'date': date,
                                            'type': 'Care Allowance',
                                            'days': 1
                                        })
    
    print("\nPodsumowanie znalezionych danych:")
    print(f"Nadgodziny: {len(data['nadgodziny'])} rekordów")
    print(f"Nieobecności: {len(data['nieobecnosci'])} dni")
    return data

def update_excel_file(excel_path, data):
    """
    Aktualizuje plik Excel na podstawie znalezionych danych.
    """
    print("\nAktualizacja pliku Excel...")
    
    # Wczytaj plik Excel
    excel_file = pd.ExcelFile(excel_path)
    
    # Przygotuj DataFrames do zapisu
    df_nadgodziny = None
    df_nieobecnosci = None
    
    # Aktualizuj arkusz nadgodziny
    if 'nadgodziny' in excel_file.sheet_names and data['nadgodziny']:
        df_nadgodziny = pd.read_excel(excel_file, sheet_name='nadgodziny')
        print("\nAktualizacja nadgodzin:")
        
        # Weź pierwsze znalezione nadgodziny (zakładamy jeden rekord na miesiąc)
        overtime = data['nadgodziny'][0]
        
        # Znajdź wiersz dla pracownika (zakładamy, że jest tylko jeden)
        if len(df_nadgodziny) > 0:
            row_idx = 0  # Pierwszy wiersz
            print(f"Aktualizacja nadgodzin: {overtime['hours']} godzin")
            df_nadgodziny.at[row_idx, 'Ilość godzin'] = overtime['hours']
            df_nadgodziny.at[row_idx, 'Ilość - 50%'] = overtime['hours']
    
    # Aktualizuj arkusz nieobecności
    if 'nieobecności' in excel_file.sheet_names and data['nieobecnosci']:
        df_nieobecnosci = pd.read_excel(excel_file, sheet_name='nieobecności')
        print("\nAktualizacja nieobecności:")
        
        # Zlicz dni Care Allowance
        care_allowance_days = len(data['nieobecnosci'])
        
        # Znajdź wiersz dla pracownika (zakładamy, że jest tylko jeden)
        if len(df_nieobecnosci) > 0:
            row_idx = 0  # Pierwszy wiersz
            print(f"Aktualizacja dni opieki: {care_allowance_days} dni")
            df_nieobecnosci.at[row_idx, 'ilość dni opieki'] = care_allowance_days
    
    # Zapisz zmiany w pliku Excel
    with pd.ExcelWriter(excel_path, mode='a', if_sheet_exists='replace') as writer:
        if df_nadgodziny is not None:
            df_nadgodziny.to_excel(writer, sheet_name='nadgodziny', index=False)
        if df_nieobecnosci is not None:
            df_nieobecnosci.to_excel(writer, sheet_name='nieobecności', index=False)

def process_time_report(pdf_path, excel_path):
    """
    Przetwarza raport czasu pracy i aktualizuje plik Excel.
    """
    try:
        # Wczytaj dane z PDF
        data = extract_time_report_data(pdf_path)
        
        # Aktualizuj plik Excel
        update_excel_file(excel_path, data)
        
        print("\nPomyślnie przetworzono raport czasu pracy.")
    except Exception as e:
        print(f"\nWystąpił błąd podczas przetwarzania raportu: {e}")
        raise

if __name__ == "__main__":
    pdf_path = "Time Tracking Report.pdf"
    excel_path = "Nadgodziny_nieobecności_pracownicy.xlsx"
    
    process_time_report(pdf_path, excel_path) 