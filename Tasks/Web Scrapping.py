import requests
from bs4 import BeautifulSoup
r=requests.get('https://www.geeksforgeeks.org/python-programming-language/')
print(r)
cont=BeautifulSoup(r.content,'html.parser')
print(cont.prettify())
print(cont.title)
print(cont.title.name)
#Finding Elements by class
s=cont.find('div',class_='entry-content')
content=s.find_all('p')
print(content)
# Finding by id
s = cont.find('div', id= 'main')
leftbar = s.find('ul', class_='leftBarList')
content = leftbar.find_all('a')
print(content)
content = leftbar.find_all('li')
print(content)
#Removing the tags from the content of the page 
s = cont.find('div', class_='entry-content')
lines = s.find_all('p') 
for line in lines:
    print(line.text)
#removing tags from left side bar content
s = cont.find('div', id= 'main')
leftbar = s.find('ul', class_='leftBarList')
lines = leftbar.find_all('li') 
for line in lines:
    print(line.text)
    
s = cont.find('div', id= 'main')
leftbar = s.find('ul', class_='rightBarList')
lines = leftbar.find_all('li') 
for line in lines:
    print(line.text)
# to extract links
for link in cont.find_all('a'):
    print(link.get('href'))
#to 
titles = cont.find_all('div',attrs = {'class'})
print(titles)
# to extract imagex
images_list = []
images = cont.select('img')
for image in images:
    src = image.get('src')
    alt = image.get('alt')
    images_list.append({"src": src, "alt": alt})
     
for image in images_list:
    print(image)
