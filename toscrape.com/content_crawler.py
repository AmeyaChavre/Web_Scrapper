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

page_url_list = []
for page_no in range(1,11):
    page_url_list.append(f"http://quotes.toscrape.com/page/{page_no}/")
#print(page_url_list)

all_authors_list = []
for page_url in page_url_list:
    page_result = requests.get(page_url)
    page_soup = bs4.BeautifulSoup(page_result.text,"lxml")
    for author_name in page_soup.select('span small'):
        all_authors_list.append(author_name.text)
print(f"There are {len(list(set(all_authors_list)))} author names found on all pages of website quotes.toscrape.com : {set(all_authors_list)}")
    
        
    

