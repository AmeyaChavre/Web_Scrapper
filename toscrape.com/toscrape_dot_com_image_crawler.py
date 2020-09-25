import requests
import bs4

count = 0
url_list = []
for page_urls in range(50):
    count+=1
    url_list.append(f"http://books.toscrape.com/catalogue/page-{count}.html")
#print(url_list)

img_url_list=[]
for url in url_list:
    img_req = requests.get(url)
    soup_of_img = bs4.BeautifulSoup(img_req.text,"lxml")
    for url_src in soup_of_img.select('img'):
        img_url_list.append(url_src['src'])
print(f"Total Images found on Website : {len(img_url_list)}")

img_full_url=[]

for img_url in img_url_list:
    img_full_url.append("http://books.toscrape.com"+str(img_url[2:]))
#print(img_full_url)
print("All image url's extracted from toscrape.com")

file_count=0
for image_address in img_full_url:
    download_image = requests.get(image_address)
    file_count+=1
    file = open(f"D:\\Scrapped_Images\\file_{file_count}.jpg",'wb')
    file.write(download_image.content)
    file.close()
print(f"All {file_count} images have been downloaded")
    

    
    



