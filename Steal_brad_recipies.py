import requests
from bs4 import BeautifulSoup

# fetch the page content
url = 'https://lafoy.ru/keto-hleb-recepty-3923'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.prettify())

# extract product names, prices, and image URLs
bred_names = soup.find_all('h2', class_='tm8 post__title')
bred_ingridients = soup.find_all('p', attrs={'class': 'tm11 post__text'})
#bred_recipies = soup.find_all_next('p', class_='tm11 post__text')

counter = 0
for name in bred_names:
    print(f"Product: {name.text.strip()}")
    print(f"Recipie: {bred_ingridients[counter].text.strip()}")
    print(f"Recipie: {bred_ingridients[counter + 1].text.strip()}")
    if name.text.strip().startswith('8'):
        print(f"Recipie: {bred_ingridients[counter + 2].text.strip()}")
        counter += 1
    print("-" * 35)
    counter += 2



