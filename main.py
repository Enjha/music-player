from ast import main
from fileinput import filename
from tkinter import *
from app.models.Library import *
from app.models.Music import *

import os 
import shutil
import fnmatch
from tkinter import filedialog
import pygame
from pygame import mixer
import ctypes  # An included library with Python install.   


def main():
    
    window = Tk()
    pygame.mixer.init()
    
    # Ajout d'un titre à la fenêtre principale :
    window.title("Spotizer")
    window.iconbitmap("ressources\\icons\\logo.ico")
    window.anchor(CENTER)
    window.geometry("600x750")
    window.resizable(False,False)
    window.config(bg='#5DC863')
    window.maxsize(600,750)
    window.minsize(600,750)

    music_path = "ressources\\songs"
    pattern = "*.mp3" 

    music_space = Listbox(window, fg="black", bg="grey", width=100,font=('helvetica',18))
    music_space.pack(padx=18, pady=18)
          
    space = Label(window, text="Boutons space",bg='#5DC863', fg='black', font=('poppin',22))
    space.pack(pady=150)          

    import_button = Button(window, text="Importer des musiques", bg="grey", fg="black", command=lambda : Library.import_music(music_path, music_space))
    import_button.pack(pady=5, padx=25, side=RIGHT)
    
    #scroll_music = Scrollbar(window)
    #scroll_music.config(command=music_space.yview)
    #scroll_music.pack(side=RIGHT, fill=Y)

    for root, dirs, files, in os.walk(music_path):
        for filename in fnmatch.filter(files, pattern):
            final_name = filename.strip('.mp3')
            music_space.insert('end', final_name)

    
    buttons = Frame(window, bg='grey')
    buttons.pack(padx=10, pady=5,anchor='center') 
    
    prev_icon = PhotoImage(file="ressources\\icons\\prev.png")
    prev_button = Button(window, text="prev", image=prev_icon, bg='grey',borderwidth=0, command=lambda : Music.prev_music(music_path, music_space, space))
    prev_button.pack(padx=8, pady=10, in_=buttons, side=LEFT)
    
    stop_icon = PhotoImage(file="ressources\\icons\\stop.png")
    stop_button = Button(window, text="stop", image=stop_icon, bg='grey',borderwidth=0, command=lambda : Music.stop_music(music_space))
    stop_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
    
    play_icon = PhotoImage(file="ressources\\icons\\play.png")
    play_button = Button(window, text="play", image=play_icon, bg='grey',borderwidth=0, command=lambda : Music.play_music(music_path, music_space, space))
    play_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
    
    pause_icon = PhotoImage(file="ressources\\icons\\pause.png")
    pause_button = Button(window, text="pause", image=pause_icon, bg='grey',borderwidth=0, command=lambda : Music.pause_music(pause_button))
    pause_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
    
    next_icon = PhotoImage(file="ressources\\icons\\next.png")
    next_button = Button(window, text="next", image=next_icon, bg='grey',borderwidth=0, command=lambda : Music.next_music(music_path, music_space, space))
    next_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)


   # space2 = Label(window, text="nav space",bg='#5DC863', fg='black', font=('grey',22))
   # space2.pack(pady=15)
    
    nav = Frame(window, bg='white')
    nav.pack(padx=10, pady=5,anchor='center')
    # Affichage de la fenêtre créée :
    window.mainloop()

    print("Tout fonctionne correctement")


if __name__ == "__main__":
    main()