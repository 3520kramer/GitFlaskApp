import requests, re, os
from contextlib import contextmanager

def download_github_logos():
    logo_urls = [element for img_tag in re.split('[<>]', requests.get('https://github.com/logos').text) if all(word in img_tag for word in ['img', 'src', 'logo']) for element in img_tag.split('"') if 'http' in element]
    
    for count, url in enumerate(logo_urls):
        res = requests.get(url)
        with file_manager(f'logo_{count}.png', 'wb') as file:
            file.write(res.content)
    

@contextmanager
def file_manager(filename, mode):
    os.chdir('static')
    file = open(filename, mode)
    try:
        yield file
    finally:
        os.chdir('..')
        file.close()