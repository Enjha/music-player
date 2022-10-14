import os 
from app.models.library import Library

# Modèle playlist représentant une playlist
class Playlist (object):

    # Chemin pointant les playlists
    global PLAYLIST_PATH
    PLAYLIST_PATH = "ressources\playlists"

    title = ""          # Titre de la playlsit
    music_list = []     # Liste des musiques de la playlist

    # Constructeur
    def __init__(self, title):
        self.title = title

    # Initialise les liste de musiques et de playlists en allant chercher directemment dans les fichiers/dossiers.
    def init_music_list(self):
        file = open(PLAYLIST_PATH+"\\"+self.title+".txt", "r")
        line = file.readline()
        while line:
            music_title = line.replace("\n", "")
            music = self.find_music_by_name(music_title)
            self.music_list.append(music)
            line = file.readline()               
        file.close()

    #Getter sur le title et la liste des musiques
    def get_title(self):
        return self.title   

    def get_music_list(self):
        return self.music_list

    # Créer une playlist avec un titre
    def create(self):
        if not os.path.isfile(PLAYLIST_PATH+"\\"+self.title+".txt"):
            file = open(PLAYLIST_PATH+"\\"+self.title+".txt",'w')
            file.close()
            print("Création de la playlist "+self.title)
            return True
        else:
            print(self.title+" existe déja.")
            return False

    # Supprimer une playlist 
    def delete(self):
        if os.path.isfile(PLAYLIST_PATH+"\\"+self.title+".txt"):
            os.remove(PLAYLIST_PATH+"\\"+self.title+".txt")
            title = self.title
            print ("La playlist "+title+" a été supprimée.")
            return True
        else:
            print(self.title+" n'existe pas.")
            return False
    
    # Ajouter une musique a la playlist
    def add_music(self, music):
        library = Library()
        print(self.title)
        if not os.path.isfile(PLAYLIST_PATH+"\\"+self.title+".txt"):
            print(self.title+" n'éxiste pas.")
        else:
            print(music.get_title())
            if library.is_music_exist(music.get_title()):
                playlist_file = open(PLAYLIST_PATH+"\\"+self.title+".txt",'a')
                playlist_file.write(music.get_title()+'\n')
                playlist_file.close()
                print(music.get_title()+" ajouté à "+self.title)
                self.music_list.append(music)
            else:
                print("Cette musique n'est pas présente dans votre librairie.")

    # Retirer une musique de la playlist
    def remove_music(self, music):
        if not os.path.isfile(PLAYLIST_PATH+"\\"+self.title+".txt"):
            print(self.title+" n'éxiste pas.")
        else:
            try:
                with open(PLAYLIST_PATH+"\\"+self.title+".txt", 'r') as fr:
                    lines = fr.readlines()
                    with open(PLAYLIST_PATH+"\\"+self.title+".txt", 'w') as fw:
                        for line in lines:
                            if line == music.get_title():
                                music_name = line
                                fw.write(line)
                print(music_name+" a été retirée.")
            except:
                print("Oops! something error")
                
    # Retirer une musique de la playlist avec l'index dans la playlist
    def remove_music_by_index(self, index):
        if not os.path.isfile(PLAYLIST_PATH+"\\"+self.title+".txt"):
            print(self.title+" n'éxiste pas.")
        else:
            try:
                with open(PLAYLIST_PATH+"\\"+self.title+".txt", 'r') as fr:
                    lines = fr.readlines()
                    ptr = 1
                    with open(PLAYLIST_PATH+"\\"+self.title+".txt", 'w') as fw:
                        for line in lines:
                            if ptr != index:
                                music_name = line
                                fw.write(line)
                print(music_name+" a été retirée.")
            except:
                print("Oops! something error")

    # Retrouver une musique dans la librairie avec son titre
    def find_music_by_name(self, name):
        library = Library()
        music_list_library = library.get_music_list()
        for music in music_list_library:
            if(music.get_title() == name):
                return music