import subprocess, os

import sys
sys.path.append('/Users/kramer/Documents/DAT18b/4_semester/python/exam/GitFlask/model')
sys.path.append('/Users/kramer/Documents/DAT18b/4_semester/python/exam/GitFlask/modules')
from my_decorators import folder_size_before_and_after
from my_decorators import timer_decorator

class GithubHandler:

    def __init__(self):
        self.has_executed_command = False
        self.time_spend = 0
        self.folder_size = 0
        self.response_message_from_command = ''

    @property
    def has_executed_command(self):
        return self.__has_executed_command

    @has_executed_command.setter
    def has_executed_command(self, has_executed_command):
        self.__has_executed_command = has_executed_command

    @property
    def time_spend(self):
        return self.__time_spend

    @time_spend.setter
    def time_spend(self, time_spend):
        self.__time_spend = time_spend

    @property
    def folder_size(self):
        return self.__folder_size

    @folder_size.setter
    def folder_size(self, folder_size):
        self.__folder_size = folder_size

    @property
    def response_message_from_command(self):
        return self.__response_message_from_command

    @response_message_from_command.setter
    def response_message_from_command(self, response_message_from_command):
        self.__response_message_from_command = response_message_from_command

    # change this to list comp if needed
    # RECURSIVE FUNCTION MIGHT BE GOOD FOR FUNCTION PART OF PRESENTATION
    # SAME FUNCTION BUT WITHOUT *args IS IN DECORATOR SCRIPT
    def find_size_of_folder(self, *args): 
        total_size = 0
        try:
            if len(args)==0:
                for element in os.listdir():

                    if os.path.isfile(element):
                        total_size += os.path.getsize(element)

                    elif os.path.isdir(element):
                        total_size += self.find_size_of_folder(element)
            else:
                for element in os.listdir(args[0]):
                    element_path = f'{args[0]}/{element}'

                    if os.path.isfile(element_path):
                        total_size += os.path.getsize(element_path)

                    elif os.path.isdir(element_path):
                        total_size += self.find_size_of_folder(element_path)

        except NotADirectoryError:
            if len(args)==0:
                return os.path.getsize()
            else:
                return os.path.getsize(args[0])

        return total_size

    @timer_decorator
    def clone_repo(self, clone_url):
        subprocess.run(['git', 'clone', clone_url])

    @folder_size_before_and_after
    def pull(self):
        subprocess.run(['git', 'pull'])

    def add_commit(self):
        subprocess.run(['git', 'add', '.'])
        self.response_message_from_command = subprocess.check_output(['git', 'commit', '-m', '"From git_flask_app.py"']).decode('utf-8').replace('\n', ' -')

    @timer_decorator
    def push(self):
        self.response_message_from_command = subprocess.check_output(['git', 'push'], stderr=subprocess.STDOUT).decode('utf-8').rstrip() #stderr=subprocess.STDOUT - sometimes it sends the 

    def fetch(self):
        subprocess.run(['git', 'fetch'])

g = GithubHandler()

