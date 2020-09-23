import requests
import bs4

#Insert any URL to count paragraph
 
formatted_html_text = bs4.BeautifulSoup((requests.get("https://en.wikipedia.org/wiki/Rocket")).text,"lxml")
 
count=0
for paragraph in range(len(formatted_html_text.select('p'))):
     print(f"Paragraph {count} : {formatted_html_text('p')[count].text}")
     count+=1
  
print(f"Paragraph count on : {formatted_html_text('title')[0].text} page : {count}")

#The Contents of Wikipedia Page
 
for content in formatted_html_text.select('.toclevel-1'):
     print(f"{content.text}")
    
res_image = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Soyuz_TMA-9_launch.jpg/800px-Soyuz_TMA-9_launch.jpg")

f = open('C:\\Users\\acer\\Desktop\\Web_Scrapper','wb+')
f.write(res_image.content)
f.close()



