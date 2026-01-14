# Imports
import sys # 
import numpy as np # 
import pandas as pd # 
import tkinter as tk # 
from pathlib import Path # 
from tkinter import ttk # 
from tkinter import filedialog # 
from tkinter import messagebox #
import matplotlib.pyplot as plt #  
# Functions
def main(): # 
    '''
    The main function.
    Starts the GUI and connects it to the backend
    '''
    hb = HerdBuch()
    pg = PedGen()
    gui = GUITools(hb,pg)

# Objects

class HerdBuch(): # 
    '''
    Docstring für HBEdit
    '''
    def __init__(self): # 
        '''
        Docstring für __init__
        '''
        self.csv_path = None
        self.df = pd.DataFrame()

    def open_csv(self,csv_path):
        self.csv_path = Path(csv_path) # 
        self.df = pd.read_csv(self.csv_path, sep=';') # CSV - Fle einelsen
        self.df = self.df.fillna('') # Leere Felder mit leerem String füllen
        self.df.insert(loc=8,column='NameTitel',value=(self.df.Name + ' ' + self.df.Titel).str.strip())

    def new_csv(self):
        self.df = pd.DataFrame({'Name':[''],'Titel':[''],'LOM':[''],'Geb':[''],'Bew':[''],'Farbe':[''],'Vater':[''],'Mutter':['']})
        self.df.insert(loc=8,column='NameTitel',value=(self.df.Name + ' ' + self.df.Titel).str.strip())

class PedGen(): # 
    '''
    The Pedigree-Generator object class.
    So to speak, the Gerneratir itself.
    '''
    def __init__(self): # 
        '''
        Initializes the generator. 
        Loads the csv file into a DataFrame and fills gaps with empty strings.
        '''
        self.csv_path = None
        self.df = pd.DataFrame()

    def df_to_string(self, elter, ngen, gen): # Funktion um Datenbankwerte in String umzuwandeln
        '''
        Convert the data frame content into corresponding strings depending on the number of generations.
        '''
        if ngen == 3 and gen == 1: # Ausnahme wenn über 3 generationen und aktuell in 1. Generation
            return f'{self.df.values[elter][0][0]} {str(self.df.values[elter][0][1])} {'\n' * 2} {self.df.values[elter][0][2]} {' ' * 3 } {'\n' * 2} Bew.: {self.df.values[elter][0][4]} {' ' * 3} Farbe: {self.df.values[elter][0][5]}' # 

        else: return f'{self.df.values[elter][0][0]}  {str(self.df.values[elter][0][1])} {'\n' * 2} {self.df.values[elter][0][2]} {' ' * 3} Bew.: {self.df.values[elter][0][4]}  {' ' * 3} Farbe: {self.df.values[elter][0][5]}' # 

    def generate_pedigree(self, ind, ngen): # Struktur des Pedigree erstellen
        '''
        Generates the pedigree. 
        Requests the individual and the number of generations (supports 1, 2, or 3 generations). 
        Also uses the function to calculate the IK.
        '''
        if not any(self.df.Name==ind): # Fehlermeldung wenn Tier nicht in Datenbank
            messagebox.showerror('Fehler', f'Tier "{ind}" nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') # 
            raise ValueError(f'Tier "{ind}" nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') # 

        if not any(num==ngen for num in {1,2,3}): # 
            messagebox.showerror('Fehler', f'Bitte gebben sie als Anzahl der Generationen "1", "2" oder "3" ein. Ihre Eingabe war {ngen}.') # 
            raise ValueError(f'Bitte gebben sie als Anzahl der Generationen "1", "2" oder "3" ein. Ihre Eingabe war {ngen}.') # 

        print(f'\033[36mPedigree von {ind} wird über {ngen} Generationen generiert.\033[0m')
        ped = pd.DataFrame() # Leeres Dateframe erstellen
        nk_list = [ind] # Nachkommeliste mit anfäglichem Individuum inizialisieren
        gen_str_list = ['V.','M.','V.V.','V.M.','M.V.','M.M.','V.V.V.','V.V.M.','V.M.V.','V.M.M.','M.V.V.','M.V.M.','M.M.V.','M.M.M.'] # Strings für die Einszelnen Generationen an Väetrn und Müttern
        ik = 0
        for gen in range(1,ngen+1): #Für jede Genreartion...
            gen_list = [] # 
            v_m_list = [] # 
            for i in nk_list: # Für jedes Tier in der Nachkommenliste
                vater = self.df.NameTitel == self.df[self.df.Name == str(i)].Vater.values[0] # Welcher eintrag im df enthält den Vater
                if any(vater): v_m_list.append(self.df.Name[vater].values[0]) # Name des Vaters in Vater - Mutter Liste hinzufügen
                else: # Fehlermeldung wenn kein Vater gefunden
                    messagebox.showerror('Fehler', f'Vater von {i} nicht gefunden. Es werden nur {gen-1} Generationen generiert. Bitte Datensatz überpüfen.') # 
                    print(f'\033[33mVater von {i} nicht gefunden. Es werden nur {gen-1} Generationen generiert. Bitte Datensatz überpüfen.\033[0m')
                    return gen - 1, ik, ped # Rückgabe aktuelles Pedigree und aktualiserter Genrationenanzahl

                mutter = self.df.NameTitel == self.df[self.df.Name == str(i)].Mutter.values[0] # Welcher Eintrag im df enthält die Mutter
                if any(mutter): v_m_list.append(self.df.Name[mutter].values[0]) # Name der Mutter in Vater - Mutter Liste hinzufügen
                else:# Fehlermeldung wenn keine Mutter gefunden
                    messagebox.showerror('Fehler', f'Mutter von {i} nicht gefunden. Es werden nur {gen-1} Generationen generiert. Bitte Datensatz überpüfen.') # 
                    print(f'\033[33mMutter von {i} nicht gefunden. Es werden nur {gen-1} Generationen generiert. Bitte Datensatz überpüfen.\033[0m')
                    return  gen - 1, ik, ped #Rückgabe aktuelles Pedigree und aktualiserter Genrationenanzahl

                gen_list.append('$\\bf{'+gen_str_list.pop(0)+'}$'+' '+self.df_to_string(vater,ngen,gen)) # 
                for y in range(int((2**ngen-2**gen)/(2**(gen-1)))): # damit index passt / immer gleich
                    gen_list.append(None) # 

                gen_list.append('$\\bf{'+gen_str_list.pop(0)+'}$'+' '+self.df_to_string(mutter,ngen,gen)) # 

            if gen == 1: ik = self.calc_inbreed(self.df.Name[vater].values[0], self.df.Name[mutter].values[0])

            nk_list.clear() # Nachkommenliste leeren
            nk_list = v_m_list # Nachkomenliste mit nächster Genreration füllen.
            ped['Generation ' + str(gen)] = gen_list # 

        return gen, ik , ped # 

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
        elter1_anc_list = [{'Name':elter1, 'Num_Gen':0, 'desc':set()}] # 
        elter2_anc_list = [{'Name':elter2, 'Num_Gen':0, 'desc':set()}] # 
        for anc in elter1_anc_list: # 
            ind = anc['Name'] # 
            num_gen = anc['Num_Gen'] #
            desc = anc['desc'].copy()
            desc.add(ind) # 
            vater = self.df.NameTitel == self.df[self.df.Name == str(ind)].Vater.values[0] # 
            if any(vater): elter1_anc_list.append({'Name':self.df.Name[vater].values[0], 'Num_Gen':num_gen+1, 'desc':desc}) # 
            mutter = self.df.NameTitel == self.df[self.df.Name == str(ind)].Mutter.values[0] # 
            if any(mutter): elter1_anc_list.append({'Name':self.df.Name[mutter].values[0], 'Num_Gen':num_gen+1, 'desc':desc}) # 

        for anc in elter2_anc_list: # 
            ind = anc['Name'] # 
            num_gen = anc['Num_Gen'] #
            desc = anc['desc'].copy()
            desc.add(ind) # 
            vater = self.df.NameTitel == self.df[self.df.Name == str(ind)].Vater.values[0] # 
            if any(vater): elter2_anc_list.append({'Name':self.df.Name[vater].values[0], 'Num_Gen':num_gen+1, 'desc':desc}) # 
            mutter = self.df.NameTitel == self.df[self.df.Name == str(ind)].Mutter.values[0] # 
            if any(mutter): elter2_anc_list.append({'Name':self.df.Name[mutter].values[0], 'Num_Gen':num_gen+1, 'desc':desc}) # 
        
        common_anc_set = {anc['Name'] for anc in elter1_anc_list} & {anc['Name'] for anc in elter2_anc_list} # 
        print(common_anc_set)
        print(elter1_anc_list)
        for anc in elter1_anc_list: # No matter which parent list, because in coman_anc_set only the intersection
            if anc['Name'] in common_anc_set and bool(anc['desc'] & common_anc_set): common_anc_set.remove(anc['Name']) # So that not all ancestors of duplicates are included, they will then appear in the next recursive call.

        if bool(common_anc_set): # 
            print(f'\033[33mGemeinsamen Vorfahren für {elter1} und {elter2} gefunden: {common_anc_set}\033[0m')
            anc_inbreed_list = [] # 
            for common_anc in common_anc_set: # 
                common_anc_vater = self.df.NameTitel == self.df[self.df.Name == str(common_anc)].Vater.values[0] # 
                if any(common_anc_vater): common_anc_elter1 = self.df.Name[common_anc_vater].values[0] # 
                else: common_anc_elter1 = None # 
                common_anc_mutter = self.df.NameTitel == self.df[self.df.Name == str(common_anc)].Mutter.values[0] # 
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

    def calc_full_inbreed(self,elter1,elter2): # 
        '''
        More or less a starter function to calculate the IK when it should be calculated separately without pedigree.
        '''
        #elter1 = simpledialog.askstring('Elter 1','Name des ersten Elternteils für die Berechhnung des Inzuchtkoeffizienten: ') # 
        if not any(self.df.Name==elter1): # Fehlermeldung wenn Tier nicht in Datenbank
            messagebox.showerror('Fehler', f'Tier {elter1} nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') # 
            raise ValueError(f'Tier {elter1} nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') 

        #elter2 = simpledialog.askstring('Elter 2','Name des zweiten Elternteils für die Berechhnung des Inzuchtkoeffizienten: ') # 
        if not any(self.df.Name==elter2): # Fehlermeldung wenn Tier nicht in Datenbank
            messagebox.showerror('Fehler', f'Tier {elter2} nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') # 
            raise ValueError(f'Tier {elter2} nicht in Datensatz vorhanden. Bitte Datensatz überprüfen.') 

        return self.calc_inbreed(elter1,elter2) # 

class GUITools(): # 
    '''
    Docstring für GUITools
    '''

    def __init__(self,hb,pg):
        '''
        Docstring für __init__
        '''

        self.hb = hb 
        self.pg = pg

        self.window = tk.Tk()
        self.window.title('Pedigree Generator')
        self.window.geometry('678x345') # Width x Height

        self.menu = tk.Menu(self.window)
        self.window.config(menu=self.menu)
        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='File', menu=self.filemenu)
        self.filemenu.add_command(label='Neue Datenbank erstellen', command=self.new_data)
        self.filemenu.add_command(label='Datenbank Öffnen', command=self.open_csv)
        self.filemenu.add_separator()
        self.filemenu.add_command(label='Beenden', command=self.window.quit)
        helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label='Help', menu=helpmenu)
        helpmenu.add_command(label='About')

        self.var_csv = tk.StringVar(value='Noch keine Datenbank geöffnet')
    
        ttk.Label(self.window, text='Datenbank:', font=('',12,'bold')).grid(row=0,column=0,columnspan=2, sticky='w', pady=25)
        ttk.Label(self.window, textvariable=self.var_csv).grid(row=0,column=2,columnspan=3,sticky='w')
        ttk.Button(self.window, text='Öffnen', command=self.open_csv).grid(row=1,column=0)
        ttk.Button(self.window, text='Anzeigen', command=self.show_data).grid(row=1,column=1)
        ttk.Button(self.window, text='Bearbeiten', command=self.edit_data).grid(row=1,column=2)
        
        ttk.Label(self.window, text='Pedigree:', font=('',12,'bold')).grid(row=2,column=0,columnspan=2, sticky='w', pady=25)
        ttk.Label(self.window, text='Name').grid(row=3,column=0)
        self.entry_name = ttk.Entry(self.window)
        self.entry_name.grid(row=3,column=1)
        ttk.Label(self.window, text='Gen').grid(row=3,column=2)
        self.sb_ngen = ttk.Spinbox(self.window,from_=1, to=3, state='readonly', justify='right', width=1)
        self.sb_ngen.set(3)
        self.sb_ngen.grid(row=3,column=3)
        ttk.Button(self.window, text='Erstellen', command=self.gen_ped).grid(row=3,column=4)

        ttk.Label(self.window, text='Inzuchtkoeffizient:', font=('',12,'bold')).grid(row=4,column=0, columnspan=2, sticky='w',pady=25)
        ttk.Label(self.window, text='Elter 1').grid(row=5,column=0)
        self.entry_elter1 = ttk.Entry(self.window)
        self.entry_elter1.grid(row=5,column=1,padx=20)
        ttk.Label(self.window, text='Elter 2').grid(row=5,column=2)
        self.entry_elter2 = ttk.Entry(self.window)
        self.entry_elter2.grid(row=5,column=3, padx=20)
        ttk.Button(self.window, text='Berechnen', command=self.calc_inb).grid(row=5,column=4)
        self.window.mainloop() 
    
    def open_csv(self):
        csv_path = Path(filedialog.askopenfilename(title='CSV-Datei als Datenbank auswählen', filetypes=[('CSV files', '*.csv')])) # CSV - File über GUI abfragen
        self.hb.open_csv(csv_path)
        self.var_csv.set(csv_path)


    def new_data(self):
        self.hb.new_csv()


    def sort_by_col(self, col, reverse=False):
        '''
        Sort Treeview by given column sortieren.
        '''
        daten = [(self.tree.set(k, col), k) for k in self.tree.get_children("")] # get all items + values in this col (value_in_coll, item_ID)

        
        try: daten.sort(key=lambda t: float(t[0]), reverse=reverse) # sort numerical 
        except ValueError: daten.sort(key=lambda t: t[0], reverse=reverse) # sort as string

        
        for index, (wert, k) in enumerate(daten): # reorder to sorted index
            self.tree.move(k, '', index)

        self.tree.heading(col,command=lambda: self.sort_by_col(col, not reverse)) # next clickshloud sort reverse

    def show_data(self):
        '''
        Docstring für show_data
        '''
        self.show_window = tk.Toplevel()
        self.show_window.title('Datenbank')

        self.show_frame = ttk.Frame(self.show_window)
        self.show_frame.pack(fill="both", expand=True)

        # Treeview
        self.tree = ttk.Treeview(self.show_frame, columns=list(self.hb.df.columns), show="headings")
        
        # Scrollbars
        scroll_y = ttk.Scrollbar(self.show_frame, orient="vertical", command=self.tree.yview)
        scroll_x = ttk.Scrollbar(self.show_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=scroll_y.set, xscrollcommand=scroll_x.set)
        
        # Spalten konfigurieren
        for col, width in zip(self.hb.df.columns,[100,150,250,200,100,100,100,250,250]):
            self.tree.heading(col, text=col, command=lambda c=col: self.sort_by_col(c, False))
            self.tree.column(col, anchor="center", width=width,stretch=False)

        # Daten einfügen
        for _, row in self.hb.df.iterrows():
            self.tree.insert("", "end", values=list(row))

        # Layout
        self.tree.grid(row=0, column=0, sticky="nsew")
        scroll_y.grid(row=0, column=1, sticky="ns")
        scroll_x.grid(row=1, column=0, sticky="ew")

        self.show_frame.rowconfigure(0, weight=1)
        self.show_frame.columnconfigure(0, weight=1)

    def edit_data(self):
        edit_window = tk.Toplevel()
        edit_window.title('Bearbeiten: ' + self.var_csv.get())
        
        edit_frame = ttk.Frame(edit_window)
        edit_frame.pack(fill="both", expand=True)

        ttk.Label(edit_frame, text='Tier:', font=('',12,'bold')).grid(row=0,column=0,columnspan=2, sticky='w', pady=25)
        cbox_name = ttk.Combobox(edit_frame, width=12, values=[''])
        cbox_name.set('Name')
        cbox_name.grid(row=1,column=0)
        cbox_titel = ttk.Combobox(edit_frame, width=18, values=[''])
        cbox_titel.set('Titel')
        cbox_titel.grid(row=1,column=1)
        cbox_lom = ttk.Combobox(edit_frame, width=20, values=[''])
        cbox_lom.set('LOM')
        cbox_lom.grid(row=1,column=2)
        cbox_geb = ttk.Combobox(edit_frame, width=15, values=[''])
        cbox_geb.set('Geb')
        cbox_geb.grid(row=1,column=3)
        cbox_bew = ttk.Combobox(edit_frame, width=5, values=[''])
        cbox_bew.set('Bew')
        cbox_bew.grid(row=1,column=4)
        cbox_farbe = ttk.Combobox(edit_frame, width=10, values=[''])
        cbox_farbe.set('Farbe')
        cbox_farbe.grid(row=1,column=5)
        cbox_vater = ttk.Combobox(edit_frame, width=30, values=[''])
        cbox_vater.set('Vater mit Titel')
        cbox_vater.grid(row=1,column=6)
        cbox_muter = ttk.Combobox(edit_frame, width=30, values=[''])
        cbox_muter.set('Mutter mit Titel')
        cbox_muter.grid(row=1,column=7)
   
    def gen_ped(self):
        ind = self.entry_name.get()
        ngen =int(self.sb_ngen.get()) # ngen = user input
        self.pg.df = self.hb.df
        gen, ik, ped = self.pg.generate_pedigree(ind,ngen) # gen = real found gen --> gen <= ngen
        self.pg.plot_pedigree(ind, gen, ik, ped) # 
   
    def calc_inb(self): 
        elter1 = self.entry_elter1.get()
        elter2 = self.entry_elter2.get()
        self.pg.df = self.hb.df
        ik = self.pg.calc_full_inbreed(elter1,elter2)
        print(f'IK = {ik}')
        messagebox.showinfo('IK', f'IK = {ik}')  
        
   

# Global
if __name__ == '__main__': # 
    main() # 
