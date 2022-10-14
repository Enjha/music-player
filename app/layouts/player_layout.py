import pygame

from tkinter import *
import tkinter.font as font
from ..models.library import *
from ..models.music import *

class Player: 
    def main_window():
        
        window = Tk()
        pygame.mixer.init()
        
        library = Library()
        
        # Ajout d'un titre à la fenêtre principale :
        window.title("Spotizer")
        window.iconbitmap("ressources\\icons\\logo.ico")
        window.anchor(CENTER)
        window.geometry("1000x800")
        window.resizable(False,False)
        window.config(bg='#1e272e')
        window.maxsize(1500,1500)
        window.minsize(600,750)

        music_list = library.get_music_list()
        f = font.Font(size=20)
       
        def on_click(event):
            library.play_music(music_space, music_title, pause_button)
            retrieve_player()
            
        def forget_player():
            player_zone.grid_forget()
            library.stop_music(music_space)
            supp_zone.grid_forget()
            music_title.config(text="Pour reprendre l'écoute, cliquez sur une musique.")
            
        def retrieve_player():
            supp_zone.grid()
            player_zone.grid()   
            prev_button.pack(in_=buttons, side=LEFT)
            pause_button.pack(in_=buttons,side=LEFT)
            next_button.pack(in_=buttons, side=LEFT)
            stop_button.pack(in_=buttons, side=LEFT)
            play_button["text"] = "🔁"
            play_button.pack(padx=8, pady=15,in_=buttons, side=LEFT)
            supp_zone.grid(row=0, column=2)
            
        top_buttons = Frame(window, width=900, height=50, bg="#1e272e")
        top_buttons.grid(row=0, column=0,padx=1, pady=1)
        
        import_zone = Frame(top_buttons, width=100, bg="#1e272e")
        import_zone.grid(row=0, column=0)
        blank_zone_import = Frame(top_buttons, width=635, bg="#1e272e")
        blank_zone_import.grid(row=0, column=1)
        supp_zone = Frame(top_buttons, width=100, bg="#1e272e")
        
        import_button = Button(import_zone, text="Importer des musiques", bg="grey", fg="#1e272e", command=lambda : library.import_music(music_space))
        import_button.pack(pady=5, padx=25)
        
        supp_button = Button(supp_zone, text="🗑️ Supprimer", bg='red',borderwidth=0, command=lambda : library.delete_music(music_space))
        supp_button.pack(pady=5, padx=25)
        
        musics_frame = Frame(window, width=900, height=500, bg="#1e272e")
        musics_frame.grid(row=1, column=0,padx=1, pady=1)
        
        music_space = Listbox(musics_frame, fg="white",width=70,height=20, bg="#2f3542",font=('helvetica',18), selectbackground="#4b4b4b", relief=FLAT, selectforeground="white", highlightthickness=0, activestyle=NONE)
        music_space.pack(padx=16, pady=16)
        
        for music in music_list: 
            music_space.insert('end', music.get_title()) 
            
        music_space.bind("<Double-Button>", on_click)
        
        
        label_zone = Frame(window, width=900, height=20, bg="#1e272e")
        label_zone.grid(row=3, column=0,padx=1, pady=1)
        music_title = Label(label_zone, text="Veuillez choisir une musique.",bg='#1e272e', fg='white', font=('poppin',22))
        music_title.pack(pady=15)
        
        bottom_player = Frame(window, width=1000, height=70, bg="#1e272e")
        bottom_player.grid(row=4, column=0)
        player_zone = Frame(bottom_player, width=1000, height=70, bg="#1e272e")
        buttons = Frame(player_zone, bg='#1e272e')
        buttons.pack(padx=10, pady=5,anchor='center') 
        
        prev_button = Button(window, text="⏮", bg='#1e272e', fg='white',borderwidth=0, command=lambda : library.prev_music(music_space, music_title, pause_button))
        prev_button.pack(padx=8, pady=10, in_=buttons, side=LEFT)
        prev_button['font'] = f    
        
        stop_button = Button(window, text="⏹", bg='#1e272e', fg='white',borderwidth=0, command=lambda : forget_player())
        stop_button.pack(padx=8, pady=15, in_=buttons,side=RIGHT)
        stop_button['font'] = f 
        
        play_button = Button(window, text="▶️", bg='#1e272e', fg='white',borderwidth=0, command=lambda : library.play_music(music_space, music_title))
        play_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        play_button['font'] = f 
        
        pause_button = Button(window, text="⏸", bg='#1e272e', fg='white',borderwidth=0, command=lambda : library.pause_music(pause_button))
        pause_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
        pause_button['font'] = f 
        
        next_button = Button(window, text="⏭", bg='#1e272e', fg='white',borderwidth=0, command=lambda : library.next_music(music_space, music_title, pause_button))
        next_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        next_button['font'] = f        
        
        # Affichage de la fenêtre créée :
        window.mainloop()