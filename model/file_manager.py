class FileManager:

    def __init__(self, file_name, mode):
        self.file_name = file_name
        self.mode = mode

    def __enter__(self):
        print('enter')
        self.file = open(self.file_name, self.mode)
        return self.file

    def __exit__(self, *args):
        print('exit')
        self.file.close()

    @property
    def file_name(self):
        return self.__file_name

    @file_name.setter
    def file_name(self, file_name):
        self.__file_name = file_name

    @property
    def mode(self):
        return self.__mode

    @mode.setter
    def mode(self, mode):
        self.__mode = mode

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        self.__file = file

import requests, re, os
logo_urls = [element for img_tag in re.split('[<>]', requests.get('https://github.com/logos').text) if all(word in img_tag for word in ['img', 'src', 'logo']) for element in img_tag.split('"') if 'http' in element]

######## DOWNLOADS THE LOGOS BUT WITH HOMEMADE CONTEXT MANAGER ########
def v1():
    os.chdir('static')
    count = 0
    for url in logo_urls:
        res = requests.get(url)
        with FileManager(f'logo_{count}.png', 'wb') as file:
            file.write(res.content)
        count += 1

######## REFACTORED: DOWNLOADS THE LOGOS BUT WITH HOMEMADE CONTEXT MANAGER ########
def v2():
    os.chdir('static')
    for count, url in enumerate(logo_urls):
        res = requests.get(url)
        with FileManager(f'logo_{count}.png', 'wb') as file:
            file.write(res.content)


    # DECIDE HOW TO CREATE FILE IN STATIC FOLDER
    # FIGURE OUT WHICH DIRECTORY THE SYSTEM IS IN

#with FileManager()
