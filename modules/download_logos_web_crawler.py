import requests, re, os
from contextlib import contextmanager    

def download_github_logos(base_dir_path):
    logo_urls = [element for img_tag in re.split('[<>]', requests.get('https://github.com/logos').text) if all(word in img_tag for word in ['img', 'src', 'logo']) for element in img_tag.split('"') if 'http' in element]

    os.chdir(f'{base_dir_path}/static')

    for count, url in enumerate(logo_urls):
        res = requests.get(url)
        with file_manager(f'logo_{count}.png', 'wb') as file:
            file.write(res.content)

    os.chdir('..')
    return logo_urls


@contextmanager
def file_manager(filename, mode):
    file = open(filename, mode)
    try:
        yield file
    finally:
        file.close()