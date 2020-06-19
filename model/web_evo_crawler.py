import requests, re


######## GETS ONE LOGO URL ########
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

######## GETS ONE LOGO URL WITH LIST COMPREHENSION ########

class WebCrawlerV2:
    url = 'https://github.com/logos'

    # Download the html page and save it in a string
    res = requests.get(url)
    html = res.text

    logo_url = [element for html_line in html.splitlines() if 'github logomark' in html_line.lower() for element in html_line.split("\"") if 'http' in element]

wc2 = WebCrawlerV2

######## GETS MULTIPLE LOGO URLS WITH GENERATOR EXPRESSION ########
class WebCrawlerV3: 
    url = 'https://github.com/logos'

    # Download the html page and save it in a string
    res = requests.get(url)
    html = res.text

    logo_url = []

    def test_func(self):
        for html_line in self.html.splitlines():
            if all(word in html_line.lower() for word in ['logo', 'src', 'img']):
                for element in html_line.split('"'):
                    if 'http' in element:
                        self.logo_url.append(element)
                        

wc3 = WebCrawlerV3()

######## GETS MULTIPLE LOGO URLS WITH GENERATOR EXPRESSION AND LIST COMPREHENSION ########
class WebCrawlerV4:
    logo_url = [element for html_line in requests.get('https://github.com/logos').text.splitlines() if all(word in html_line.lower() for word in ['logo', 'src', 'img']) for element in html_line.split('"') if 'http' in element]

wc4 = WebCrawlerV4()


######## USES RE.SPLIT TO SPLIT ON TAGS '<>' INSTEAD OF LINES ########
######## GETS MULTIPLE LOGO URLS WITH GENERATOR EXPRESSION ########
class WebCrawlerV5:
    def test_func(self):
        url = 'https://github.com/logos'

        # Download the html page and save it in a string
        res = requests.get(url)
        html = res.text

        logo_url = [] 
    
        for img_tag in re.split('[<>]', html):
            if all(x in img_tag.lower() for x in ['logo', 'src', 'img']):
                for element in img_tag.split('"'):
                    if 'http' in element:
                        logo_url.append(element)
        
        return logo_url

wc5 = WebCrawlerV5()

######## USES RE.SPLIT TO SPLIT ON <> INSTEAD OF LINE ########
######## GETS MULTIPLE LOGO URLS WITH GENERATOR EXPRESSION AND LIST COMPREHENSION ########
class WebCrawlerV6:
    logo_url = [element for img_tag in re.split('[<>]', requests.get('https://github.com/logos').text) if all(word in img_tag for word in ['img', 'src', 'logo']) for element in img_tag.split('"') if 'http' in element]

    
wc6 = WebCrawlerV6()