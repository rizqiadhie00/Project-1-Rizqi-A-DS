from modules.library_item import LibrariItem 

class Dvd(LibrariItem):
    def __init__(self, title, subject, upc, actors, director, genre):
        LibrariItem.__init__(self,title, upc, subject)
        self.actors = actors
        self.director = director
        self.genre = genre
