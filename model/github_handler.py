from modules.timer import timer_decorator
import subprocess, os
from hurry.filesize import size

class GithubHandler:

    def __init__(self):
        self.has_executed_command = False
        self.time_spend = 0
        self.folder_size = 0

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
        self.__folder_size = self.format_size(folder_size)

    # change this to list comp if needed
    def find_size_of_folder(self, folder_name): 
        total_size = 0
        try:
            for element in os.listdir(folder_name):
                element_path = f'{folder_name}/{element}'

                if os.path.isfile(element_path):
                    total_size += os.path.getsize(element_path)

                elif os.path.isdir(element_path):
                    total_size += self.find_size_of_folder(element_path)

        except NotADirectoryError:
            return os.path.getsize(folder_name)
        '''
        except PermissionError:
            total_size += 0
        '''
        return total_size

    def format_size(self, size_in_bytes):
        my_system = [
            (1024 ** 3, ' tb'),
            (1024 ** 2, ' gb'),            
            (1024 ** 1, ' mb'),
            (1024 ** 0, ' bytes')
        ]
        return size(size_in_bytes, system=my_system)

    @timer_decorator
    def clone_repo(self, clone_url):
        subprocess.run(['git', 'clone', clone_url])

    @timer_decorator
    def looping(self):
        for i in range(1000000):
            if i % 100000 == 0:
                print(i)


g = GithubHandler()