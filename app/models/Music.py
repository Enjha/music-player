#Modèle représentant une musique et ses attributs
class Music :

    title = ""

    time_in_seconds = 0

    path = ""

    def __init__(self, title, time_in_seconds, path):
        self.title = title
        self.time_in_seconds = time_in_seconds
        self.path = path

    def get_title(self):
        return self.title
    
    def get_time_in_seconds(self):
        return self.time_in_seconds

    def get_path(self):
        return self.path