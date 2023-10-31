import bs4
import requests

url = "https://escueladirecta-blog.blogspot.com/2021/10/encapsulamiento-pilares-de-la.html"
result = requests.get(url)
print(type(result))
# <class 'requests.models.Response'>
# print(result.text)
"""
<!DOCTYPE html>
<html dir='ltr' lang='es' xmlns='http://www.w3.org/1999/xhtml' xmlns:b='http://www.google.com/2005/gml/b' xmlns:data='http://www.google.com/2005/gml/data' xmlns:expr='http://www.google.com/2005/gml/expr'>
<head>
<script id='mcjs'>!function(c,h,i,m,p){m=c.createElement(h),p=c.getElementsByTagName(h)[0],m.async=1,m.src=i,p.parentNode.insertBefore(m,p)}(document,"script","https://chimpstatic.com/mcjs-connected/js/users/cdd31299e4428f8ec89ab1c0f/7a1e6162b14a596c630033873.js");</script>
<meta content='width=device-width, initial-scale=1' name='viewport'/>
<title>Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python</title>
<meta content='text/html; charset=UTF-8' http-equiv='Content-Type'/>

...

_WidgetManager._RegisterWidget('_BlogArchiveView', new _WidgetInfo('BlogArchive1', 'sidebar_feed', document.getElementById('BlogArchive1'), {'languageDirection': 'ltr', 'loadingMessage': 'Cargando\x26hellip;'}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_LabelView', new _WidgetInfo('Label1', 'sidebar_feed', document.getElementById('Label1'), {}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_PopularPostsView', new _WidgetInfo('PopularPosts1', 'sidebar_item', document.getElementById('PopularPosts1'), {}, 'displayModeFull'));
_WidgetManager._RegisterWidget('_AttributionView', new _WidgetInfo('Attribution1', 'footer', document.getElementById('Attribution1'), {}, 'displayModeFull'));
</script>
</body>
</html>
"""

soup = bs4.BeautifulSoup(result.text, 'lxml')

print(soup.select('title'))
"""
[
    <title>Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python</title>
]
"""

print(soup.select('title')[0])
"""
<title>Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python</title>
"""

print(soup.select('title')[0].getText())
"""
Encapsulamiento - Pilares de la Programación Orientada a Objetos en Python
"""

special_p = soup.select('p')
print(special_p)
"""
[
    <p><span style="font-family: verdana;"><span style="background-color: white; color: #212338; font-size: 17px;">El</span><span style="background-color: white; color: #212338; font-size: 17px;"> </span><span style="box-sizing: inherit; color: #212338; font-size: 17px; font-weight: 700;">encapsulamiento</span><span style="background-color: white; color: #212338; font-size: 17px;"> </span><span style="background-color: white; color: #212338; font-size: 17px;">es el pilar de la programación orientada a objetos que se relaciona con</span><span style="box-sizing: inherit; color: #212338; font-size: 17px; font-weight: 700;"> ocultar al exterior determinados estados internos de un objeto</span><span style="background-color: white; color: #212338; font-size: 17px;">, tal que sea</span><span style="box-sizing: inherit; color: #212338; font-size: 17px; font-weight: 700;"> el mismo objeto quien acceda o los modifique</span><span style="background-color: white; color: #212338; font-size: 17px;">, pero que dicha acción</span><span style="background-color: white; color: #212338; font-size: 17px;"> </span><span style="box-sizing: inherit; color: #212338; font-size: 17px; font-weight: 700;">no se pueda llevar a cabo desde el exterior</span><span style="background-color: white; color: #212338; font-size: 17px;">, llamando a los métodos o atributos directamente.</span></span></p>,
    <p style="background-color: white; box-sizing: inherit; color: #212338; font-size: 17px; line-height: 30px; margin: 0px 0px 22px;"><span style="font-family: verdana;">Si bien en algunos lenguajes (como <em style="box-sizing: inherit;"><span style="box-sizing: inherit; font-weight: 700;">Java</span></em>), puede resultar un procedimiento habitual, <span style="box-sizing: inherit; font-weight: 700;">Python </span>no lo implementa por defecto, pero nos propone una vía alternativa para lograrlo. Esto se hace <span style="box-sizing: inherit; font-weight: 700;">anteponiendo dos guiones bajos (__)</span> al nombrar un método o atributo. De esa manera, los mismos quedarán definidos como “<em style="box-sizing: inherit;"><span style="box-sizing: inherit; font-weight: 700;">privados</span></em>”, y únicamente el mismo objeto podrá acceder a ellos.</span></p>,
    <p style="background-color: white; box-sizing: inherit; color: #212338; font-size: 17px; line-height: 30px; margin: 0px 0px 22px;"><span style="font-family: verdana;">Existe un pequeño truco <em style="box-sizing: inherit;">(no recomendado)</em> para acceder a los atributos y métodos ocultos. Dichos métodos están presentes con un nombre algo distinto:</span></p>,
    <p style="background-color: white; box-sizing: inherit; color: #212338; font-size: 17px; line-height: 30px; margin: 0px 0px 22px; text-align: center;"><span style="box-sizing: inherit; font-weight: 700;"><span style="font-family: verdana;">instancia + _ + NombreClase + método/atributo oculto</span></span></p>
]
"""

print(special_p[3])
"""
<p style="background-color: white; box-sizing: inherit; color: #212338; font-size: 17px; line-height: 30px; margin: 0px 0px 22px; text-align: center;"><span style="box-sizing: inherit; font-weight: 700;"><span style="font-family: verdana;">instancia + _ + NombreClase + método/atributo oculto</span></span></p>
"""
print(special_p[3].getText())
# instancia + _ + NombreClase + método/atributo oculto




