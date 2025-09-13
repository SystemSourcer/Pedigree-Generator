# Nutztier-Pedigree-Generator

Willkommen zum Nutztier-Pedigree-Generator!  
Dieses Projekt bietet ein Werkzeug zur Erstellung und Verwaltung von Stammbäumen für Nutztiere wie Rinder und Schafe. 

## Funktionen

- **Erstellen von Pedigrees:** Erstelle und speichere Stammbäume auf Basis von CSV-Files. Unterstützt dabbei bis zu drei Generationen.
- **Datenimport/-export:** Importiere Daten im CSV-Format und exportiere generierte Pedigrees als Dokumente (PDF) oder Bilddateien (PNG).
- **Datenanalyse:** Biete einfache Analysewerkzeuge. Aktuell die Berechnung des Inzuchtkoeffizienten mit der exakten Methode nach [Wright](https://de.wikipedia.org/wiki/Inzuchtkoeffizient#Exakte_Methode_nach_Wright).  Weitere Tools sind geplant...

## Installation

1. **Repository klonen**
   - Klonen sie die Repositoty oder downloaden sie diese als .zip-File (wenn als zip, dann daach entpacken).
   ```bash
   git clone https://github.com/SystemSourcer/Pedigree-Generator.git
   
   ```
3. **Abhängigkeiten installieren**
   - Stellen sie sicher, dass Python installiert ist oder installieren sie es z.B. mit winget (getestet mit Python 3.12). Öffnen sie dazu die Powershell und führen sie folenden Befehl aus:
   ```bash
   winget install -e --id Python.Python.3.12 --scope machine --accept-package-agreements --accept-source-agreements
   ```
   - Gehen sie im in denheruntergeladenen ider entpackten Ordner. Installieren sie die notwendigen Python-Pakete:
   ```bash
   cd Pedigree-Generator
   pip install -r requirements.txt
   ```

## Datenbank
1. **CSV:**  
  Die Datenbak muss als CSV-Flie mit Semikolon (;) als Trennzeien bereitgestellt werden.  
  Dieser lässt sich ohne Probleme aus Excel, Libreoffice oder ähnlichen Programmen exportieren.  
  Der Name der Datei ist dabei egal.
2. **Beispieldatei:**  
  Die Datei "example.csv" ist eine Beispieldatei, die zum Testen den Programms und zur Veranschaulichung der geforderten Datenstruktur dienen soll. 
3. **Regeln:**  
   Folgende Regeln sind in der Datenbank einzuhalten, damit das Programm funktioniert:
      1. Die ersten 6 Spalten müssen wie im Beispiel Name, Titel des Betriebs, Ohrmarkennummer, Geburtsdatum, die Bewertung und die Farbe enthalten.
      2. Die Namen der ersten 6 Spalten sollten exaxt un in ind dieser Reichhenfolge wie filgt lauten: **Name;Titel;LOM;Geb;Bewertung;Farbe;**
      3. Fehlt ein Eintrag in Spalte 2-6, ensteht daraus kein Fehler und das Pedigree wird ohne die fehlenden Informationen erstellt.
      4. Die Spalten "Vater" und "Mutter" müssen enthalten sein und auch genau so heißen. Es ist aber egal wo sie sich ab Spalte 7 befinden.
      5. Es können ab Spalte 7 beliebig viele weitere Spalten enthalten sein, die nicht die Bezeichung "Vater" oder "Mutter" haben.
      6. Der Name in den Spalten "Vater" oder "Mutter" muss mit dem Namen in der ersten Spalte der Zeile des entsprechenden Vater- oder Muttertiers exakt übereinstimmen (inklusive Leerzeichen vor und nach dem Name).

## Verwendung

1. **Starten der Anwendung durch Klicken oder über die Kommandozeile / Powershell mit:**
   ```bash
   python pedigree.py
   ```

2. Navigieren Sie im sich öffnenden Fenster zum CSV-File, der als Datengrunlage für das Pedigree dienen soll.
3. Geben sie ein ob sie ein Pedigree (PG) oder einen Inzuchtkoeffizienten bberechnen wollen (IK)
4. Geben sie den Namen des Tieres ein, dessen Pedigree erzeugt werdem soll.
5. Geben sie an über wie viele Generationen das Pedigree erzeugt werden soll.
6. Geben sie die Namen der Elterntiere ein wen sie den IK für deren Nachkommen berechhnen wollen.

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz. Siehe die [LICENSE](LICENSE) Datei für Details.

## Kontakt

Bei Fragen oder Anregungen kannst du in Githubb in die Issues schauen, selbst ein Issue erstellen oder uns eine [Mail](mailto:simon@galloway-mielke.de) erreschreiben.
