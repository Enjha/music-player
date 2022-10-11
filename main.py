from ast import main
from fileinput import filename
from tkinter import *
import os
import fnmatch
from tkinter import filedialog
import pygame
from pygame import mixer


def main():
    
    window = Tk()
    pygame.mixer.init()
    
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
                        
    def prev_music(): 
        prev_song = music_space.curselection()
        prev_song = prev_song[0]-1
        prev_song_name = music_space.get(prev_song)
        music_title.config(text= prev_song_name)
        mixer.music.load(music_path + "\\" + prev_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(prev_song)
        music_space.select_set(prev_song)
    
    def stop_music():
        mixer.music.stop()
        music_space.select_clear('active')
          
    def play_music():
        music_title.config(text=music_space.get("anchor"))
        #mixer.music.load(music_space.get(ACTIVE) + ".mp3")
        mixer.music.load(music_path + "\\" + music_space.get("anchor") + ".mp3")
        mixer.music.play()
        

    def pause_music():
        if(pause_button["text"]== "pause"):
            mixer.music.pause()
            pause_button["text"] = "play"
        else:
            mixer.music.unpause()
            pause_button["text"]= "pause"
        
    def next_music():
        next_song = music_space.curselection()
        next_song = next_song[0]+1
        next_song_name = music_space.get(next_song)
        music_title.config(text= next_song_name)
        mixer.music.load(music_path + "\\" + next_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(next_song)
        music_space.select_set(next_song)
    
    def import_music():
        path_import = filedialog.askdirectory();
        if path_import:
            os.chdir(path_import)
            songs=os.listdir(path_import)
            for song in songs:
                if song.endswith(".mp3"):
                    music_space(END, song) 
         
    top_buttons = Frame(window, width=900, height=50, bg="blue")
    top_buttons.grid(row=0, column=0,padx=1, pady=1)
    
    blank_zone_import = Frame(top_buttons, width=750, bg="white")
    blank_zone_import.grid(row=0, column=0,padx=1, pady=1)
    import_zone = Frame(top_buttons, width=100, bg="purple")
    import_zone.grid(row=0, column=1,padx=1, pady=1)
    
    import_button = Button(import_zone, text="Importer des musiques", bg="grey", fg="black", command=import_music)
    import_button.pack(pady=5, padx=25)
    
    
    
    musics_frame = Frame(window, width=900, height=500, bg="red")
    musics_frame.grid(row=1, column=0,padx=1, pady=1)
    
    music_space = Listbox(musics_frame, fg="black",width=70,height=20, bg="grey",font=('helvetica',18))
    music_space.pack(padx=16, pady=16)
    
    for root, dirs, files, in os.walk(music_path):
        for filename in fnmatch.filter(files, pattern):
            final_name = filename.strip('.mp3')
            music_space.insert('end', final_name)
    
    
    label_zone = Frame(window, width=900, height=20, bg="white")
    label_zone.grid(row=3, column=0,padx=1, pady=1)
    music_title = Label(label_zone, text="Boutons space",bg='#5DC863', fg='black', font=('poppin',22))
    music_title.pack(pady=15)
    
    player_zone = Frame(window, width=900, height=70, bg="blue")
    player_zone.grid(row=4, column=0,padx=1, pady=1)
    buttons = Frame(player_zone, bg='grey')
    buttons.pack(padx=10, pady=5,anchor='center') 
    
    prev_icon = PhotoImage(file="ressources\\icons\\prev.png")
    prev_button = Button(window, text="prev", image=prev_icon, bg='grey',borderwidth=0, command=prev_music)
    prev_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
    
    stop_icon = PhotoImage(file="ressources\\icons\\stop.png")
    stop_button = Button(window, text="stop", image=stop_icon, bg='grey',borderwidth=0, command=stop_music)
    stop_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
    
    play_icon = PhotoImage(file="ressources\\icons\\play.png")
    play_button = Button(window, text="play", image=play_icon, bg='grey',borderwidth=0, command=play_music)
    play_button.pack(padx=8, pady=15, in_=buttons, side=LEFT)
    
    pause_icon = PhotoImage(file="ressources\\icons\\pause.png")
    pause_button = Button(window, text="pause", image=pause_icon, bg='grey',borderwidth=0, command=pause_music)
    pause_button.pack(padx=8, pady=15, in_=buttons,side=LEFT)
    
    next_icon = PhotoImage(file="ressources\\icons\\next.png")
    next_button = Button(window, text="next", image=next_icon, bg='grey',borderwidth=0, command=next_music)
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