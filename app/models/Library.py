#Modèle principal contenant les musiques et les playlists de l'app
class Library :

    #Composé de tous les éléments Music de l'app
    music_list = []

    #Composé d'éléments Tracks
    playlists = []

    def __init__(self, music_list, playlists):
        self.music_list = music_list
        self.playlists = playlists

    def set_music_list(self, music_list):
        self.music_list = music_list
    
    def set_playlists(self, playlists):
        self.playlists = playlists
    
    def get_music_list(self):
        return self.music_list
    
    def set_playlists(self):
        return self.playlists
