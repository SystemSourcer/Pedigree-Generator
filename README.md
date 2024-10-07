# Nutztier-Pedigree-Generator

Willkommen zum Nutztier-Pedigree-Generator! Dieses Projekt bietet ein Werkzeug zur Erstellung und Verwaltung von Stammbäumen für Nutztiere wie Rinder und Schafe. 

## Funktionen

- **Erstellen von Pedigrees:** Erstelle und speichere Stammbäume auf Basis von CSV-Files.
- **Datenimport/-export:** Importiere Daten im CSV-Format und exportiere generierte Pedigrees als PDF oder Bilddateien.
- **Datenanalyse:** Biete einfache Analysewerkzeuge, um Inzuchtkoeffizienten und Verwandtschaftsgrade zu berechnen. (für die Zukunft geplant) 

## Installation

1. **Repository klonen**
   ```bash
   git clone https://github.com/DeinBenutzername/Nutztier-Pedigree-Generator.git
   cd Nutztier-Pedigree-Generator
   ```

  

2. **Abhängigkeiten installieren (automatisch)**
   -Bisher noch nicht implementiert

3. **Abhängigkeiten installieren (manuell)**
   - Stelle sicher, dass Python 3.12 installiert ist oder installieren sie es z.B. mit winegt:
   ```bash
   winget install -e --id Python.Python.3.12 --scope machine
   ```
   - Installiere die notwendigen Python-Pakete:
   ```bash
   pip install -r requirements.txt
   ```

## Verwendung

1. **Starten der Anwendung durch Klicken oder über die Komandozeile / Powershell mit:**
   ```bash
   python pedigree.py
   ```

2. Navigieren im sich öffnenden Fnester zum CSV-File, der als Datengrunlage für das Pedigree dienen soll.
3. Geben sie den Namen des Tieres ein, dessen Pedigree erzeugt werdem soll.
4. Geben sie an über wie viele Generationen das Pedigree erzeugt werden soll.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe die [LICENSE](LICENSE) Datei für Details.

## Kontakt

Bei Fragen oder Anregungen kannst du uns unter [simon@galloway-mielke.de](mailto:simon@galloway-mielke.de) erreichen.
