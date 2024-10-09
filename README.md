# Nutztier-Pedigree-Generator

Willkommen zum Nutztier-Pedigree-Generator! Dieses Projekt bietet ein Werkzeug zur Erstellung und Verwaltung von Stammbäumen für Nutztiere wie Rinder und Schafe. 

## Funktionen

- **Erstellen von Pedigrees:** Erstelle und speichere Stammbäume auf Basis von CSV-Files.
- **Datenimport/-export:** Importiere Daten im CSV-Format und exportiere generierte Pedigrees als PDF oder Bilddateien.
- **Datenanalyse:** Biete einfache Analysewerkzeuge, um Inzuchtkoeffizienten und Verwandtschaftsgrade zu berechnen. (für die Zukunft geplant) 

## Installation

1. **Repository klonen**
   - Clonen sie die Repositoty oder downloaden sie diese als .zip-File.
   ```bash
   git clone https://github.com/DeinBenutzername/Nutztier-Pedigree-Generator.git
   cd Nutztier-Pedigree-Generator
   ```
3. **Abhängigkeiten installieren**
   - Stellen sie sicher, dass Python installiert ist oder installieren sie es z.B. mit winegt (getestet mit Python 3.12). Öffnen sie dazu die Powershell und führen sie folenden Befehl aus:
   ```bash
   winget install -e --id Python.Python.3.12 --scope machine --accept-package-agreements --accept-source-agreements
   ```
   - Installiere die notwendigen Python-Pakete:
   ```bash
   pip install -r requirements.txt
   ```

## Datenbank
1. **CSV**
  Die Datenbak muss als CSV-Flie mit Semikolon (;) als Trennzeien bereitgestellt werden. Dieser lässt sich ohne Probleme aus Excel, Libreoffice oder ähnlichen Programmen exportieren. Der Name der Datei ist dabei egal.
2. **Beispieldatei**
  Die Datei "example.csv" ist eine Beispieldatei, die zum Testen den Programms und zur Veranschaulichung der geforderten Datenstruktur dienen soll. 
3. **Regeln**
   Folgende Regeln sind in der Datenbank einzuhalten, damit das Programm funktioniert:
      1. Die ersten 6 Spalten müssen wie im Beispiel Name, Titel des Betriebs, Ohrmarkennummer, Geburtsdatum, die Bewertung und die Farbe enthalten (in dieser Reihenfolge).
      2. Die Namen der ersten 6 Spalten sind frei wählbar.
      3. Fehlt ein Eintrag in Spalte 2-6, ensteht darasu kein Fehler und das Pedigree wird ohne die fehlenden Informationen erstellt.
      4. Die Spalten "Vater" und "Mutter" müssen enthalten sein und auch genau so heißen. Es ist aber egal wo sie sich ab Spalte 7 befinden.
      5. Es können ab Spalte 7 beliebig viele weitere Spalten enthalten sein, die nicht den Titel "Vater" oder "Mutter" haben.
      6. Der Name in den Spalten "Vater" oder "Mutter" muss mit dem Namen in der ersten Spalte der Zeile des entsprechenden Vater- oder Muttertiers exakt übereinstimmen (inklusive Leerzeichen vor und nach dem Name).

## Verwendung

1. **Starten der Anwendung durch Klicken oder über die Kommandozeile / Powershell mit:**
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
