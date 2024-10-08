"""
Programmbeschriebung:
Programm zum erstellen eines Pedigrees anhand einer CSV-Datenbank.
"""
# Imports
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk

from tkinter import filedialog
from tkinter import simpledialog
from tkinter import messagebox
# Funktionen
def df_to_string(elter, ngen, gen): # Funktion um Datenbakwerte in String umzuwandeln
    if ngen == 3 and gen == 1: # Ausnahme wenn über 3 generationen und aktuell in 1. Generation
        return df.values[elter][0][0] + " " + str(df.values[elter][0][1])+ "\n"*2 + df.values[elter][0][2] + " "*3 + "\n"*2 +"Bew. " + df.values[elter][0][4] + " "*3 + "Farbe: " + df.values[elter][0][5]
    else:
        return df.values[elter][0][0] + " " + str(df.values[elter][0][1])+ "\n"*2 + df.values[elter][0][2] + " "*3 + "Bew. " + df.values[elter][0][4] + " "*3 + "Farbe: " + df.values[elter][0][5]

def generate_pedigree(ind, ngen): # Struktur des Pedigree erstellen
    
    pedigree = pd.DataFrame() #Leere Dateframe
    nklist = [ind] # Nachkommeliste mit anfäglichem Individuum
    verwandschaft = ["V.","M.","V.V.","V.M.","M.V.","M.M.","V.V.V.","V.V.M.","V.M.V.","V.M.M.","M.V.V.","M.V.M.","M.M.V.","M.M.M."] # Strings für die Einszelnen Generationen an Väetrn und Müttern
    
    for gen in range(1,ngen+1): #Für jede Genreartion...
        
        gen_list = []
        vater_mutter = []
        for i in nklist: # Für jedes Tier in der Nachkommenliste
            
            vater = df.Name == df[df.Name == str(i)].Vater.values[0] # Welcher eintrag im df enthält den Vater
            if any(vater):
                vater_mutter.append(df.Name[vater].values[0]) # Name des Vaters in Vater-Mutter-Liste hinzufügen
            else: # Fehlermeldung wenn kein Vater gefunden
                messagebox.showerror("Fehler", "Vater von " + i + " nicht gefunden. Es wird eine Generation weniger ausgegeben. Bitte Datensatz überpüfen." )
                return pedigree,gen-1 #Rückgabe aktuelles Pedigree und aktualiserter Genrationenanzahl

            mutter = df.Name == df[df.Name == str(i)].Mutter.values[0] # Welcher Eintrag im df enthält die Mutter
            if any(mutter):
                vater_mutter.append(df.Name[mutter].values[0]) # Name der Mutter in Vater-Mutter-Liste hinzufügen
            else:# Fehlermeldung wenn keine Mutter gefunden
                messagebox.showerror("Fehler", "Mutter von " + i + " nicht gefunden. Es wird eine Generation weniger ausgegeben. Bitte Datensatz überpüfen." )
                return pedigree,gen-1 #Rückgabe aktuelles Pedigree und aktualiserter Genrationenanzahl

            gen_list.append("$\\bf{" + verwandschaft.pop(0) + "}$" + "     " + df_to_string(vater,ngen,gen))
            for y in range(int((2**ngen-2**gen)/(2**(gen-1)))): # damit index passt / immer gleich
                gen_list.append(None)
            gen_list.append("$\\bf{" + verwandschaft.pop(0) + "}$" + "     " + df_to_string(mutter,ngen,gen))

        nklist.clear() # Nachkommenliste leeren
        nklist = vater_mutter  # Nachkomenliste mit nächster Genreration füllen.

        pedigree["Generation "+str(gen)] = gen_list
    
    return pedigree,gen # Rückgabe fertiges Pedigree und der ursprünglichen Genrationenanzahl (rein formal)
