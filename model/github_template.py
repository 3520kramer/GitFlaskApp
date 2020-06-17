import os, requests, subprocess

username = input('Which user do you want to download from? ')

# gets the full api from specified url
res = requests.get('https://api.github.com/users/' + username + '/repos')

# saves it in json format
json_res = res.json()


# saves the length of the json file to find how many repos
json_length = len(json_res)

# creates list to save url's to clone from and saves each url in the json_res in the list
clone_url = []
for i in range(json_length):
    clone_url.append(json_res[i]['clone_url'])

print(clone_url)

# creates folder to save cloned url and change into it
os.mkdir('cloned_repos')
os.chdir('cloned_repos')

# run the command to clone the repos
for url in clone_url:
    subprocess.run(['git', 'clone', url])
