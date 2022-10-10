from fileinput import filename
from tkinter import *
from app.models.Library import *

from tkinter import filedialog
import pygame
from pygame import mixer
#Modèle représentant une musique et ses attributs
class Music :
    
    
    def play_music(music_path, music_space, space):
        space.config(text=music_space.get("anchor"))
        mixer.music.load(music_path + "\\" + music_space.get("anchor") + ".mp3")
        mixer.music.play()
        
    
    def prev_music(music_path, music_space, space): 
        prev_song = music_space.curselection()
        prev_song = prev_song[0]-1
        prev_song_name = music_space.get(prev_song)
        space.config(text= prev_song_name)
        mixer.music.load(music_path + "\\" + prev_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(prev_song)
        music_space.select_set(prev_song)
    
    def next_music(music_path, music_space, space):
        next_song = music_space.curselection()
        next_song = next_song[0]+1
        next_song_name = music_space.get(next_song)
        space.config(text= next_song_name)
        mixer.music.load(music_path + "\\" + next_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(next_song)
        music_space.select_set(next_song)
    
    
    def pause_music(pause_button):
        if(pause_button["text"]== "pause"):
            mixer.music.pause()
            pause_button["text"] = "play"
        else:
            mixer.music.unpause()
            pause_button["text"]= "pause"
            
    
    def stop_music(music_space):
        mixer.music.stop()
        music_space.select_clear('active')
          