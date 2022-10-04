#Modèle playlist représentant une playlist -> liste de musique séléctionnées
class Playlist :

    #Composé d'éléments Music
    musics = []

    def __init__(self, musics):
        self.musics = musics

    def set_musics(self, musics):
        self.musics = musics
    
    def get_musics(self):
        return self.musics
