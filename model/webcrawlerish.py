# Create an application that asks for an url. 
# Then Download that html page, and its images, icons etc. and change it so it will work locally on your computer. Locally means that you should be able to cut your internet connection and still have a functionig html page. 
# when done push all files to you github account. (you are allowed to manualy create an online repo and feed the clone url to your program. but the rest should be done through python).

# You will have to use the requests module, the OS module and the subprocesses module for this taks.

import requests, os, subprocess

# Ask for url
#url = input("What URL do you want to save locally? ")
url = 'http://wikipedia.dk/' # FOR TESTING

# Create a name for directory
directory_name = url.split('//')[1]

# Make a directory and change into it
#os.rmdir(directory_name) # FOR TESTING
os.mkdir(directory_name)
os.chdir(directory_name)

# Download the html page and save it in a string
res = requests.get(url)
html = res.text

# Search the string for possible scripts and icons to download (href)
links_to_download = []
html_splitted = html.splitlines(True)

for line in html_splitted:
    # for pics and css
    if 'link' in line and 'href' in line:
        #print(line)
        splitted_link = line.split('"')
        links_to_download.append(splitted_link[splitted_link.index(' href=')+1])
        
    # for javascript
    elif 'script' in line and 'src' in line:
        #print(line)
        splitted_link = line.split('"')
        links_to_download.append(splitted_link[splitted_link.index('\t<script src=')+1])
    
    elif 'img src' in line:
        print(line)

        splitted_link = line.split('"')
        links_to_download.append(splitted_link[splitted_link.index('<img src=')+1])



print('links to download:',links_to_download)
count = 0
# Download scripts and pics
# Loop doesn't change the content of links_to_download list, it only modifies it in the loop
for link in links_to_download:
    # Check if url is full or not, and if not, prepend the url from user input
    if link[:4] != 'http':
        # modifies the link to be a complete URL
        file_name = link
        link = url + link
        print('link i if:', link)
    else:
        print('link i else:', link)
        # Split link by '/' and save the last index in array as filename
        file_name = link.split('/')[-1]
        print('file_name i else', file_name)
        print('find:', html.find(link))
        
        # replace the original link in the html with the filename which is also the path
        html = html.replace(link, file_name)

        #print("filename:", file_name)
    count += 1

    res = requests.get(link)
    file = open(file_name, 'wb').write(res.content)

'''
for l in links_to_download:
    print(l)
    res = requests.get(l)
    file = open(file_name, 'wb').write(res.content)'''

# Write the html to a file
html_name = directory_name.split('.')[0] + '.html'
file = open(html_name, 'w')
file.write(html)

# Lav funktion der tjekker fil, og tjekker hvad content der downloades
