from tkinter import *
from app.models.Library import *
from pygame import mixer

#Classe permettant la gestion des musiques lors de la lecture
class Music :
    
    # Chemin pour le fichier des musiques.
    global LIBRARY_PATH
    LIBRARY_PATH = "ressources\songs"

    title = "" # titre de la musiques
    duration = 0 # durée de la musiques

    # Constructeur
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    # Getter du titre, et de la durée de la musique
    def get_title(self):
        return self.title
    
    def get_duration(self):
        return self.duration

    # Méthode équals classique
    def equals(self, music):
        if self.title == music.get_title() and self.duration == music.get_duration():
            return True
        else:
            return False

    # Méthode permettant de jouer une musique
    def play_music(music_space, space):
        space.config(text=music_space.get("anchor"))
        mixer.music.load(LIBRARY_PATH + "\\" + music_space.get("anchor") + ".mp3")
        mixer.music.play()
        
    # Méthode permettant de jouer la musique précédente
    def prev_music(music_space, space): 
        prev_song = music_space.curselection()
        prev_song = prev_song[0]-1
        prev_song_name = music_space.get(prev_song)
        space.config(text= prev_song_name)
        mixer.music.load(LIBRARY_PATH + "\\" + prev_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(prev_song)
        music_space.select_set(prev_song)
    
    # Méthode permettant de jouer la musique suivante
    def next_music(music_space, space):
        next_song = music_space.curselection()
        next_song = next_song[0]+1
        next_song_name = music_space.get(next_song)
        space.config(text= next_song_name)
        mixer.music.load(LIBRARY_PATH + "\\" + next_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(next_song)
        music_space.select_set(next_song)
    
    # Méthode permettant de mettre en pause la musique courante
    def pause_music(pause_button):
        if(pause_button["text"]== "pause"):
            mixer.music.pause()
            pause_button["text"] = "play"
        else:
            mixer.music.unpause()
            pause_button["text"]= "pause"
            
    # Méthode permettant d'arrêter la lecture d'une quelconque musique
    def stop_music(music_space):
        mixer.music.stop()
        music_space.select_clear('active')
          