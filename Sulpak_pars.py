from bs4 import BeautifulSoup
import requests


def save():
    with open('sulpak_comps.txt', 'a') as file:
        file.writelines(f"Название: {comp['title']}, Цена: {comp['price']}, Ссылка: {comp['link']}")


def parce():
    URL = 'https://www.sulpak.kg/f/noutbuki'
    HEADERS = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:89.0) Gecko/20100101 Firefox/89.0'
    }

    response = requests.get(URL, headers=HEADERS, verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='goods-tiles')
    comps = []
    print(items)

    for item in items:
        try:
            comps.append({'title': item.find('h3', class_='title').get_text(strip=True),
                          'price': item.find('div', class_='price').get_text(strip=True),
                          'link': URL + item.find('div', class_='product-container-right-side').find('a').get(
                              'href'), })
        except:
            pass

    global comp
    for comp in comps:
        print(f"Название :{comp['title']}, Цена: {comp['price']}, Ссылка: {comp['link']}")
        save()


parce()
