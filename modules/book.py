from modules.library_item import LibrariItem 

class Book(LibrariItem):
    def __init__(self, title, subject, upc, issbn, authors, dds_number):
        LibrariItem.__init__(self,title, upc, subject)
        self.issbn = issbn
        self.authors = authors
        self.dds_number = dds_number
