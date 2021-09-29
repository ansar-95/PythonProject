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
    def create_widgets(self):
        self.create_source_dossier_button()

    def create_source_dossier_button(self):
        yt_button = Button(self.frame, text="Choisir un dossier",command=self.choisirUnDossier)
        yt_button.pack(pady=25, fill=X)

    def choisirUnDossier(self):
        self._srcFolder = tkFileDialog.askdirectory(parent=self._fenetre,initialdir="/user",title='Please select a directory')
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
        