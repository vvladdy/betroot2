import re

from bs4 import BeautifulSoup
import requests
import json
import csv
from pandas import DataFrame

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0"
                  "Safari/537.36"
}

def collect_nout(url='https://rozetka.com.ua/notebooks/c80004/'):
    with requests.Session() as session:

        response = session.get(url, timeout=10)

        assert response.status_code == 200, 'Bad response'
        print(response.status_code)

    response = requests.get(url=url, headers=headers)
    soup = BeautifulSoup(response.text, 'lxml')
    page_count = int(soup.find('div', class_="pagination "
                                             "ng-star-inserted").find_all(
        'li', class_="pagination__item ng-star-inserted")[-1].text.strip())
    print(f'Total page for parsing {page_count}...')

    products, price = (), 0

    for page in range(1, page_count + 1):
        print(f'Обработка {page} страницы...')
        url = f'https://rozetka.com.ua/notebooks/c80004/page={page}/'
        response = requests.get(url=url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        items = soup.find_all('li', class_='catalog-grid__cell '
                            'catalog-grid__cell_type_slim ng-star-inserted')

        for it in items:
            title = it.find('a', class_="goods-tile__picture "
                    "ng-star-inserted").find('img').get('alt').strip()

            # title = it.find('a', class_ = 'goods-tile__heading '
            #                 'ng-star-inserted').text.strip()
            link = it.find('a', class_='goods-tile__heading '
                            'ng-star-inserted').get('href').strip()
            try:
                pricefull = it.find('div', class_="goods-tile__price "
                    "ng-star-inserted").find(
                    'p', class_="ng-star-inserted").find('span', class_=
                "goods-tile__price-value").text.strip()
            except:
                pricefull = 0  # 'Not price'

            try:
                pricered = it.find('div', class_="goods-tile__price "
                    "price--red ng-star-inserted").find('p', class_=
                    "ng-star-inserted").find('span', class_=
                    "goods-tile__price-value").text.strip()
                intpricered = ' '.join(re.findall(r'\d+', pricered))
            except:
                pricered = 'Net skidki'

            try:
                pricegrey = it.find('div', class_="goods-tile__price--old "
                            "price--gray ng-star-inserted").text.strip()
                intpricegrey = ' '.join(re.findall(r'\d+', pricegrey))
            except:
                pricegrey = 'Net skidki'

            imglink = it.find('a', class_="goods-tile__picture "
                            "ng-star-inserted").find('img')['src']

            if pricefull != 0:
                price = pricefull
            if pricefull == 0:  # 'Not price':
                price = int(intpricered.replace(' ', ''))

            print('Описание: ', title)
            print('Ссылка на продукт: ', link)
            print('Цена: ', price),
            print('Цена до скидки: ', intpricegrey),
            # print('Цена со скидкой: ', (pricered, intpricered))
            # print('Цена полная: ', pricefull)
            print('Ссылка на фото: ', imglink)

            products += ({
                             'title': title,
                             'link': link,
                             'price': price,
                             'price before': intpricegrey,
                             'imglink': imglink
                         },)
    return products


def main():
    # print(collect_nout())

    with open('rozetka.json', 'w') as file:
        json.dump(collect_nout(), file, indent=4)

    # df = DataFrame(collect_nout(), columns=['title', 'link',
    #                            'price', 'imglink'])
    # df.to_csv(r'rozetka.csv', header=True)


if __name__ == '__main__':
    main()
