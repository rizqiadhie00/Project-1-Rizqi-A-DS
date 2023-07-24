from modules.book import Book
from modules.magazine import Magazine
from modules.dvd import Dvd
from modules.catalog import Catalog
from modules.cd import Cd
import json

book1 = Book('Title test',
             'ini book 1',
             None,
             '1345-5433',
             'Raka Mahendra',
             '08989787876'
             )

book2 = Book('Title test',
             'ini ini',
             None,
             '1345-4567',
             'Raka Mahen',
             '08989787876'
             )

book3 = Book('Title test',
             'ini ini',
             None,
             '1345-4567',
             'Raka Mahen',
             '08989787876'
             )

magazine1 = Magazine(
    'media cnn test',
    'edisi 14 juli 2023',
    None,
    'volume 1',
    '-'
)

magazine2 = Magazine(
    'media cnbc',
    'edisi 15 juli 2023',
    None,
    'volume 2',
    '-'
)

dvd1= Dvd(
    'Test DVD 1',
    'Ini subject test dvd 1',
    None,
    None,
    None,
    'Comedy'
)


#collect per kategori
book = [book1, book2, book3] 
magazine = [magazine1, magazine2]
dvd = [dvd1]

# get data from json
f = open('files/catalog.json')
data_json = json.load(f)
for item in data_json:
    if item['source'] == 'book':
        book.append(Book(
            title=item['title'],
            subject=item['subject'],
            upc=item['upc'],
            issbn=item['issbn'],
            authors=item['authors'],
            dds_number=item['dds_number'],
        ))
        
#collect all
catalog_all = [book, magazine, dvd]
print(catalog_all)
#run and search
input_search = 'test'
results = Catalog(catalog_all).search(input_search)

if results:
    for index, result in enumerate(results):
        print(f'result ke-{index+1} | {result}')
    else:
        print('No result')

