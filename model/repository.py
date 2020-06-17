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
            #self.created_at = datetime.strptime(f'{args[2][0:10]} {args[2][11:19]}', '%Y-%m-%d %H:%M:%S')
            #self.updated_at = datetime.strptime(f'{args[3][0:10]} {args[3][11:19]}', '%Y-%m-%d %H:%M:%S')
            self.created_at = args[2]
            self.updated_at = args[3]
            self.language = args[4]
            self.clone_url = args[5]

    def __repr__(self):
        return f'{self.__dict__}'

    def __str__(self):
        return self.__name

    # GREAT FOR EXAM
    def __iter__(self):
        for value in self.__dict__.values():
            yield value          
    
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

    # research try/except and see if it can be used
    @created_at.setter
    def created_at(self, created_at):
        try:
            self.__created_at = datetime.strptime(f'{created_at[0:10]} {created_at[11:19]}', '%Y-%m-%d %H:%M:%S')
        except TypeError:
            self.__created_at = created_at
        

    @property
    def updated_at(self):
        return self.__updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        try:
            self.__updated_at = datetime.strptime(f'{updated_at[0:10]} {updated_at[11:19]}', '%Y-%m-%d %H:%M:%S')
        except TypeError:
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

repo1=Repository()
repo1.created_at = '2020-01-07T23:52:44Z'
repo1.updated_at = '2020-01-07T23:52:44Z'