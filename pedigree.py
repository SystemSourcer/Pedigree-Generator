# Imports
import sys # 
import numpy as np # 
import pandas as pd # 
import tkinter as tk # 
from pathlib import Path # 
from tkinter import filedialog # 
from tkinter import messagebox # 
import matplotlib.pyplot as plt # 
from tkinter import simpledialog # 
# Functions
def main(): # 
    '''
    The main function.
    Asks the user for the Task.
    '''
    csv_path = Path(filedialog.askopenfilename(title='CSV-Datei als Datensatz auswählen', filetypes=[('CSV files', '*.csv')])) # CSV - File über GUI abfragen
    pg = PedGen(csv_path) # 
    task = simpledialog.askstring('Anwendung','Geben sie "PG" ein um ein Pedigree zu generieren oder "IK" um einen Inzuchtkoeffizient zu berechnen.')
    if task not in ('PG', 'IK'): 
        messagebox.showerror('Fehler', f'Bitte geben Sie PG ode IK ein. Ihre eingabe wahr {task}.') # 
        sys.exit() # 

    elif task == 'PG':
        ind, gen, ik, ped = pg.generate_pedigree() # 
        pg.plot_pedigree(ind, gen, ik, ped) # 
    
    else: print(f'IK = {pg.calc_full_inbreed()}')

# Objects
class PedGen(): # 
    '''
    The Pedigree-Generator object class.
    So to speak, the Gerneratir itself.
    '''
    def __init__(self, csv_path): # 
        '''
        Initializes the generator. 
        Loads the csv file into a DataFrame and fills gaps with empty strings.
        '''
        self.csv_path = Path(csv_path) # 
        self.df = pd.read_csv(self.csv_path, sep=';') # CSV - Fle einelsen
        self.df = self.df.fillna(' ') # Leere Felder mit leerem String füllen

    def df_to_string(self, elter, ngen, gen): # Funktion um Datenbankwerte in String umzuwandeln
        '''
        Convert the data frame content into corresponding strings depending on the number of generations.
        '''
        if ngen == 3 and gen == 1: # Ausnahme wenn über 3 generationen und aktuell in 1. Generation
            return f'{self.df.values[elter][0][0]} {str(self.df.values[elter][0][1])} {'\n' * 2} {self.df.values[elter][0][2]} {' ' * 3 } {'\n' * 2} Bew.: {self.df.values[elter][0][4]} {' ' * 3} Farbe: {self.df.values[elter][0][5]}' # 

        else: return f'{self.df.values[elter][0][0]}  {str(self.df.values[elter][0][1])} {'\n' * 2} {self.df.values[elter][0][2]} {' ' * 3} Bew.: {self.df.values[elter][0][4]}  {' ' * 3} Farbe: {self.df.values[elter][0][5]}' # 

    def generate_pedigree(self): # Struktur des Pedigree erstellen
        '''
        Generates the pedigree. 
        Requests the individual and the number of generations (supports 1, 2, or 3 generations). 
        Also uses the function to calculate the IK.
        '''
        ind = simpledialog.askstring('Tier','Name des Tiers für das ein Pedigree erstellt werden soll: ') # Tier für das Pedigree über GUI abfragen
        if not any(self.df.Name==ind): # Fehlermeldung wenn Tier nicht in Datenbank
            messagebox.showerror('Fehler', f'Tier "{ind}" nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') # 
            sys.exit() # 

        n_gen = simpledialog.askinteger('Anzahl','Geben sie an wie viele Generationen das Pedigree beinhalten soll (1/2/3): ') # Anzahl der zu erstellenden Generationen über GUI abfragen
        if not any(num==n_gen for num in {1,2,3}): # 
            messagebox.showerror('Fehler', f'Bitte gebben sie als Anzahl der Generationen "1", "2" oder "3" ein. Ihre Eingabe war {n_gen}.') # 
            sys.exit() # 

        print(f'\033[36mPedigree von {ind} wird über {n_gen} Generationen generiert.\033[0m')
        ped = pd.DataFrame() # Leeres Dateframe erstellen
        nk_list = [ind] # Nachkommeliste mit anfäglichem Individuum inizialisieren
        gen_str_list = ['V.','M.','V.V.','V.M.','M.V.','M.M.','V.V.V.','V.V.M.','V.M.V.','V.M.M.','M.V.V.','M.V.M.','M.M.V.','M.M.M.'] # Strings für die Einszelnen Generationen an Väetrn und Müttern
        ik = 0
        for gen in range(1,n_gen+1): #Für jede Genreartion...
            gen_list = [] # 
            v_m_list = [] # 
            for i in nk_list: # Für jedes Tier in der Nachkommenliste
                vater = self.df.Name == self.df[self.df.Name == str(i)].Vater.values[0] # Welcher eintrag im df enthält den Vater
                if any(vater): v_m_list.append(self.df.Name[vater].values[0]) # Name des Vaters in Vater - Mutter Liste hinzufügen
                else: # Fehlermeldung wenn kein Vater gefunden
                    messagebox.showerror('Fehler', f'Vater von {i} nicht gefunden. Es werden nur {gen-1} Generationen generiert. Bitte Datensatz überpüfen.') # 
                    print(f'\033[33mVater von {i} nicht gefunden. Es werden nur {gen-1} Generationen generiert. Bitte Datensatz überpüfen.\033[0m')
                    return ind, gen - 1, ik, ped # Rückgabe aktuelles Pedigree und aktualiserter Genrationenanzahl

                mutter = self.df.Name == self.df[self.df.Name == str(i)].Mutter.values[0] # Welcher Eintrag im df enthält die Mutter
                if any(mutter): v_m_list.append(self.df.Name[mutter].values[0]) # Name der Mutter in Vater - Mutter Liste hinzufügen
                else:# Fehlermeldung wenn keine Mutter gefunden
                    messagebox.showerror('Fehler', f'Mutter von {i} nicht gefunden. Es werden nur {gen-1} Generationen generiert. Bitte Datensatz überpüfen.') # 
                    print(f'\033[33mMutter von {i} nicht gefunden. Es werden nur {gen-1} Generationen generiert. Bitte Datensatz überpüfen.\033[0m')
                    return ind, gen - 1, ik, ped #Rückgabe aktuelles Pedigree und aktualiserter Genrationenanzahl

                gen_list.append('$\\bf{'+gen_str_list.pop(0)+'}$'+' '+self.df_to_string(vater,n_gen,gen)) # 
                for y in range(int((2**n_gen-2**gen)/(2**(gen-1)))): # damit index passt / immer gleich
                    gen_list.append(None) # 

                gen_list.append('$\\bf{'+gen_str_list.pop(0)+'}$'+' '+self.df_to_string(mutter,n_gen,gen)) # 

            if gen == 1: ik = self.calc_inbreed(self.df.Name[vater].values[0], self.df.Name[mutter].values[0])

            nk_list.clear() # Nachkommenliste leeren
            nk_list = v_m_list # Nachkomenliste mit nächster Genreration füllen.
            ped['Generation ' + str(gen)] = gen_list # 

        return ind, gen, ik , ped # 

    def plot_pedigree(self, ind, gen, ik, ped): # Figur mit supplots erstellen (jeder Plot eine generation)
        '''
        Converts the pedigree into a format that is understandable and clear to the user. 
        The displayed plot can then be saved as a PDF or PNG file. 
        '''
        if gen == 0: # Fehlermeldung wenn erste Generation, undmait auch kein Pedigree ertsellt werden kann.
            messagebox.showerror('Fehler','Bereits die erste Generation konnte nicht vollstänig im Datensatz gefunden werden. Erstellung eines Pedigrees daher nicht möglich.') # 
            sys.exit() #

        print(f'\033[36m{gen} Generationen des Peigrees von {ind} werden geplottet.\033[0m')
        fig, ax = plt.subplots(1, gen, figsize=(16, 9)) # Eine Zeile, gen Spalten
        if gen == 1: ax = np.array([ax]) # ax in array wandeln wenn nur eine Gen
        for g in range(gen): # Für jede gen eine Spalte im Pedigree erzeugen
            table1 = ax[g].table(cellText=ped.iloc[:,g].values[ped.iloc[:,g].notna()].reshape(-1,1), cellLoc='center', loc='center') # 
            table1.auto_set_font_size(False) # 
            table1.set_fontsize(10*1.2**gen/(1.2**(g+1))) # Schriftgröße an Generationenanzahl anpassen
            table1.scale(1, 5*2**gen/(2**(g+1))) # Tabellengröße an Generationenanzahl anpassen
            ax[g].axis('off') # Axen ausblenden
            ax[g].set_title('Generation '+str(g+1)) # Titel für jede Spalte setzen

        # Abstand zwischen den Tabellen einstellen
        plt.subplots_adjust(wspace=0) # Hier wird der horizontal Abstand zwischen den Subplots eingestellt
        # Informationen des Individuums ausgeben.
        fig.suptitle(f'{ind} {self.df[self.df.Name==ind].Titel.values[0]};{8*' '}{self.df[self.df.Name==ind].LOM.values[0]}\ngeb.: {self.df[self.df.Name==ind].Geb.values[0]};{8*' '}Bew.: {self.df[self.df.Name==ind].Bewertung.values[0]};{8*' '}Farbe: {self.df[self.df.Name==ind].Farbe.values[0]};{8*' '}IK = {ik}', fontweight='bold', linespacing=2) # 
        # Anzeigen des Pedigrees
        plt.show() # 

    def calc_inbreed(self,elter1,elter2): # 
        '''
        Calculates the inbreeding coefficient (IK).         
        Calls itself recursively for this purpose.
        Used by the function to generate the pedigree. Can also be called separately by the calc_full_Inbreed function.
        '''
        if not any(self.df.Name==elter1): return 0  # 
        if not any(self.df.Name==elter2): return 0 #
        print(f'\033[36mIK wird für Nachkomme von {elter1} mit {elter2} berechnent.\033[0m') 
        elter1_anc_list = [{'Name':elter1, 'Num_Gen': 0}] # 
        elter2_anc_list = [{'Name':elter2, 'Num_Gen': 0}] # 
        for anc in elter1_anc_list: # 
            ind = anc['Name'] # 
            num_gen = anc['Num_Gen'] # 
            vater = self.df.Name == self.df[self.df.Name == str(ind)].Vater.values[0] # 
            if any(vater): elter1_anc_list.append({'Name':self.df.Name[vater].values[0], 'Num_Gen': num_gen+1}) # 
            mutter = self.df.Name == self.df[self.df.Name == str(ind)].Mutter.values[0] # 
            if any(mutter): elter1_anc_list.append({'Name':self.df.Name[mutter].values[0], 'Num_Gen': num_gen+1}) # 

        for anc in elter2_anc_list: # 
            ind = anc['Name'] # 
            num_gen = anc['Num_Gen'] # 
            vater = self.df.Name == self.df[self.df.Name == str(ind)].Vater.values[0] # 
            if any(vater): elter2_anc_list.append({'Name':self.df.Name[vater].values[0], 'Num_Gen': num_gen+1}) # 
            mutter = self.df.Name == self.df[self.df.Name == str(ind)].Mutter.values[0] # 
            if any(mutter): elter2_anc_list.append({'Name':self.df.Name[mutter].values[0], 'Num_Gen': num_gen+1}) # 
        
        common_anc_set = {d['Name'] for d in elter1_anc_list} & {d['Name'] for d in elter2_anc_list} # 
        if bool(common_anc_set): # 
            print(f'\033[33mGemeinsamen Vorfahren für {elter1} und {elter2} gefunden: {common_anc_set}\033[0m')
            anc_inbreed_list = [] # 
            for common_anc in common_anc_set: # 
                common_anc_vater = self.df.Name == self.df[self.df.Name == str(common_anc)].Vater.values[0] # 
                if any(common_anc_vater): common_anc_elter1 = self.df.Name[common_anc_vater].values[0] # 
                else: common_anc_elter1 = None # 
                common_anc_mutter = self.df.Name == self.df[self.df.Name == str(common_anc)].Mutter.values[0] # 
                if any(common_anc_mutter): common_anc_elter2 = self.df.Name[common_anc_mutter].values[0] # 
                else: common_anc_elter2 = None # 
                elter1_num_gen_list = [anc['Num_Gen'] for anc in elter1_anc_list if anc['Name'] == common_anc] # 
                elter2_num_gen_list = [anc['Num_Gen'] for anc in elter2_anc_list if anc['Name'] == common_anc] # 
                for n1 in elter1_num_gen_list: # 
                    for n2 in elter2_num_gen_list: # 
                        anc_inbreed_list.append(0.5**(n1+n2+1) * (1+self.calc_inbreed(common_anc_elter1,common_anc_elter2))) # 

            inbreed = sum(anc_inbreed_list) # 
            print(f'\033[33mInzuchtkoefizient für Nachkomme aus {elter1} und {elter2} gefunden: {inbreed}\033[0m') # 
            return inbreed # 

        else: 
            print(f'\033[32mKeinen gemeinsamen Vorfahren für {elter1} und {elter2} gefunden.\033[0m')
            return 0 # 

    def calc_full_inbreed(self,): # 
        '''
        More or less a starter function to calculate the IK when it should be calculated separately without pedigree.
        '''
        elter1 = simpledialog.askstring('Elter 1','Name des ersten Elternteils für die Berechhnung des Inzuchtkoeffizienten: ') # 
        if not any(self.df.Name==elter1): # Fehlermeldung wenn Tier nicht in Datenbank
            messagebox.showerror('Fehler', f'Tier {elter1} nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') # 
            sys.exit() # 

        elter2 = simpledialog.askstring('Elter 2','Name des zweiten Elternteils für die Berechhnung des Inzuchtkoeffizienten: ') # 
        if not any(self.df.Name==elter2): # Fehlermeldung wenn Tier nicht in Datenbank
            messagebox.showerror('Fehler', f'Tier {elter2} nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') # 
            sys.exit() # 

        return self.calc_inbreed(elter1,elter2) # 

# Global
if __name__ == '__main__': # 
    main() # 
