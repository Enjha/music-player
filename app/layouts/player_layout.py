from tkinter import *
from tkinter import font
import tkinter.ttk as ttk
from app.models.library import *
from app.models.music import *

import time

class PlayerLayout (Frame): 

    window = ()

    # Constructeur
    def __init__(self, window):
        self.window = window

    def print(self):
        font_text_button = font.Font(size=20, family=('Comic Sans MS'), weight=font.BOLD)
        library = Library()
        music_list = library.get_music_list()
       
        # Evenement lors d'un clic de souris à un endroit précis
        def on_click_playlist(event):
            pass

        def on_click_music(event):
            library.play_music(music_space, music_title, pause_button)
            supp_button.pack(side=RIGHT)
            retrieve_player()
        
        # Permet de faire disparaître le lecteur lorsque aucune musique n'est jouée  
        def forget_player():
            player_zone.grid_forget()
            library.stop_music(music_space)
            supp_button.pack_forget()
            music_title.config(text="Pour reprendre l'écoute, cliquez sur une musique.")
        
        # Permet de faire apparaître le lecteur lorsque qu'une musique est jouée  
        def retrieve_player():
            player_zone.grid()   
            prev_button.pack(in_=buttons, side=LEFT)
            pause_button.pack(in_=buttons,side=LEFT)
            next_button.pack(in_=buttons, side=LEFT)
            stop_button.pack(in_=buttons, side=LEFT)
            play_button["text"] = "🔁"
            play_button.pack(padx=8, pady=15,in_=buttons, side=LEFT)
    

        # Zone haute de la fenêtre contenant les boutons de l'interface
        top_buttons = Frame(self.window, bg="green")
        top_buttons.grid(padx=(10,10),pady=(20,20),row=0, column=0)
        # Boutons importer, accéder aux playlists et supprimer
        import_button = Button(top_buttons, text="Importer des musiques", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : library.import_music(music_space))
        playlist_button = Button(top_buttons, text="Accéder aux playlists", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : library.import_music(music_space))
        supp_button = Button(top_buttons,text="🗑️ Supprimer", activebackground='#ff5e57', bg='#ff3f34', fg ='white', borderwidth=0, command=lambda : library.delete_music(music_space))
        
        import_button.pack(padx=(10),pady=(10),side=LEFT)
        playlist_button.pack(padx=(40),pady=(10),side=LEFT)
        supp_button.pack_forget()
        
        # Zone centrale de la fenêtre où les musiques seront affichées
        musics_frame = Frame(self.window, width=900, height=500, bg="#141414")
        musics_frame.grid(row=1, column=0,padx=1, pady=1)
        
        music_space = Listbox(musics_frame, fg="white",width=70,height=14, bg="#202020",font=('helvetica',18), selectbackground="#4b4b4b", relief=FLAT, selectforeground="white", highlightthickness=0, activestyle=NONE)
        music_space.pack(padx=10, pady=10)
        # On rempli la listbox précédemment créé des musiques de notre librairie
        for music in music_list: 
            music_space.insert('end', music.get_title()) 
        
        # Ajout d'un évènement pour le clic sur un musique dans cette zone   
        music_space.bind("<Double-Button>", on_click_music)
        # Affichage d'information utilisateur et de la musique jouée dans un label
        label_zone = Frame(self.window, width=900, height=20, bg="#141414")
        label_zone.grid(row=3, column=0,padx=1, pady=1)
        music_title = Label(label_zone, text="Veuillez choisir une musique.",bg='#141414', fg='white', font=('poppin',22))
        music_title.pack(pady=15)
        
        # Zone du player en bas de la fenêtre
        bottom_player = Frame(self.window, width=1000, height=70, bg="#141414")
        bottom_player.grid(padx=(0,0),pady=(0,30), row=4, column=0)
        player_zone = Frame(bottom_player, width=1000, height=70, bg="#141414")
        # Ajout d'une frame de boutons
        buttons = Frame(player_zone, bg='#141414')
        buttons.pack(padx=10, pady=5,anchor='center') 
        # Boutons précèdent
        prev_button = Button(self.window, text="⏮", bg='#141414', fg='white',borderwidth=0, command=lambda : library.prev_music(music_space, music_title, pause_button))
        prev_button.pack(padx=8, pady=10, in_=buttons, side=LEFT)
        prev_button['font'] = font_text_button     
        # Bouton stop
        stop_button = Button(self.window, text="⏹", bg='#141414', fg='white',borderwidth=0, command=lambda : forget_player())
        stop_button.pack(padx=8, pady=15, in_=buttons,side=RIGHT)
        stop_button['font'] = font_text_button  
        # Bouton jouer
        play_button = Button(self.window, text="▶️", bg='#141414', fg='white',borderwidth=0, command=lambda : library.play_music(music_space, music_title, pause_button))
        play_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        play_button['font'] = font_text_button  
        # Bouton pause
        pause_button = Button(self.window, text="⏸", bg='#141414', fg='white',borderwidth=0, command=lambda : library.pause_music(pause_button))
        pause_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
        pause_button['font'] = font_text_button 
        # Bouton suivant
        next_button = Button(self.window, text="⏭", bg='#141414', fg='white',borderwidth=0, command=lambda : library.next_music(music_space, music_title, pause_button))
        next_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        next_button['font'] = font_text_button       
    
        # Affichage d'un slider pour la musique en cours de lecture
        slider_zone = Frame(self.window, width=900, height=20, bg="#141414")
        slider_zone.grid(row=5, column=0,padx=1, pady=1)
        music_slider = ttk.Scale(slider_zone, from_=0, to=100, orient=HORIZONTAL, value=0, length=400)
        music_slider.pack(side=LEFT, padx=50)

        
        status_zone = Frame(self.window,width=900, height=10, bg='white')
        status_zone.grid(row=6, column=0,padx=1, pady=1)
        status_bar = Label(status_zone, text='TIMER HERE', bd=1, bg='red', relief=GROOVE, anchor=E)
        status_bar.pack(fill=X, side=BOTTOM, ipady=2) 
        
        def play_time():
            current_time = mixer.music.get_pos() / 1000  
            converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))
            
            song = music_space.get(ACTIVE)
            current_song = library.find_music_by_name(song)
            song = LIBRARY_PATH + "\\" + song + ".mp3"
            song_length = current_song.get_duration()
            converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))
            current_time +=1
            if int(music_slider.get() == int(song_length)):
                status_bar.config(text=f'Temps écoulé : {converted_song_length} ')
            elif int(music_slider.get()) == int(current_time):
                slider_position = int(song_length)
                music_slider.config(to=slider_position, value=int(current_time))
            else:
                slider_position = int(song_length)
                music_slider.config(to=slider_position, value=int(music_slider.get()))
                converted_current_time = time.strftime('%M:%S', time.gmtime(int(music_slider.get())))
                status_bar.config(text=f'Temps écoulé : {converted_current_time}  sur  {converted_song_length} ')
                next_time = int(music_slider.get()) + 1
                music_slider.config(value=next_time)

            #status_bar.config(text=f'Temps écoulé : {converted_current_time}  sur  {converted_song_length} ')
            #music_slider.config(value=int(current_time))
            status_bar.after(1000, play_time) 
            
        play_time()
    # Destruction de la fenêtre   
    def clear(self):
        self.destroy()