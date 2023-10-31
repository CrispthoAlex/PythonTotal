import bs4
import requests


url_base = 'https://books.toscrape.com/catalogue/page-{}.html'

result = requests.get(url_base.format('1'))  # just the page 1
soup = bs4.BeautifulSoup(result.text, 'lxml')

books_page_1 = soup.select('.product_pod')
print(len(books_page_1))  # 20 results

# print(books_page_1[0].select('.star-rating.Three'))
"""
[
    <p class="star-rating Three">
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
    <i class="icon-star"></i>
</p>
]
"""
# searching title from a book
catch_book_title = books_page_1[0].select('a')[1]['title']
print(catch_book_title)

# -------------------------------------------------------------------------
print('*' * 30)
print('books_high_rating')
print('*' * 30)
books_high_rating = []

# iterate the page
for page in range(1, 51):
    # create soup from each page
    url_page = url_base.format(page)
    result_page = requests.get(url_page)
    soup_page = bs4.BeautifulSoup(result_page.text, 'lxml')

    # select book data
    books = soup_page.select('.product_pod')

    # iterate books
    for book in books:
        # Check 4 or 5 stars
        if len(book.select('.star-rating.Four')) != 0 or len(book.select('.star-rating.Five')) != 0:
            # save title
            book_title = book.select('a')[1]['title']

            # add book to the list
            books_high_rating.append(book_title)

# see books with 4 or 5 rating
for t in books_high_rating:
    print(t)
"""
Sharp Objects
Sapiens: A Brief History of Humankind
The Dirty Little Secrets of Getting Your Dream Job
The Boys in the Boat: Nine Americans and Their Epic Quest for Gold at the 1936 Berlin Olympics
Shakespeare's Sonnets
Set Me Free
Scott Pilgrim's Precious Little Life (Scott Pilgrim #1)
Rip it Up and Start Again
Chase Me (Paris Nights #2)

...

Icing (Aces Hockey #2)
Having the Barbarian's Baby (Ice Planet Barbarians #7.5)
Giant Days, Vol. 1 (Giant Days #1-4)
Fruits Basket, Vol. 1 (Fruits Basket #1)
Deep Under (Walker Security #1)
Choosing Our Religion: The Spiritual Lives of America's Nones
Bright Lines
Bounty (Colorado Mountain #7)
Bleach, Vol. 1: Strawberry and the Soul Reapers (Bleach #1)
Ajin: Demi-Human, Volume 1 (Ajin: Demi-Human #1)
A Spy's Devotion (The Regency Spies of London #1)
1,000 Places to See Before You Die
"""

