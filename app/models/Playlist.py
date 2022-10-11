#Modèle playlist représentant une playlist -> liste de musique séléctionnées
import os

PLAYLIST_PATH = "resources\playlists"
LIBRAIRIE_PATH = "resources\songs"

def getPlaylists():
    playlists = []
    dir_list = os.listdir(PLAYLIST_PATH)
    for file in dir_list:
        playlists.append(file)
    return playlists

def getMusics(playlist_name):
    if os.path.isfile(PLAYLIST_PATH+"\\"+playlist_name+".txt"):
        musics = []
        file = open(PLAYLIST_PATH+"\\"+playlist_name+".txt", "r")
        line = file.readline()
        while line:
            line = file.readline()
            music = line.replace("\n", "")
            if music != '':
                musics.append(music)
        file.close()
        return musics
    else:
        print("Cette playlist n'existe pas.")

def create(name):
    if not os.path.isfile(PLAYLIST_PATH+"\\"+name+".txt"):
        print("Création de la playlist "+name)
        file = open(PLAYLIST_PATH+"\\"+name+".txt",'w')
        file.close()
    else:
        print(name+" existe déja.")

def delete(name):
    if os.path.isfile(PLAYLIST_PATH+"\\"+name+".txt"):
        os.remove(PLAYLIST_PATH+"\\"+name+".txt")
        print(name+" a été supprimée.")
    else:
        print(name+" n'existe pas.")
  
def add_musics(playlist_name, music_name):
    if not os.path.isfile(PLAYLIST_PATH+"\\"+playlist_name+".txt"):
        print(playlist_name+" n'éxiste pas.")
    else:
        if not os.path.isfile(LIBRAIRIE_PATH+"\\"+music_name):
            playlist_file = open(PLAYLIST_PATH+"\\"+playlist_name+".txt",'a')
            playlist_file.write(music_name+'\n')
            playlist_file.close()
            print(music_name+" ajouté à "+playlist_name)
        else:
            print("Cette musique n'est pas présente dans votre librairie.")

def remove_musics(playlist_name, line_number):
    music_name = ""
    if not os.path.isfile(PLAYLIST_PATH+"\\"+playlist_name+".txt"):
        print(playlist_name+" n'éxiste pas.")
    else:
        try:
            with open(PLAYLIST_PATH+"\\"+playlist_name+".txt", 'r') as fr:
                lines = fr.readlines()
                ptr = 1
                with open(PLAYLIST_PATH+"\\"+playlist_name+".txt", 'w') as fw:
                    for line in lines:
                        if ptr != line_number:
                            music_name = line
                            fw.write(line)
                        ptr += 1
            print(music_name+" a été retirée.")
        except:
            print("Oops! something error")

def play_playist(name):
    music_list = getMusics(name)
    #play(music_list)    


create('playlist_1')
#delete('playlist_1')
#add_musics('playlist_1','Avicii - The Nights')
#add_musics('playlist_1','Cry Baby- Tokyo Revengers')
#remove_musics('playlist_1', 2)
print(getMusics('playlist_1'))
print(getPlaylists())