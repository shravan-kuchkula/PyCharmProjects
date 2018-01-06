# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url
#url = 'http://www.dice.com/job/result/10377914/BD52369852?src=19'
url = 'http://www.dice.com/job/result/cybercod/CS10-137318512?src=19'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extracts the response as html: html_doc
html_doc = r.text

# create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Print the title of Guido's webpage
#pretty_soup = soup.prettify()

#print(pretty_soup)

# find all 'p' tags
p_tags = soup.find_all('p')

for tag in p_tags:
    print(tag.text)
