import json
import requests
import bs4

URL = 'https://upl.uz'

response = requests.get(URL)
response.raise_for_status()

site_html = response.text



soup = bs4.BeautifulSoup(site_html, 'html.parser')

content = soup.find('div', id='upl-content')




items = content.find_all('div', {'class': 'sh-news'})
result = []
for item in items:
    title = item.find('h2', class_='sh-title').get_text()
    href = item.find('a')['href']
    img = item.find('img')['data-src']
    side_date = item.find('div', class_='side-date').find('span').get_text()
    text = item.find('div', class_='sh-text').next.get_text()\


    inner_page = requests.get(href)
    inner_page.raise_for_status()
    inner_soup = bs4.BeautifulSoup(inner_page.text, 'html.parser')

inner_data = []
side_block = inner_soup.find_all('div', {'class': 'side-block'})
inner_items = side_block.find_all('a')
for i in inner_items:
    t = i.find('div', class_='b-title').get_text
    sd = i.find('div', class_='side-date').find_all('span')
    time = sd[0].get_text()
    reviews = sd[1].get_text()

    inner_data.append({
        'title': t,
        'time': time,
        'reviews': reviews
    })

    result.append({
        'title': title,
        'img': img,
        'href': href,
        'date': side_date,
        'text': text
    })

print(result)



with open('data.json', 'w', encoding='utf-8') as file:
    json.dump(result, file, indent=4, ensure_ascii=False)
