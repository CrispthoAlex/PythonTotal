import bs4
import requests


url = 'https://www.escueladirecta.com/courses'
result = requests.get(url)

soup = bs4.BeautifulSoup(result.text, 'lxml')

img_element = soup.select('img')
for img in img_element:
    print(img)
"""
[
    <img alt="Escuela Directa" src="https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=height:60/https://www.filepicker.io/api/file/UTNSPDfDQgurVa1kLkcC" srcset="https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=height:120/https://www.filepicker.io/api/file/UTNSPDfDQgurVa1kLkcC 2x"/>
    <img alt="" class="course-box-image" role="presentation" src="https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/136becbcea3e4d51abede23bf9794cf1/bcae2c4d38ac4953bd27a3d3be140893"/>
    <img alt="Federico Garay" class="img-circle" src="https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:30,height:30/https://www.filepicker.io/api/file/MGAWdJKaQqmQ2aMIRUbv"/>
    <img alt="Teachable" class="powered-by-logo" rel="noopener" src="https://fedora.teachablecdn.com/assets/footer/teachable-logomark-white-31d2296978598bacace50e6d48a2e1223c20a9b074af424acdd465676f81560f.svg" target="_blank"/>
]
"""

course_img = soup.select('.course-box-image')
for img in course_img:
    print(img)
"""
<img alt="" class="course-box-image" role="presentation" src="https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/136becbcea3e4d51abede23bf9794cf1/bcae2c4d38ac4953bd27a3d3be140893"/>
"""
image_1_url = course_img[0]['src']
print(image_1_url)
"""
https://process.fs.teachablecdn.com/ADNupMnWyR7kCWRvm76Laz/resize=width:705/https://file-uploads.teachablecdn.com/136becbcea3e4d51abede23bf9794cf1/bcae2c4d38ac4953bd27a3d3be140893
"""
course_image_1 = requests.get(image_1_url)
print(course_image_1)
# <Response [200]>
# print(course_image_1.content)
# ----binary file----

f = open('course_image_1.jpg', 'wb')
f.write(course_image_1.content)
f.close()
# check directory to find the image


