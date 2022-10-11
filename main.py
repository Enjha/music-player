import pygame

from ast import main
from tkinter import *
from app.models.Library import *
from app.models.Music import *

def main():
    
    window = Tk()
    pygame.mixer.init()
    
    library = Library()
    
    # Ajout d'un titre à la fenêtre principale :
    window.title("Spotizer")
    window.iconbitmap("ressources\\icons\\logo.ico")
    window.anchor(CENTER)
    window.geometry("1000x800")
    window.resizable(False,False)
    window.config(bg='#5DC863')
    window.maxsize(1500,1500)
    window.minsize(600,750)

    music_path = "ressources\\songs"
    pattern = "*.mp3" 
    
    music_list = library.get_music_list()

    def on_click(event):
        Music.play_music(music_space, music_title)
        retrieve_player()
    
    def forget_player():
        player_zone.grid_forget()
    
    def retrieve_player():
        player_zone.grid(row=0, column=0,padx=1, pady=1)   
         
    top_buttons = Frame(window, width=900, height=50, bg="blue")
    top_buttons.grid(row=0, column=0,padx=1, pady=1)
    
    import_zone = Frame(top_buttons, width=100, bg="purple")
    import_zone.grid(row=0, column=0)
    blank_zone_import = Frame(top_buttons, width=630, bg="white")
    blank_zone_import.grid(row=0, column=1)
    supp_zone = Frame(top_buttons, width=100, bg="purple")
    supp_zone.grid(row=0, column=2)
    
    import_button = Button(import_zone, text="Importer des musiques", bg="grey", fg="black", command=lambda : library.import_music(music_space))
    import_button.pack(pady=5, padx=25)
    
    supp_button = Button(window, text="🗑️ Supprimer", bg='red',borderwidth=0, command=lambda : library.delete_music(music_space))
    supp_button.pack(pady=5, padx=25)
    
    musics_frame = Frame(window, width=900, height=500, bg="red")
    musics_frame.grid(row=1, column=0,padx=1, pady=1)
    
    music_space = Listbox(musics_frame, fg="black",width=70,height=20, bg="grey",font=('helvetica',18))
    music_space.pack(padx=16, pady=16)
    
    for music in music_list: 
        music_space.insert('end', music.get_title()) 
        
    music_space.bind("<Button>", on_click)
    
    
    label_zone = Frame(window, width=900, height=20, bg="white")
    label_zone.grid(row=3, column=0,padx=1, pady=1)
    music_title = Label(label_zone, text="Titre de musique ici",bg='#5DC863', fg='black', font=('poppin',22))
    music_title.pack(pady=15)
    
    
    bottom_player = Frame(window, width=900, height=70, bg="blue")
    bottom_player.grid(row=4, column=0,padx=1, pady=1)
    player_zone = Frame(bottom_player, width=900, height=70, bg="purple")
    buttons = Frame(player_zone, bg='grey')
    buttons.pack(padx=10, pady=5,anchor='center') 
        
    prev_icon = PhotoImage(file="ressources\\icons\\prev.png")
    prev_button = Button(window, text="prev", image=prev_icon, bg='grey',borderwidth=0, command=lambda : Music.prev_music(music_space, music_title))
    prev_button.pack(padx=8, pady=10, in_=buttons, side=LEFT)
    
    stop_icon = PhotoImage(file="ressources\\icons\\stop.png")
    stop_button = Button(window, text="stop", image=stop_icon, bg='grey',borderwidth=0, command=lambda : Music.stop_music(music_space))
    stop_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
    
    play_icon = PhotoImage(file="ressources\\icons\\play.png")
    play_button = Button(window, text="play", image=play_icon, bg='grey',borderwidth=0, command=lambda : Music.play_music(music_space, music_title))
    play_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
    
    pause_icon = PhotoImage(file="ressources\\icons\\pause.png")
    pause_button = Button(window, text="pause", image=pause_icon, bg='grey',borderwidth=0, command=lambda : Music.pause_music(pause_button))
    pause_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
    
    next_icon = PhotoImage(file="ressources\\icons\\next.png")
    next_button = Button(window, text="next", image=next_icon, bg='grey',borderwidth=0, command=lambda : Music.next_music(music_space, music_title))
    next_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
        
    '''
    scroll_music = Scrollbar(window)
    scroll_music.config(command=music_space.yview)
    scroll_music.pack(side=RIGHT, fill=Y)
    '''
    
    # Affichage de la fenêtre créée :
    window.mainloop()


if __name__ == "__main__":
    main()