import os 
import shutil
import fnmatch
import ctypes
import mutagen

from tkinter import *
from tkinter import filedialog
from app.models.Music import *
from mutagen.mp3 import MP3

import pygame
from pygame import mixer

#Classe permettant la gestion des musiques dans la librairie
class Library :
    #Composé d'éléments Tracks
    playlists = []

    music_list = []
    
    def __init__(self):
        self.init_music_list()


    global path
    path ="ressources\\songs"
    
    def create_music_by_name(self, name):
        audio = MP3(path+"\\"+name)
        audio_info = audio.info
        duration = int(audio_info.length)
        music = Music(name.replace(".mp3", "") , duration)
        return music
    
    def init_music_list(self):
        pattern = "*.mp3" 
        music_list = []
        for root, dirs, files, in os.walk(path): #music
            for filename in fnmatch.filter(files, pattern): 
                music=self.create_music_by_name(filename)
                music_list.append(music)
        self.music_list = music_list

    def get_music_list(self):
        return self.music_list


    #Methode d'import de fichier mp3 
    def import_music(self, music_space):
        #Ouvrir la fenêtre de dialogue pour importer des fichier .mp3
        songs=filedialog.askopenfilenames(initialdir="songs/",title="Importer fichier audio", filetypes=(("mp3 Files","*.mp3"),))
        #Parcourir la selection
        for song in songs: 
            #Ne regarder que le nom de la musique
            song_rename = song.replace("C:/Users/bapti/Music/","") #Changer avec un split
            #Si elle a déjà été importé : Empêcher le re-import et afficher une popin
            if(os.path.exists(path+"/"+ song_rename)):
                ctypes.windll.user32.MessageBoxW(0, song_rename+" a déjà été importé", "Attention", 1)
            #Si non, on l'ajoute à l'interface et dans le dossier
            else:
                shutil.copy(song, path)       
                song = song.replace("C:/Users/bapti/Music/","")       
                music = self.create_music_by_name(song)
                music_space.insert(END,music.get_title())
                