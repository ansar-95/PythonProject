import os
from tkinter import *
from PIL import ImageTk,Image
import tkFileDialog
import time

#90 tourne limage a gauche
#-90 tourne limage a droite
#180 a lenvers
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
        self._objetCanvas = []
        self._objetCreateImage = []
        self._img = ""
        self._image = ""
        self._photo = ""
        self._button = []
        self.canvas = Canvas(self.frame,width=1000,height=1000,bg="white")
    def create_widgets(self):
        self.create_source_dossier_button()
        self.create_tourner_a_droite_button()

    def create_source_dossier_button(self):
        yt_button = Button(self.frame, text="Choisir un dossier",command=self.choisirUnDossier)
        yt_button.pack(pady=25, fill=X)

    def create_tourner_a_droite_button(self):
        yt_buttonDroite = Button(self.frame,text='Tourner a droite',command=lambda: self.tournerImageDroite(self._srcFolder,self.listeFichier,self._objetCanvas,self._objetCreateImage))
        yt_buttonDroite.pack(pady=25, fill=X)

    def creerDictionnnaire(self,listeFichier):
        for i in range(len(listeFichier)):
            self._objetCanvas.append(listeFichier[i])

    def choisirUnDossier(self):
        self._srcFolder = tkFileDialog.askdirectory(parent=self._fenetre,initialdir="/user",title='Please select a directory')
        self.listeFichier = os.listdir(self._srcFolder)
        self.afficherLesImages(self._srcFolder,os.listdir(self._srcFolder))
        self.creerDictionnnaire(self.listeFichier)



    def afficherLesImages(self,src,listeFichier):
        p = 0
        for i in listeFichier: 
            v = locals()
            img = src+"/"+i
            image = Image.open(img)
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            self.dicimg[p] = photo
            #self._objetCanvas.append(Canvas(self.frame,width=200,height=200,bg="white"))
            x = int((p+1)) *200
            image_on_cavas =  self.canvas.create_image(x,25,anchor=NW,image =photo)
            self._objetCreateImage.append(image_on_cavas)
            
            
            p = p +1
        self.canvas.pack()
            
    
    def tournerImageDroite(self,scr,listeFichier,listeCanvas,listeObjetCanvas):

        for i in range(len(listeFichier)):
            self.traitementImage(scr,listeFichier,i)
        
        self.canvas.delete("all")

        self.afficherLesImages(scr,listeFichier)



    def traitementImage(self,scr,listeFichier,index,degree):
        self._img = scr+"/"+listeFichier[index]
        self._image = Image.open(self._img) 
        self._image = self._image.rotate(-90)
        self._image.save("image/"+listeFichier[index])
        self._image = self._image.resize((200, 200), Image.ANTIALIAS)
        self._photo = ImageTk.PhotoImage(self._image)
        #self.canvas.itemconfig(self._objetCreateImage[index],image=self._photo)
        
        

  