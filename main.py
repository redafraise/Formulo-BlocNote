from tkinter import *
import os
import time
from tkinter import filedialog
from tkinter import messagebox
from tkinter import colorchooser
from tkinter import scrolledtext
from tkinter import font

infos = {'size': 12, 'font': 'Trebuchet'}

def clear():
    input.delete("1.0", "end")


def save():
     try:
         with open(infos['file'], "w") as file:
             file.write(input.get("1.0", "end-1c"))
             file.close()
             messagebox.askokcancel("Enregistrer", f"Sauvegarde reussite ! \n {infos['file']}")
             editeur.title("Formulo Bloc Note - {}".format(infos['file']))
     except:
         save_as()

def open_file():
    aa = filedialog.askopenfilename(initialdir="/", title='Ouvrir fichier')
    infos['file'] = aa
    if os.path.exists(aa):
        with open(aa, "r") as file:
            a = file.readlines()
            e = ""
            for i in a:
                e = e + i + "\n"
            input.delete("1.0", "end")
            input.insert("1.0", e)
            file.close()
    editeur.title("Formulo Bloc Note - {}".format(infos['file']))

def save_as():
    aa = filedialog.asksaveasfilename(initialdir="/", title='Enregistrer', defaultextension='.txt')
    try:
        with open(aa, "w") as file:
            file.write(input.get("1.0", "end-1c"))
            file.close()
            messagebox.askokcancel("Enregistrer", f"Sauvegarde reussite ! \n {aa}")
            infos['file'] = aa
        editeur.title("Formulo Bloc Note - {}".format(infos['file']))
    except:
        messagebox.showerror(title='Enregistrer', message='Echec de la sauvegarde')


def quitter():
    aa = messagebox.askyesno(title='Quitter', message='Etes vous sur de vouloir quitter ?')
    if aa:
        editeur.quit()

def annuler():
    input.edit_undo()

def selec():
    input.tag_add(SEL,"1.0", END)
    input.mark_set(0.0, END)

def bg_color():
    (rgb, hexadecimal) = colorchooser.askcolor()
    if hexadecimal:
        input.config(bg=hexadecimal)

def fg_color():
    (rgb, hexadecimal) = colorchooser.askcolor()
    if hexadecimal:
        input.config(fg=hexadecimal)

def size(taille):
    input.config(font=(infos['font'], taille))
    infos['size']=taille

def pol(police):
    input.config(font=(police, infos['size']))
    infos['font']=police

def a_propos():
    messagebox.showinfo(title='Formulo Bloc Note - A propos', message='Un bloc note très basique fait sous python par Formulaire \na l\'aide des librairies OS et TKINTER dans le but de pratiquer. \nDiscord: Formulaire.#1549\nGithub: https://github.com/formulaire\n\nPs: de prochains ajouts arrivent.')

def insert_time():
    ti = time.localtime()
    ti_ = f"{ti.tm_mday}/{ti.tm_mon}/{ti.tm_year} {ti.tm_hour}:{ti.tm_min}"
    input.insert(INSERT,ti_)

editeur = Tk()

editeur.title("Formulo Bloc Note")
editeur.geometry("730x480")
editeur.minsize(480, 360)
editeur.config(background='#FFFFFF')
editeur.iconbitmap('font.ico')

frame = Frame(editeur, bg='#FFFFFF')

menu = Menu(editeur)

fichier = Menu(menu, tearoff=0)
fichier.add_command(label="Ouvrir un fichier", command=open_file)
fichier.add_separator()
fichier.add_command(label="Enregistrer", command=save)
fichier.add_command(label="Enregistrer sous", command=save_as)
fichier.add_separator()
fichier.add_command(label="Quitter", command=quitter)
menu.add_cascade(label="Fichier", menu=fichier)

edition = Menu(menu, tearoff=0)
edition.add_command(label= "Annuler", command=annuler)
edition.add_separator()
edition.add_command(label="Tout Effacer", command=clear)
edition.add_command(label= "Tout selectionner", command=selec)
edition.add_separator()
edition.add_command(label='Insérer l\'heure et la date', command=insert_time)
menu.add_cascade(label="Edition", menu=edition)

taille = Menu(tearoff=0)
for i in range(10,37):
    taille.add_command(label=str(i), command=lambda taille=i: size(taille))

police = Menu(tearoff=0)
polices = font.families(editeur)
for i in polices:
    police.add_command(label=str(i), command=lambda police=i: pol(police))

format = Menu(menu, tearoff=0)
format.add_command(label="Couleur Arriere plan", command=bg_color)
format.add_command(label="Couleur Texte", command=fg_color)
format.add_separator()
format.add_cascade(label="Taille", menu=taille)
format.add_separator()
format.add_cascade(label='Police', menu=police)
menu.add_cascade(label="Format", menu=format)

aide = Menu(menu, tearoff=0)
aide.add_command(label="A propos", command=a_propos)
menu.add_cascade(label='Aide', menu=aide)

editeur.config(menu=menu)


input = scrolledtext.ScrolledText(editeur, font=("Terminal", 12), bg='#FFFFFF', fg='#000000', pady=2, padx=3, width=400, height=400, undo=True)
input.pack()

frame.pack(expand=YES)

editeur.mainloop()
