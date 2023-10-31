import bs4
import requests

"""
toscrape.com allows to enjoy web scraping
"""
url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

for n in range(1, 11):
    print(url_base.format(n))
"""
https://books.toscrape.com/catalogue/page-1.html
https://books.toscrape.com/catalogue/page-2.html
https://books.toscrape.com/catalogue/page-3.html
https://books.toscrape.com/catalogue/page-4.html
https://books.toscrape.com/catalogue/page-5.html
https://books.toscrape.com/catalogue/page-6.html
https://books.toscrape.com/catalogue/page-7.html
https://books.toscrape.com/catalogue/page-8.html
https://books.toscrape.com/catalogue/page-9.html
https://books.toscrape.com/catalogue/page-10.html
"""




