import os
from tkinter import *
from PIL import ImageTk,Image
from tkinter import filedialog
=======
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
        self._largeur = IntVar() 
        self._longeur = IntVar() 
        self.canvas = Canvas(self.frame,width=1000,height=1000,bg="white")

    def create_widgets(self):
        self.create_source_dossier_button()
        self.create_tourner_a_droite_button()

        self.renomerToutImages()
        
        self.create_tourner_a_gauche_button()

        #self.create_input_largeur()
        #self.create_input_longueur()
        self.create_redimmension_Composant()
    def create_source_dossier_button(self):
        yt_button = Button(self.frame, text="Choisir un dossier",command=self.choisirUnDossier)
        yt_button.pack(pady=25, fill=X)

    def create_tourner_a_droite_button(self):
        yt_buttonDroite = Button(self.frame,text='Tourner a droite',command=lambda: self.tournerImageDroite(self._srcFolder,self.listeFichier,self._objetCanvas,self._objetCreateImage))
        yt_buttonDroite.pack(pady=25, fill=X)

    def create_tourner_a_gauche_button(self):
        yt_buttonGauche = Button(self.frame,text='Tourner a gauche',command=lambda: self.tournerImageGauche(self._srcFolder,self.listeFichier,self._objetCanvas,self._objetCreateImage))
        yt_buttonGauche.pack(pady=30, fill=X)
    
    def create_redimmension_Composant(self):
        largeur = IntVar() 
        largeur.set(0)
        entree = Entry(self.frame, textvariable=largeur, width=30)
        entree.pack()

        longueur = IntVar() 
        longueur.set(0)
        entree = Entry(self.frame, textvariable=longueur, width=30)
        entree.pack()

        redimensionner= Button(self.frame,text='Redimensionner',command=lambda: self.redimensionner(self._srcFolder,self.listeFichier,longueur.get(),largeur.get()))
        redimensionner.pack(pady=30, fill=X)



    def creerDictionnnaire(self,listeFichier):
        for i in range(len(listeFichier)):
            self._objetCanvas.append(listeFichier[i])

    def choisirUnDossier(self):
        self._srcFolder = filedialog.askdirectory(parent=self._fenetre,initialdir="/user",title='Please select a directory')
        self.listeFichier = os.listdir(self._srcFolder)
        self.afficherLesImages(self._srcFolder,os.listdir(self._srcFolder))
        self.creerDictionnnaire(self.listeFichier)



    def renomerToutImages(self):
        var = StringVar()
        yt_label_img = Button(self.frame, textvariable=var, relief=RAISED)
        var.set("Renommer les Images")
        yt_label_img.pack(pady=25, fill=X)
        self.renameImages()
    
    def renommerPetS(self):

        def changerleP():
            pr = pref.get()
            path = os.chdir("C:\\Users\\konaren\\Documents\\image")
            d=0
            for images in os.listdir(path):
                add_image_prefix = pr+"_""Image{}.png".format(d)
                os.rename(images , add_image_prefix)
                d = d+1
        
        def changerleS():
            sf = suf.get()
            path = os.chdir("C:\\Users\\konaren\\Documents\\image")
            d=0
            for images in os.listdir(path):
                add_image_suffix = "Image""_"+sf+"{}.png".format(d)
                os.rename(images , add_image_suffix)
                d = d+1
        

        p1 = Label(self.frame, text='Prefixe des images :')
        p1.pack(pady=0)
        pref = StringVar()
        entree1 = Entry(self.frame, textvariable =pref, width=15)
        entree1.pack(padx=0, pady=10)
        
        

        btn_preffix = Button(self.frame, text='Changer le prefixe' ,command=changerleP)
        btn_preffix.pack(padx=5, pady=20)



        p2 = Label(self.frame, text='Suffixe des images :')
        p2.pack(pady=0)
        suf = StringVar()
        entree2 = Entry(self.frame,textvariable =suf, width=15)
        entree2.pack(padx=0, pady=10)
       
        btn_suffixe = Button(self.frame, text='Changer le suffixe',command=changerleS)
        btn_suffixe.pack(padx=5, pady=5)
    

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
            
    

    def tournerImageDroite(self,src,listeFichier):

        for i in listeFichier:
            img = src+"/"+i
            image = Image.open(img) 
            image.rotate(45)
        
        self.afficherLesImages(src,listeFichier)


    def renameImages(self):
        path = os.chdir("C:\\Users\\konaren\\Documents\\image")
        p =0
        for image in os.listdir(path):
            new_image_name = "Image{}.png".format(p)
            os.rename(image , new_image_name)
            p = p+1

    def tournerImageDroite(self,scr,listeFichier,listeCanvas,listeObjetCanvas):

        for i in range(len(listeFichier)):
            self.traitementImage(scr,listeFichier,i,-90)
        self.canvas.delete("all")
        self.afficherLesImages(scr,listeFichier)


    def tournerImageGauche(self,scr,listeFichier,listeCanvas,listeObjetCanvas):

        for i in range(len(listeFichier)):
            self.traitementImage(scr,listeFichier,i,90)
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

    def redimensionner(self,scr,listeFichier,longueur,largeur):

        for i in range(len(listeFichier)):
            self.redimensionnerTraitement(scr,listeFichier,i,longueur,largeur)
        self.canvas.delete("all")
        self.afficherLesImages(scr,listeFichier)   
    
    def redimensionnerTraitement(self,scr,listeFichier,index,longueur,largeur):
        self._img = scr+"/"+listeFichier[index]
        self._image = Image.open(self._img)
        self._image = self._image.resize((longueur,largeur), Image.ANTIALIAS)
        self._image.save("image/"+listeFichier[index])
        self._photo = ImageTk.PhotoImage(self._image)
        #self.canvas.itemconfig(self._objetCreateImage[index],image=self._photo)
