import bs4
import requests

url = "https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html"
result = requests.get(url)
print(type(result))
# <class 'requests.models.Response'>

soup = bs4.BeautifulSoup(result.text, 'lxml')

special_p = soup.select('p')
print(special_p[3].getText())
# instancia + _ + NombreClase + método/atributo oculto

post_title = soup.select('div .post-title')
print(len(post_title))
# 4
for idx, p in enumerate(post_title):
    print(f'{idx} - {p.getText()}')
"""
0 - 



Configurando la Impresión Perfecta de un Libro de Excel





1 - 
Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python

2 - Cohesión - Pilares de la Programación Orientada a Objetos en Python
3 - Acoplamiento - Pilares de la Programación Orientada a Objetos en Python
"""


