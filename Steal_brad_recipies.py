import requests
from bs4 import BeautifulSoup

# fetch the page content
url = 'https://lafoy.ru/sup-iz-svinyh-rebryshek-recepty-3723'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.prettify())

# extract product names, prices, and image URLs
bred_names = soup.find_all('h2', class_='tm8 post__title')
bred_ingridients = soup.find_all('p', attrs={'class': 'tm11 post__text'})

counter = 0
biggers = ["3.", "4.", "5.", "11.", "12."] #, "8."]
giggers = ["8.", "220."] #, "11."]
exclusion = "400."
for name in bred_names:
    if not name.text.strip().startswith(exclusion):
        print(f"Название: {name.text.strip()}")
        print(f"Ингридиенты: {bred_ingridients[counter].text.strip()}")
        print(f"Рецепт: {bred_ingridients[counter + 1].text.strip()}")
        for i in biggers:
            if name.text.strip().startswith(i):
                print(f"{bred_ingridients[counter + 2].text.strip()}")
                counter += 1
        for i in giggers:
            if name.text.strip().startswith(i):
                print(f"{bred_ingridients[counter + 2].text.strip()}")
                print(f"{bred_ingridients[counter + 3].text.strip()}")
                counter += 2
        print("-" * 35)
        counter += 2
    else:
        counter += 1



