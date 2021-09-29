import os
from tkinter import *
from PIL import ImageTk,Image
import tkFileDialog

class Program:

    def __init__(self):
        self._srcFolder = ""
        self._destFolder = ""
        self._fenetre = Tk()
        self.frame = Frame(self._fenetre)
        self.create_widgets()
        self.frame.pack(expand=YES,side=LEFT)
        self.dicimg = {}
        self.listeFichier = []
    def create_widgets(self):
        self.create_source_dossier_button()
        self.create_tourner_a_droite_button()

    def create_source_dossier_button(self):
        yt_button = Button(self.frame, text="Choisir un dossier",command=self.choisirUnDossier)
        yt_button.pack(pady=25, fill=X)

    def create_tourner_a_droite_button(self):
        yt_buttonDroite = Button(self.frame,text='Tourner a droite',command=lambda: self.tournerImageDroite(self._srcFolder,self.listeFichier))
        yt_buttonDroite.pack(pady=25, fill=X)

    def choisirUnDossier(self):
        self._srcFolder = tkFileDialog.askdirectory(parent=self._fenetre,initialdir="/user",title='Please select a directory')
        self.listeFichier = os.listdir(self._srcFolder)
        self.afficherLesImages(self._srcFolder,os.listdir(self._srcFolder))

    def afficherLesImages(self,src,listeFichier):
        p = 0
        for i in listeFichier: 
            v = locals()
            img = src+"/"+i
            image = Image.open(img)
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.dicimg[p] = photo
            v["cadre%d" % p]=Canvas(self.frame,width=200,height=200,bg="white")
            v["cadre%d" % p].create_image(0,0,anchor=NW,image =photo)
            v["cadre%d" % p].pack()
            p = p +1
    
    def tournerImageDroite(self,scr,listeFichier):

        for i in listeFichier:
            img = scr+"/"+i
            image = Image.open(img) 
            image.rotate(45)
        
        self.afficherLesImages(scr,listeFichier)