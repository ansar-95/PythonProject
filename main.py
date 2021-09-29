# coding: utf-8
import os
from tkinter import * 
import tkFileDialog


fenetre = Tk()

fenetre.title("My application")


# # for ligne in range(10):
# #     for colonne in range(10):
# #         Button(fenetre, text='L%s-C%s' % (ligne, colonne), borderwidth=1).grid(row=ligne, column=colonne)
# Button(fenetre, text='Tourner à droite', borderwidth=1).grid(row=2, column=1)

# fenetre.mainloop()







def choisirUnDossier():
    return tkFileDialog.askdirectory(parent=fenetre,initialdir="/user",title='Please select a directory')

bouton=Button(fenetre, text="Choisir un dossier", command=choisirUnDossier)
bouton.pack()


fenetre.mainloop()



