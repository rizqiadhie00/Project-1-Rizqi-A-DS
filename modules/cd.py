from modules.library_item import LibrariItem 

class Cd(LibrariItem):
    def __init__(self, title, subject, upc, artist):
        LibrariItem.__init__(self,title, upc, subject)
        self.artist = artist
