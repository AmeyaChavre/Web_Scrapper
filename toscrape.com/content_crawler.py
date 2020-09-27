import requests
import bs4


result = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(result.text,"lxml")

author_list = []

for author in soup.select('span small'):
    author_list.append(author.text)
    
print(f"List of authors on first page : \n\n {set(author_list)}")
