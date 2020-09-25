import requests
import bs4

#Insert any URL to count paragraph
  
formatted_html_text = bs4.BeautifulSoup((requests.get("https://en.wikipedia.org/wiki/Rocket")).text,"lxml")
  
count=0
for paragraph in range(len(formatted_html_text.select('p'))):
      #print(f"Paragraph {count} : {formatted_html_text('p')[count].text}")
      count+=1
   
print(f"Paragraph count on : {formatted_html_text('title')[0].text} page : {count}")
 
#The Contents of Wikipedia Page
  
for content in formatted_html_text.select('.toclevel-1'):
      print(f"{content.text}")
    
#Download all images in a Wikipedia Page

req_for_image = requests.get("https://en.wikipedia.org/wiki/Rocket")

soup = bs4.BeautifulSoup(req_for_image.text,"lxml")

print(f"There are {len(soup.select('.thumbimage'))} images on webpage.")

list_of_tags = list(soup.select('.thumbimage'))

extract_src = []

for tags in list_of_tags:
    extract_src.append(tags['src'])
#print(extract_src)

url_list=[]

for src in extract_src:
    
    url_list.append("https:"+str(src))
#print(url_list)

count=0
for url in url_list:
    download_image = requests.get(url)
    count+=1
    file = open(f"C:\\Users\\acer\\Desktop\\file_{count}.jpg",'wb')
    file.write(download_image.content)
    file.close()
print(f"All {count} images have been downloaded")
    
    


