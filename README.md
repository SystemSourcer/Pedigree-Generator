# Nutztier-Pedigree-Generator

Willkommen zum Nutztier-Pedigree-Generator!  
Dieses Projekt bietet ein Werkzeug zur Erstellung und Verwaltung von Stammbäumen für Nutztiere wie beispielsweise Rinder und Schafe. 

## Funktionen
- **Datenimport:** Öffnen einer Datenbank in Form eines csv-Files. 
- **Datenbank erstellen und bearbeiten:** Mit es kann eine neue Danbank erstellt und eine importiere Datenbank bearbeitet werden.
- **Erstellen von Pedigrees:** Erstellen und speichern von Stammbäume auf Basis von CSV-Files. Unterstützt dabei bis zu drei Generationen.
- **Datenanalyse:** Bietet einfache Analysewerkzeuge. Aktuell die Berechnung des Inzuchtkoeffizienten mit der exakten Methode nach [Wright](https://de.wikipedia.org/wiki/Inzuchtkoeffizient#Exakte_Methode_nach_Wright).  Weitere Tools sind geplant...

## Installation

1. **Repository klonen**
   - Klonen sie die Repositoty oder downloaden sie diese den pedigree.py und den requirements.txt file oder alles als .zip-File (wenn als zip, dann danch entpacken).
   ```bash
   git clone https://github.com/SystemSourcer/Pedigree-Generator.git
   ```
2. **Abhängigkeiten installieren**
   - Stellen sie sicher, dass Python installiert ist oder installieren sie es z.B. mit winget (getestet mit Python 3.12). Öffnen sie dazu die Powershell und führen sie folenden Befehl aus:
   ```bash
   winget install -e --id Python.Python.3.12 --scope machine --accept-package-agreements --accept-source-agreements
   ```
   - Gehen sie in den heruntergeladenen oder entpackten Ordner. Installieren sie die notwendigen Python-Pakete:
   ```bash
   cd Pedigree-Generator
   pip install -r requirements.txt
   ```

## Datenbank
1. **CSV:**  
  Die Datenbak muss als CSV-Flie mit Semikolon (;) als Trennzeien bereitgestellt werden.  
  Dieser lässt sich ohne Probleme aus Excel, Libreoffice oder ähnlichen Programmen exportieren.
  Wird die Datenbank mit dem Tool angelegt, wird automatisch das entsprechende Format und Trennzeichen gewählt (empfohlen).
  Der Name der Datei ist dabei nicht relevant.

2. **Beispieldatei:**  
  Die Datei "example.csv" ist eine Beispieldatei, die zum Testen den Programms und zur Veranschaulichung der geforderten Datenstruktur dienen soll.
 
3. **Regeln:**  
   Folgende Regeln sind in der Datenbank einzuhalten, damit das Programm funktioniert:
      1. Die ersten 7 Spalten müssen wie im Beispiel Name, Titel, LOM (Ohrmarkennummer), Geb (Geburtsdatum), die Bew (Bewertung), die Farbe und das (Gender) Geschlechtenthalten.
      2. Die Namen der ersten 7 Spalten sollten exakt un in ind dieser Reichhenfolge wie folgt lauten: **Name;Titel;LOM;Geb;Bew;Farbe;Gender**
      3. Fehlt ein Eintrag in Spalte 2-6, ensteht daraus kein Fehler und das Pedigree wird ohne die fehlenden Informationen erstellt (Ausnahme siehe 5.).
      4. Die Spalten 8 und 9 sollten "Vater" und "Mutter" heißen und müssen enthalten sein.
      5. Der Name in den Spalten "Vater" oder "Mutter" muss mit dem Namen in der ersten und dem Titel in der zweiten Spalte der Zeile des entsprechenden Vater- oder Muttertiers exakt übereinstimmen (inklusive Leerzeichen vor dem Titel und nach dem Name).

## Verwendung

1. **Starten der Anwendung durch Klicken oder über die Kommandozeile / Powershell mit:**
   ```bash
   python pedigree.py
   ```

2. >Es öffnet sich dann das Hauptfenster der Anwendung.
3. Als nächstes mus entweder ein bestehender csv-File geöffnet (Button öffnen) oder ein neuer erstellt werden (File --> Neue Datenbank erstellen).
4. Nun kann optional die Datenbank angezeigt oder bearbeitet werden. 
5. Erst beim drücken des Speicher-Buttons werden die Änderungen der geöffnetetn Datenbank auch im entsprechenden csf.-File gespeichert. 
6. Um ein Pedigree zu erstellen, geben sie den Namen des Tiers und die Anzahl an Generationen ein. Dann klicken sie auf "Erstellen".
7. Um den Inzuchtkoeffizient einer möglichen Anparung zu berechen, geben sie die Namen der zwei Elterntiere ein. Dann kilcken sie auf "Berechnen".

## Lizenz

Dieses Projekt steht unter der LRU-License (limited right of use). Siehe die [LICENSE](LICENSE) Datei für Details.

## Kontakt

Aktuell besteht kein ausgewiesener Suppor oder Kontakt jeglicher Art.
