from ast import main, pattern
from fileinput import filename
# from tkinter import *
import tkinter as tk
import os
import fnmatch
#from pygame import mixer


def main():
    window = tk.Tk()

    # Ajout d'un titre à la fenêtre principale :
    window.title("Spotizer")

    window.geometry("500x600")
    window.resizable = False
    window.config(bg='green')

    music_path = "ressources\\songs"
    pattern = "*.mp3"


    music_space = tk.Listbox(window, fg="white", bg="black", width=100,height=20)
    music_space.pack(padx=10, pady=10)

    for root, dirs, files, in os.walk(music_path):
        for filename in fnmatch.filter(files, pattern):
            final_name = filename.strip('.mp3')
            music_space.insert('end', final_name)

    # Affichage de la fenêtre créée :
    window.mainloop()

    print("ça fonctionne correctement")


if __name__ == "__main__":
    main()
