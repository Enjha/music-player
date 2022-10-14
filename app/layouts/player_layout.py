from tkinter import *
from tkinter import font
from app.models.library import *
from app.models.music import *

class PlayerLayout (Frame): 

    window = ()

    # Constructeur
    def __init__(self, window):
        self.window = window

    def print(self):
        font_text_button = font.Font(size=20, family=('Comic Sans MS'), weight=font.BOLD)
        library = Library()
        music_list = library.get_music_list()
       
        def on_click_playlist(event):
            pass

        def on_click_music(event):
            library.play_music(music_space, music_title, pause_button)
            supp_button.pack(side=RIGHT)
            retrieve_player()
            
        def forget_player():
            player_zone.grid_forget()
            library.stop_music(music_space)
            supp_button.pack_forget()
            music_title.config(text="Pour reprendre l'écoute, cliquez sur une musique.")
            
        def retrieve_player():
            player_zone.grid()   
            prev_button.pack(in_=buttons, side=LEFT)
            pause_button.pack(in_=buttons,side=LEFT)
            next_button.pack(in_=buttons, side=LEFT)
            stop_button.pack(in_=buttons, side=LEFT)
            play_button["text"] = "↻"
            play_button.pack(padx=8, pady=15,in_=buttons, side=LEFT)

        top_buttons = Frame(self.window, bg="green")
        top_buttons.grid(padx=(10,10),pady=(20,20),row=0, column=0)
        
        import_button = Button(top_buttons, text="Importer des musiques", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : library.import_music(music_space))
        playlist_button = Button(top_buttons, text="Accéder aux playlists", activebackground="#0be881", bg="#05c46b", fg="white", command=lambda : library.import_music(music_space))
        supp_button = Button(top_buttons,text="🗑️ Supprimer", activebackground='#ff5e57', bg='#ff3f34', fg ='white', borderwidth=0, command=lambda : library.delete_music(music_space))
        
        import_button.pack(padx=(10),pady=(10),side=LEFT)
        playlist_button.pack(padx=(40),pady=(10),side=LEFT)
        supp_button.pack_forget()
        
        musics_frame = Frame(self.window, width=900, height=500, bg="#141414")
        musics_frame.grid(row=1, column=0,padx=1, pady=1)
        
        music_space = Listbox(musics_frame, fg="white",width=70,height=20, bg="#202020",font=('helvetica',18), selectbackground="#4b4b4b", relief=FLAT, selectforeground="white", highlightthickness=0, activestyle=NONE)
        music_space.pack(padx=10, pady=10)
        
        for music in music_list: 
            music_space.insert('end', music.get_title()) 
            
        music_space.bind("<Button>", on_click_music)
             
        label_zone = Frame(self.window, width=900, height=20, bg="#141414")
        label_zone.grid(row=3, column=0,padx=1, pady=1)
        music_title = Label(label_zone, text="Veuillez choisir une musique.",bg='#141414', fg='white', font=('poppin',22))
        music_title.pack(pady=15)

        
        bottom_player = Frame(self.window, width=1000, height=70, bg="#141414")
        bottom_player.grid(padx=(0,0),pady=(0,30), row=4, column=0)
        player_zone = Frame(bottom_player, width=1000, height=70, bg="#141414")
        buttons = Frame(player_zone, bg='#141414')
        buttons.pack(padx=10, pady=5,anchor='center') 
        
        prev_button = Button(self.window, text="⏮", bg='#141414', fg='white',borderwidth=0, command=lambda : library.prev_music(music_space, music_title, pause_button))
        prev_button.pack(padx=8, pady=10, in_=buttons, side=LEFT)
        prev_button['font'] = font_text_button     
        
        stop_button = Button(self.window, text="⏹", bg='#141414', fg='white',borderwidth=0, command=lambda : forget_player())
        stop_button.pack(padx=8, pady=15, in_=buttons,side=RIGHT)
        stop_button['font'] = font_text_button  
        
        play_button = Button(self.window, text="▶️", bg='#141414', fg='white',borderwidth=0, command=lambda : library.play_music(music_space, music_title))
        play_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        play_button['font'] = font_text_button  
        
        pause_button = Button(self.window, text="⏸", bg='#141414', fg='white',borderwidth=0, command=lambda : library.pause_music(pause_button))
        pause_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
        pause_button['font'] = font_text_button 
        
        next_button = Button(self.window, text="⏭", bg='#141414', fg='white',borderwidth=0, command=lambda : library.next_music(music_space, music_title, pause_button))
        next_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        next_button['font'] = font_text_button       
        
    def clear(self):
        self.destroy()