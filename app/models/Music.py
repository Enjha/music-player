from fileinput import filename
from tkinter import *
from app.models.Library import *

from tkinter import filedialog
import pygame
from pygame import mixer

#Classe permettant la gestion des musiques lors de la lecture
class Music :
    title = ""
    duration = 0

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def get_title(self):
        return self.title
    
    def get_duration(self):
        return self.duration

    #Méthode permettant de jouer une musique
    def play_music(music_path, music_space, space):
        if (music_space.get("anchor") != ""):
            space.config(text=music_space.get("anchor"))
            song_name =music_space.get("anchor")
        else:
            music_space.select_set(0)
            space.config(text=music_space.get(0))
            song_name = music_space.get(0)
        mixer.music.load(music_path + "\\" + song_name + ".mp3")
        mixer.music.play()
        
    #Méthode permettant de jouer la musique précédente
    def prev_music(music_path, music_space, space): 
        prev_song = music_space.curselection()
        prev_song = prev_song[0]-1
        prev_song_name = music_space.get(prev_song)
        space.config(text= prev_song_name)
        if (prev_song_name == ""):
            music_space.select_set(music_space.size() - 1)
            prev_song = music_space.size() - 1
            prev_song_name = music_space.get(prev_song)
        mixer.music.load(music_path + "\\" + prev_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(prev_song)
        music_space.select_set(prev_song)
    
    #Méthode permettant de jouer la musique suivante
    def next_music(music_path, music_space, space):
        next_song = music_space.curselection()
        next_song = next_song[0]+1
        next_song_name = music_space.get(next_song)
        space.config(text= next_song_name)
        if (next_song_name == ""):
            music_space.select_set(0)
            next_song = 0
            next_song_name = music_space.get(next_song)
            space.config(text=next_song_name)
        mixer.music.load(music_path + "\\" + next_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(next_song)
        music_space.select_set(next_song)
    
    #Méthode permettant de mettre en pause la musique courante
    def pause_music(pause_button):
        if(pause_button["text"]== "pause"):
            mixer.music.pause()
            pause_button["text"] = "play"
        else:
            mixer.music.unpause()
            pause_button["text"]= "pause"
            
    #Méthode permettant d'arrêter la lecture d'une quelconque musique
    def stop_music(music_space):
        mixer.music.stop()
        music_space.select_clear('active')
          