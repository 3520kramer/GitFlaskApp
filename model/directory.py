import os

from directory_content import DirectoryContent

class Directory:

    def __init__(self):
        self.base_dir_path = os.getcwd()
        self.content = os.listdir()
        self.has_error_changing_dir = False
        self.has_git_init = self.check_git_init()

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

        temp.sort(key=lambda x: x.is_dir, reverse=True)
        #temp.insert(0, DirectoryContent('..', None))
            
        self.__content = temp
    
    @property
    def has_error_changing_dir(self):
        return self.__has_error_changing_dir

    @has_error_changing_dir.setter
    def has_error_changing_dir(self, has_error_changing_dir):
        self.__has_error_changing_dir = has_error_changing_dir
    
    @property
    def has_git_init(self):
        return self.__has_git_init

    @has_git_init.setter
    def has_git_init(self, has_git_init):
        self.__has_git_init = has_git_init

    def check_git_init(self):
        if '.git' in os.listdir():
            return True
        else:
            return False

    def change_dir(self, path):
        try:
            os.chdir(path)
            self.content = os.listdir()
            self.has_git_init = self.check_git_init()

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
temp = []
temp.append(DirectoryContent('mappe', True))
temp.append(DirectoryContent('mappe2', True))
temp.append(DirectoryContent('mappe3', True))
temp.append(DirectoryContent('fil1', False))
temp.append(DirectoryContent('fil2', False))

temp.sort(key=lambda x: x.is_dir, reverse=True)
temp.insert(0, DirectoryContent('..', None))
'''
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