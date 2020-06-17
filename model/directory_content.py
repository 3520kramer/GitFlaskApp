class DirectoryContent:

    def __init__(self, name, is_dir):
        self.name = name
        self.is_dir = is_dir

    def __repr__(self):
        return f'{self.__dict__}'

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def is_dir(self):
        return self.__is_dir

    @is_dir.setter
    def is_dir(self, is_dir):
        self.__is_dir = is_dir

