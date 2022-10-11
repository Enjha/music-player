import os 
import shutil
import fnmatch
import ctypes


from tkinter import *
from tkinter import filedialog
import pygame
from pygame import mixer

#Classe permettant la gestion des musiques dans la librairie
class Library :
    #Methode d'import de fichier mp3 
    def import_music(music_path, music_space):
        #Ouvrir la fenêtre de dialogue pour importer des fichier .mp3
        songs=filedialog.askopenfilenames(initialdir="songs/",title="Importer fichier audio", filetypes=(("mp3 Files","*.mp3"),))
        #Parcourir la selection
        for song in songs: 
            #Ne regarder que le nom de la musique
            song_rename = song.replace("C:/Users/bapti/Music/","")
            #Si elle a déjà été importé : Empêcher le re-import et afficher une popin
            if(os.path.exists(music_path+"/"+ song_rename)):
                ctypes.windll.user32.MessageBoxW(0, song_rename+" a déjà été importé", "Attention", 1)
            #Si non, on l'ajoute à l'interface et dans le dossier
            else:
                shutil.copy(song, music_path)       
                song = song.replace("C:/Users/bapti/Music/","")         
                music_space.insert(END,song)