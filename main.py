from ast import main, pattern
from fileinput import filename
from importlib.resources import path
from multiprocessing.resource_sharer import stop
from struct import pack
from tkinter import *
import tkinter as tk
import os
import fnmatch
import pygame
from pygame import mixer
import time
#import vlc
from playsound import playsound
from pydub import AudioSegment
from pydub.playback import play

root = Tk()

root.title('GeeksforGeeks sound player')
 
root.geometry("500x400")
 
pygame.mixer.init()# initialise the pygame
 
def play():
    pygame.mixer.music.load("ressources\\songs\\Avicii - The Nights.mp3")
    pygame.mixer.music.play(loops=0)
 
title=Label(root,text="GeeksforGeeks",bd=9,relief=GROOVE,
            font=("times new roman",50,"bold"),bg="white",fg="green")
title.pack(side=TOP,fill=X)
 
play_button = Button(root, text="Play Song", font=("Helvetica", 32), command=play)
play_button.pack(pady=20)
root.mainloop()
"""
def main():
    
    pygame.init()
    window = tk.Tk()
    pygame.mixer.init()
    mixer.init()
    
    # Ajout d'un titre à la fenêtre principale :
    window.title("Spotizer")
    window.iconbitmap("ressources\\icons\\logo.ico")
    window.anchor(tk.CENTER)
    window.geometry("600x750")
    window.resizable(False,False)
    window.config(bg='#5DC863')

    window.maxsize(600,750)
    window.minsize(600,750)

    music_path = "ressources\\songs"
    pattern = "*.mp3"

    def play():
        space.config(text=music_space.get("anchor"))
        #mixer.music.load("ressources\\songs\\Avicii - The Nights.mp3")
        #vlc.MediaPlayer("ressources\\songs\\Avicii - The Nights.mp3").play()
        #mixer.music.load(music_path + "\\" + music_space.get("anchor"))
        #mixer.music.play()
        
        path = music_path + "\\" + music_space.get("anchor") + ".mp3"
        
        playsound(path) 
        
        
        #song = AudioSegment.from_mp3("ressources\\songs\\Avicii - The Nights.mp3")
        #print('playing sound using  pydub')
        #play(song)

 
    music_space = tk.Listbox(window, fg="black", bg="grey", width=100,font=('helvetica',18))
    music_space.pack(padx=18, pady=18)

    for root, dirs, files, in os.walk(music_path):
        for filename in fnmatch.filter(files, pattern):
            final_name = filename.strip('.mp3')
            music_space.insert('end', final_name)



    space = tk.Label(window, text="Boutons space",bg='#5DC863', fg='black', font=('poppin',22))
    space.pack(pady=15)
    
    buttons = tk.Frame(window, bg='grey')
    buttons.pack(padx=10, pady=5,anchor='center') 
    
    prev_icon = tk.PhotoImage(file="ressources\\icons\\prev.png")
    prev_button = tk.Button(window, text="prev", image=prev_icon, bg='grey',borderwidth=0)
    prev_button.pack(padx=8, pady=15, in_=buttons, side=tk.LEFT)
    
    stop_icon = tk.PhotoImage(file="ressources\\icons\\stop.png")
    stop_button = tk.Button(window, text="stop", image=stop_icon, bg='grey',borderwidth=0)
    stop_button.pack(padx=8, pady=15, in_=buttons,side=tk.LEFT)
    
    play_icon = tk.PhotoImage(file="ressources\\icons\\play.png")
    play_button = tk.Button(window, text="play", image=play_icon, bg='grey',borderwidth=0, command=play)
    play_button.pack(padx=8, pady=15, in_=buttons, side=tk.LEFT)
    
    pause_icon = tk.PhotoImage(file="ressources\\icons\\pause.png")
    pause_button = tk.Button(window, text="pause", image=pause_icon, bg='grey',borderwidth=0)
    pause_button.pack(padx=8, pady=15, in_=buttons,side=tk.LEFT)
    
    next_icon = tk.PhotoImage(file="ressources\\icons\\next.png")
    next_button = tk.Button(window, text="next", image=next_icon, bg='grey',borderwidth=0)
    next_button.pack(padx=8, pady=15, in_=buttons, side=tk.LEFT)


    space2 = tk.Label(window, text="nav space",bg='#5DC863', fg='black', font=('grey',22))
    space2.pack(pady=15)
    
    nav = tk.Frame(window, bg='white')
    nav.pack(padx=10, pady=5,anchor='center')
    # Affichage de la fenêtre créée :
    window.mainloop()

    print("Tout fonctionne correctement")


if __name__ == "__main__":
    main()
"""