import requests
from bs4 import BeautifulSoup

# fetch the page content
url = 'https://lafoy.ru/makarony-s-syrom-v-duhovke-recepty-4384'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')


# extract product names, prices, and image URLs
bred_names = soup.find_all('h2', class_='tm8 post__title')
bred_ingridients = soup.find_all('p', attrs={'class': 'tm11 post__text'})

counter = 0
biggers = ["1."] #, "2.", "4.", "6.", "7.", "8."]
for name in bred_names:
    print(f"Название: {name.text.strip()}")
    print(f"Ингридиенты: {bred_ingridients[counter].text.strip()}")
    print(f"Рецепт: {bred_ingridients[counter + 1].text.strip()}")
    for i in biggers:
        if name.text.strip().startswith(i):
            print(f"{bred_ingridients[counter + 2].text.strip()}")
            counter += 1
    print("-" * 35)
    counter += 2



