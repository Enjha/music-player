from app.models.Library import *

# Modèle playlist représentant une playlist
class Playlist :

    # Chemin pointant les playlists
    global PLAYLIST_PATH
    PLAYLIST_PATH = "resources\playlists"

    title = ""          # Titre de la playlsit
    music_list = []     # Liste des musiques de la playlist

    # Constructeur
    def __init__(self, title, music_list):
        self.title = title
        self.music_list = music_list

    # Initialise les liste de musiques et de playlists en allant chercher directemment dans les fichiers/dossiers.
    def init_music_list(self):
        file = open(PLAYLIST_PATH+"\\"+self.title+".txt", "r")
        line = file.readline()
        while line:
            music = line.replace("\n", "")
            self.music_list.append(music)
            line = file.readline()               
        file.close()

    # Créer une playlist avec un titre
    def create(self, title):
        if not os.path.isfile(PLAYLIST_PATH+"\\"+title+".txt"):
            file = open(PLAYLIST_PATH+"\\"+title+".txt",'w')
            file.close()
            print("Création de la playlist "+title)
            self.title = title
            return True
        else:
            print(title+" existe déja.")
            return False

    # Supprimer une playlist 
    def delete(self, title):
        if os.path.isfile(PLAYLIST_PATH+"\\"+title+".txt"):
            os.remove(PLAYLIST_PATH+"\\"+title+".txt")
            del self
            print ("La playlist "+title+" a été supprimée.")
            return True
        else:
            print(title+" n'existe pas.")
            return False
    
    # Ajouter une musique a la playlist
    def add_music(self, playlist_name, music):
        if not os.path.isfile(PLAYLIST_PATH+"\\"+playlist_name+".txt"):
            print(playlist_name+" n'éxiste pas.")
        else:
            if Library.is_music_exist(music.get_title()):
                playlist_file = open(PLAYLIST_PATH+"\\"+playlist_name+".txt",'a')
                playlist_file.write(music.get_title()+'\n')
                playlist_file.close()
                print(music.get_title()+" ajouté à "+playlist_name)
                self.music_list.append(music)
            else:
                print("Cette musique n'est pas présente dans votre librairie.")

    # Retirer une musique de la playlist
    def remove_music(playlist_name, index):
        if not os.path.isfile(PLAYLIST_PATH+"\\"+playlist_name+".txt"):
            print(playlist_name+" n'éxiste pas.")
        else:
            try:
                with open(PLAYLIST_PATH+"\\"+playlist_name+".txt", 'r') as fr:
                    lines = fr.readlines()
                    ptr = 1
                    with open(PLAYLIST_PATH+"\\"+playlist_name+".txt", 'w') as fw:
                        for line in lines:
                            if ptr != index:
                                music_name = line
                                fw.write(line)
                            ptr += 1
                print(music_name+" a été retirée.")
            except:
                print("Oops! something error")