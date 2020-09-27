import requests
import bs4


result = requests.get("http://quotes.toscrape.com/")
soup = bs4.BeautifulSoup(result.text,"lxml")

author_list = []

for author in soup.select('span small'):
    author_list.append(author.text)
    
print(f"List of authors on first page : \n\n {set(author_list)} \n\n")

quotes_list = []
for quotes in soup.select('.text'):
    quotes_list.append(quotes.text)
print(f"List of quotes on first page : \n\n {quotes_list} \n\n")

tag_list=[]

for tags in soup.select('.tag-item a'):
    tag_list.append(tags.text)
print(f"List of Top 10 tags on first page : \n\n {tag_list} \n\n")
    

