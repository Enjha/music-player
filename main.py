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
    window.geometry("600x750")
    window.resizable(False,False)
    window.config(bg='#5DC863')

    window.maxsize(600,750)
    window.minsize(600,750)

    music_path = "ressources\\songs"
    pattern = "*.mp3" 
                        
    def prev_music(): 
        prev_song = music_space.curselection()
        prev_song = prev_song[0]-1
        prev_song_name = music_space.get(prev_song)
        space.config(text= prev_song_name)
        mixer.music.load(music_path + "\\" + prev_song_name + ".mp3")
        mixer.music.play()
        music_space.select_clear(0, 'end')
        music_space.activate(prev_song)
        music_space.select_set(prev_song)
    
    def stop_music():
        mixer.music.stop()
        music_space.select_clear('active')
          
    def play_music():
        space.config(text=music_space.get("anchor"))
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
        space.config(text= next_song_name)
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
         
    import_button = Button(window, text="Importer des musiques", bg="grey", fg="black", command=import_music)
    import_button.pack(pady=5, padx=25, side=RIGHT)
 
    music_space = Listbox(window, fg="black", bg="grey", width=100,font=('helvetica',18))
    music_space.pack(padx=18, pady=18)
    
    scroll_music = Scrollbar(window)
    scroll_music.config(command=music_space.yview)
    scroll_music.pack(side=RIGHT, fill=Y)

    for root, dirs, files, in os.walk(music_path):
        for filename in fnmatch.filter(files, pattern):
            final_name = filename.strip('.mp3')
            music_space.insert('end', final_name)



    space = Label(window, text="Boutons space",bg='#5DC863', fg='black', font=('poppin',22))
    space.pack(pady=15)
    
    buttons = Frame(window, bg='grey')
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


    space2 = Label(window, text="nav space",bg='#5DC863', fg='black', font=('grey',22))
    space2.pack(pady=15)
    
    nav = Frame(window, bg='white')
    nav.pack(padx=10, pady=5,anchor='center')
    # Affichage de la fenêtre créée :
    window.mainloop()

    print("Tout fonctionne correctement")


if __name__ == "__main__":
    main()