import requests, re

class WebCrawlerV1:

    url = 'https://github.com/logos'

    # Download the html page and save it in a string
    res = requests.get(url)
    html = res.text

    # Split html to lines to find 
    html_splitted = html.splitlines()

    logo_url = ''

    for html_line in html_splitted:
        if 'github logomark' in html_line.lower():
            for element in html_line.split('"'):
                if 'http' in element:
                    logo_url = element

wc1 = WebCrawlerV1


class WebCrawlerV2:
    url = 'https://github.com/logos'

    # Download the html page and save it in a string
    res = requests.get(url)
    html = res.text

    logo_url = [element for html_line in html.splitlines() if 'github logomark' in html_line.lower() for element in html_line.split("\"") if 'http' in element]

wc2 = WebCrawlerV2

'''
class WebCrawlerV3:
    url = 'https://github.com/logos'

    # Download the html page and save it in a string
    res = requests.get(url)
    html = res.text

    logo_url = ''

    for something in html.splitlines():
        if all(x in something.lower() for x in ['logo', 'src', 'mark']):
            print('TRUEEEEE')

    for html_line in html.splitlines():
        if all(x in html_line.lower() for x in ['logo', 'src', 'mark']):
            print('---')
            print(html_line)
            print('---')
            for element in html_line.split('"'):
                if 'http' in element:
                    logo_url = element
                    print(element)
'''


class WebCrawlerV4:
    logo_url = [element for html_line in requests.get('https://github.com/logos').text.splitlines() if all(word in html_line.lower() for word in ['logo', 'src', 'mark']) for element in html_line.split('"') if 'http' in element]


class WebCrawlerV5:
    logo_url = [element for img_tag in re.split('[<>]', requests.get('https://github.com/logos').text) if all(word in img_tag for word in ['img', 'src', 'logo']) for element in img_tag.split('"') if 'http' in element]

    #if all(x in html_line.lower() for x in ['logo', 'src', 'mark'])

    # Download the html page and save it in a string
    html_ = "<inde i krokodille 1> hej hej <inde i krokodille 2> < ikke lukket <inde i en lukket>"
    html_splitted = re.split('[<>]', html_)

    
wc5 = WebCrawlerV5()

class WebCrawlerV6:
    url = 'https://github.com/logos'

    # Download the html page and save it in a string
    res = requests.get(url)
    html = res.text.splitlines()

    logo_url = ''

    #if all(word in line for word in ['logo', 'src', 'logo'] for line in html):
    #    print('yes')

    a_string = "A string is more than its parts!"
    matches = ["more", "wholesome", "milk"]

    if any(x in a_string for x in matches): 
        print('WTF')

wc6 = WebCrawlerV6()