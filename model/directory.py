import os
from directory_content import DirectoryContent

class Directory:

    def __init__(self):
        self.current_dir = os.getcwd()
        self.content = os.listdir()

    def __repr__(self):
        return f'{self.__dict__}'

    def __add__(self, other):
        if os.path.lexists(os.path.join(other)):
            os.chdir(other)
            return Directory()
        else:
            return self

    @property
    def current_dir(self):
        return self.__current_dir
    
    @current_dir.setter
    def current_dir(self, current_dir):
        self.__current_dir = current_dir

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):

        temp = []

        for dir_content in content:
            if os.path.isdir(dir_content):
                temp.append(DirectoryContent(dir_content, True))
            else:
                temp.append(DirectoryContent(dir_content, False))
            
        self.__content = temp

    def go_one_dir_up(self):
        os.chdir('..')
        return Directory()

d = Directory()
'''
for content in d.content:
    if os.path.isfile(content):
        
        print(f'{content} is file')
    else:
        print(f'{content} is folder')
'''
os.getcwd()

os.listdir()

os.path.isfile('model')

os.path.isdir('model')