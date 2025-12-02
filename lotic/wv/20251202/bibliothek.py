import json

class Bibliothek:
    def __init__(self, media_list = []):
        self._media_list = media_list

    def add_media(self, media):
        self._media_list.append(media)
        return True
    def find_media_index(self, title):
        for index in range(0, len(self._media_list)):
            if self._media_list[index].get_title() == title:
                return index
        return -1
    def remove_media(self, title):
        index = self.find_media_index(title)
        if index == -1:
            return False
        self._media_list.pop(index)
        return True
    def convert_to_dictlist(self):
        dictlist = []
        for media in self._media_list:
            media_dict = {
                'title': media.get_title(),
                'release_year': media.get_release_year(),
                'author': media.get_author(),
                'page_count': media.get_page_count(),
            }
            dictlist.append(media_dict)
        return dictlist
    def list_medias(self):
        for media in self._media_list:
            print(media)
    def import_csv(self):
        filename = input('Welche Datei soll importiert werden? ')
        import_file = open(filename, 'r')
        csv_string = import_file.read()
        media_list = csv_string.splitlines()
        for media_string in media_list:
            attribute_list = media_string.split(',')
            title = attribute_list[0]
            release_year = attribute_list[1]
            author = attribute_list[2]
            page_count = attribute_list[3]
            book = Buch(title, release_year, author, page_count)
            self.add_media(book)
        import_file.close()
        print(f'{len(media_list)} Bücher wurden importiert')
    def export_csv(self):
        filename = input('Dateiname? ')
        export_file = open(filename, 'w')
        csv_string = ''
        for media in self._media_list:
            media_string = f'{media.get_title()},{media.get_release_year()},{media.get_author()},{media.get_page_count()}\n'
            csv_string += media_string
        export_file.close()
    def export_json(self):
        filename = input('Dateiname? ')
        export_file = open(filename, 'w')
        dict_list = self.convert_to_dictlist()
        json_string = json.dumps(dict_list)
        export_file.write(json_string)
        print(f'{len(dict_list)} Bücher wurden exportiert')
    def import_json(self):
        filename = input('Dateiname? ')
        import_file = open('importme.json')
        json_string = import_file.read()
        media_list = json.load(json_string)
        print(media_list)
    def info(self):
        print('coming soon')

class Medium:
    def __init__(self, titel, erscheinungsjahr):
        self._titel = titel
        self._erscheinungsjahr = erscheinungsjahr
    def get_title(self):
        return self._titel
    def get_release_year(self):
        return self._erscheinungsjahr

class Buch(Medium):
    def __init__(self, titel, erscheinungsjahr, autor, seitenzahl):
        super().__init__(titel, erscheinungsjahr)
        self._autor = autor
        self._seitenzahl = seitenzahl
    def get_author(self):
        return self._autor
    def get_page_count(self):
        return self._seitenzahl
    def __str__(self):
        return f'{self._titel} - {self._erscheinungsjahr} - {self._autor} - {self._seitenzahl}'
    def info(self):
        print(f'{self._titel} - {self._erscheinungsjahr} - {self._autor} - {self._seitenzahl}')

class Dvd(Medium):
    def __init__(self, titel, erscheinungsjahr,  regisseur, spielzeit):
        super().__init__(titel, erscheinungsjahr)
        self._regisseur = regisseur
        self._spielzeit = spielzeit
    def get_spielzeit(self):
        return self._spielzeit
    def get_regisseur(self):
        return self._regisseur
    def __str__(self):
        return f'{self._titel} - {self._erscheinungsjahr} - {self._regisseur} - {self._spielzeit}'
    def info(self):
        print(f'{self._titel} - {self._erscheinungsjahr} - {self._regisseur} - {self._spielzeit}')

def readBookInfo():
    title = input('Titel: ')
    release_year = input('Erscheinungsjahr: ')
    author = input('Autor: ')
    pages = input('Seitenzahl: ')
    buch = Buch(title, release_year, author, pages)
    biblio1.add_media(buch)
    print('Buch hinzugefügt')

def readDVDInfo():
    title = input('Titel: ')
    release_year = input('Erscheinungsjahr: ')
    regisseur = input('Regisseur: ')
    runtime = input('Spielzeit: ')
    dvd = Dvd(title, release_year, regisseur, runtime)
    biblio1.add_media(dvd)
    print('DVD hinzugefügt')

def removeTitle():
    title = input('Titel: ')
    media_removed = biblio1.remove_media(title)
    if media_removed:
        return print('Medium wurde entfernt')
    return print('Medium konnte nicht entfernt werden')

def readUserInput():
    userInput = ''
    while userInput != 'q':
        userInput = input()
        if userInput == '1':
            readBookInfo()
        elif userInput == '2':
            readDVDInfo()
            biblio1.info()
        elif userInput == '3':
            removeTitle()
        elif userInput == '4':
            biblio1.list_medias() 
            readUserInput()
        elif userInput == '5':
            biblio1.import_csv()
        elif userInput == '6':
            biblio1.export_csv()
        elif userInput == '7':
            biblio1.import_json()
        elif userInput == '8':
            biblio1.export_json()
        elif userInput == 'h':
            bibmenu()
        elif userInput == 'q':
            break
        else:
            print('Ungültige Eingabe')


biblio1 = Bibliothek()

# Some test Media
buch1 = Buch('Momo', 1973, 'Micheal Ende', 250)
biblio1.add_media(buch1)
#dvd1 = Dvd('The hateful eight', 2015, 'Quentin Tarantino', 168)
#biblio1.add_media(dvd1)

def bibmenu():
    print('''
    Willkommen in Lotics Bibliothek
    [1]: Buch hinzufügen
    [2]: DVD hinzufügen
    [3]: Medium löschen
    [4]: Liste
    [5]: Importiere CSV
    [6]: Exportiere CSV
    [7]: Importiere JSON
    [8]: Exportiere JSON
    [h]: Hilfe
    [q]: Beenden
    ''')

bibmenu()
readUserInput()

