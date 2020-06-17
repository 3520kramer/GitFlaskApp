from datetime import datetime

class Repository:

    #id, name, created_at, updated_at, language, clone_url
    # overloading the constructor
    def __init__(self, *args):
        if len(args) == 0:
            self.id = 0
        elif len(args) == 6:
            self.id = args[0]
            self.name = args[1]
            self.created_at = datetime.strptime(f'{args[2][0:10]} {args[2][11:19]}', '%Y-%m-%d %H:%M:%S')
            self.updated_at = datetime.strptime(f'{args[3][0:10]} {args[3][11:19]}', '%Y-%m-%d %H:%M:%S')
            self.language = args[4]
            self.clone_url = args[5]

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return self.__name
    
    # makes it possible to compare two instances on a specific field. 
    # GREAT FOR EXAM!, example of python data model and magic methods
    def __eq__(self, other):
        return self.id == other
    
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id):
        self.__id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def created_at(self):
        return self.__created_at

    @created_at.setter
    def created_at(self, created_at):
        self.__created_at = created_at

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        self.__updated_at = updated_at

    @property
    def language(self):
        return self.__language

    @language.setter
    def language(self, language):
        self.__language = language

    @property
    def clone_url(self):
        return self.__clone_url

    @clone_url.setter
    def clone_url(self, clone_url):
        self.__clone_url = clone_url

    

'''
repo1 = Repository(12, 'test', '2020-01-07T23:52:44Z', '2020-01-07T23:53:56Z', 'Java', 'www.test.dk')
'''