from urllib.request import urlopen
from bs4 import BeautifulSoup

# specify the url
url = "https://usedcars.audi.co.uk/usedcar/audi/s4/s4-saloon/url-1_15-list.htm#/i/s|10,AABF|1024,53.08828,-2.96093,100,TEwxMiA4WHU/l|12,1,t_geo,U"

# Connect to the website and return the html to the variable ‘page’
try:
    page = urlopen(url)
except:
    print("Error opening the URL")

# parse the html using beautiful soup and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the <div> of name and get its value
content = soup.find('div', {"class": "details"})

print(content)
article = ''
for i in content.findAll('strong'):
    article = article + ' ' +  i.text
print(article)

# Saving the scraped text
# with open('scraped_text.txt', 'w') as file:
#     file.write(article)