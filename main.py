from tkinter import *
import os
from tkinter import filedialog
from tkinter import messagebox

def clear():
    input.delete("1.0", "end")


def save():
     aa = filedialog.askopenfilename(initialdir="/", title='Fichiers')
     if os.path.exists(aa):
         with open(aa, "w") as file:
             file.write(input.get("1.0", "end-1c"))
             file.close()
             messagebox.askokcancel("Save", f"Sauvegarde reussite ! \n {aa}")

             
def open_file():
    aa = filedialog.askopenfilename(initialdir="/", title='Fichiers')
    if os.path.exists(aa):
        with open(aa, "r") as file:
            a = file.readlines()
            e = ""
            for i in a:
                e = e + i + "\n"
            input.delete("1.0", "end")
            input.insert("1.0", e)
            file.close()


editeur = Tk()

editeur.title("Formulo Bloc Note")
editeur.geometry("730x480")
editeur.minsize(480, 360)
editeur.config(background='#FFFFFF')
editeur.iconbitmap('font.ico')

frame = Frame(editeur, bg='#FFFFFF')

menu = Menu(editeur)

menu2 = Menu(menu, tearoff=0)
menu2.add_command(label="Enregistrer", command=save)
menu2.add_command(label="Ouvrir un fichier", command=open_file)
menu2.add_command(label="Tout Effacer", command=clear)
menu2.add_command(label="Quitter", command=editeur.quit)
menu.add_cascade(label="Fichier", menu=menu2)

editeur.config(menu=menu)

input = Text(editeur, font=("Trebuchet", 25), bg='#FFFFFF', fg='#000000')
input.pack()

frame.pack(expand=YES)

editeur.mainloop()
