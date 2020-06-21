import time, os


def timer_decorator(func):
    def wrapper(*args):
        start = time.time()
        func(*args)
        end = time.time()
        return ('%.2f' % (end-start))
    return wrapper

def folder_size_before_and_after(func):
    def wrapper(*args):
        start_size = find_size_of_folder()
        func(*args)
        end_size = find_size_of_folder()
        return {'start_size': start_size, 'end_size': end_size, 'difference': end_size-start_size}
    return wrapper

def find_size_of_folder(*args): 
        total_size = 0
        try:
            if len(args)==0:
                for element in os.listdir():

                    if os.path.isfile(element):
                        total_size += os.path.getsize(element)

                    elif os.path.isdir(element):
                        total_size += find_size_of_folder(element)
            else:
                for element in os.listdir(args[0]):
                    element_path = f'{args[0]}/{element}'

                    if os.path.isfile(element_path):
                        total_size += os.path.getsize(element_path)

                    elif os.path.isdir(element_path):
                        total_size += find_size_of_folder(element_path)

        except NotADirectoryError:
            if len(args)==0:
                return os.path.getsize()
            else:
                return os.path.getsize(args[0])

        return total_size

@timer_decorator
def looping():
    for i in range(1000000):
        if i % 100000 == 0:
            print(i)

@timer_decorator
def printing():
    time.sleep(0.0001)
    print("wauw")