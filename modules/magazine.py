from modules.library_item import LibrariItem

class Magazine(LibrariItem):
    def __init__(self, title, subject, upc, volume, issue):
        LibrariItem.__init__(self, title, subject, upc)
        self.volume = volume
        self.issue = issue