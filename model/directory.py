import os
from model.directory_content import DirectoryContent

class Directory:

    def __init__(self):
        self.base_dir_path = os.getcwd()
        self.content = os.listdir()
        self.has_error_changing_dir = False

    def __repr__(self):
        return f'{self.__dict__}'

    # EXAMPLE OF PYTHON USING DATAMODEL FOR 
    def __add__(self, other):
        if os.path.lexists(os.path.join(other)):
            os.chdir(other)
            return Directory()
        else:
            return self

    @property
    def base_dir_path(self):
        return self.__base_dir_path
    
    @base_dir_path.setter
    def base_dir_path(self, base_dir_path):
        self.__base_dir_path = base_dir_path

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):

        #temp = [DirectoryContent('..', True)]
        temp = []

        # TODO: CREATE LIST COMP
        for dir_content in content:
            if os.path.isdir(dir_content):
                temp.append(DirectoryContent(dir_content, True))
            else:
                temp.append(DirectoryContent(dir_content, False))
            
        self.__content = temp

    @property
    def has_error_changing_dir(self):
        return self.__has_error_changing_dir

    @has_error_changing_dir.setter
    def has_error_changing_dir(self, has_error_changing_dir):
        self.__has_error_changing_dir = has_error_changing_dir
    
    def change_dir(self, path):
        try:
            os.chdir(path)
            print(os.getcwd())
            self.content = os.listdir()
            self.has_error_changing_dir = False
        except NotADirectoryError or FileNotFoundError:
            print('ERROR: Could not change directory!')
            self.has_error_changing_dir = True
        
        '''if os.path.lexists(os.path.join(path)):
            os.chdir(path)
            self.content = os.listdir()
            self.has_error_changing_dir = False
        else:
            print('ERROR: Could not change directory!')
            self.has_error_changing_dir = True'''

d = Directory()
'''
for content in d.content:
    if os.path.isfile(content):
        
        print(f'{content} is file')
    else:
        print(f'{content} is folder')
'''

'''
os.getcwd()

os.listdir()

os.path.isfile('model')

os.path.isdir('model')
'''