import os, requests, subprocess
import repository as repo
import time

class Github:
    def __init__(self):
        self.__account_username = 'no name'
        self.__repo_info = [] 

    def __repr__(self):
        return self.__account_username

    def __str__(self):
        return self.__account_username

    def __len__(self):
        len(self.__repo_info)
    
    def __iter__(self):
        while True:
            yield self.__repo_info

    @property
    def account_username(self):
        return self.__account_username

    @account_username.setter
    def account_username(self, account_username):
        self.__account_username = account_username

    @property
    def repo_info(self):
        return self.__repo_info

    @repo_info.setter
    def repo_info(self, repo_info):
        self.__repo_info = repo_info

    def fetch_repo_info(self):
        '''
        # gets the full api from specified url and saves it in json format
        json_res = requests.get(f'https://api.github.com/users/{self.account_username}/repos').json()
        
        print(json_res)
        
        # list comp which
        self.repo_info = [repo.Repository(repository['name'], 
                                            repository['created_at'], 
                                            repository['updated_at'], 
                                            repository['language'], 
                                            repository['clone_url']) for repository in json_res]
        '''

        self.repo_info = [repo.Repository(repository['id'],
                                            repository['name'],  
                                            repository['created_at'], 
                                            repository['updated_at'], 
                                            repository['language'], 
                                            repository['clone_url']) for repository in requests.get(f'https://api.github.com/users/{self.account_username}/repos').json()]


    # generator function which returns a generator expression
    def repo_generator(self):
        # how it could be done
        '''
        for repository in repo_info:
            yield repository
        '''
        # how it should be done
        return (r for r in self.repo_info) 

    # Measure which method of this and the one below is more effective
    def find_repo_normal(self, id):
        for repository in self.repo_info:
            if repository == id:
                return repository

    def find_repo_with_gen(self, id):
        for repository in self.repo_generator():
            if repository == id:
                return repository


'''
git = Github()
git.account_username = '3520kramer'
git.fetch_repo_info()
'''



'''
# gets the full api from specified url
res = requests.get('https://api.github.com/users/3520kramer/repos')

# saves it in json format
json_res = res.json()

# list comprehension of all the users repos
#repos = [repo.Repository(res['name']) for res in json_res]
'''