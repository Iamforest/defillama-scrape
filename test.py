import requests
from bs4 import BeautifulSoup

#URL of the page I am scraping
URL = "https://realpython.github.io/fake-jobs/"

#Store the page using get
page = requests.get(URL)

# store the soup, this is what the webserver sent us.
soup = BeautifulSoup(page.content, 'html.parser')

#Results - this is the ID 
results = soup.find(id="ResultsContainer")
if results is None:
    print('results is EMPTY')
print(results.prettify())