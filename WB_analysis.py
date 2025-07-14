import requests
from datetime import datetime
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px

arr = []

query_list = [
    'лонгслив женский оверсайз',
    'лонгслив женский'
]

max_page = 3
brand = 'ТЕЛОДВИЖЕНИЯ'

for query in query_list:
  for page in range(1, max_page + 1):
    res = requests.get(
      f"https://search.wb.ru/exactmatch/ru/female/v9/search?ab_testing=false&appType=64&curr=rub&dest=123585762&hide_dtype=13&lang=ru&page={page}&query={query}&resultset=catalog&sort=popular"
    )
    for card in res.json()['data']['products']:
      if card.get('log') and card['brand'] == brand:
        arr.append([
            card['log']['position'],
            card['log']['promoPosition'],
            datetime.now(),
            query,
            card['name']
        ])
    print(f"query: {query} page: {page}")

df = pd.DataFrame(arr)

df.columns = ['position', 'promo_position', 'created_at', 'query', 'name']

df['diff'] = df['position'] - df['promo_position']
df['hour'] = df['created_at'].dt.hour
df['date'] = df['created_at'].dt.date
df1 = df[df['name'] == 'Лонгслив женский оверсайз с длинным рукавом']

plt.plot(df1['position']);
print(df)


pd.pivot_table(
    df1,
    index='query',
    columns='hour',
    values='promo_position',
    aggfunc='mean',
    fill_value=0
)

px.line(df1['position'])