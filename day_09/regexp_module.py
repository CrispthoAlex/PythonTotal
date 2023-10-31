import re


text = ('The Jungle Book is a collection of stories by Rudyard Kipling, published in 1894. The stories tell mostly of Mowgli, an Indian boy who is raised by wolves and learns self-sufficiency and wisdom from the jungle animals.')
# Option 1
# ----------------------------------
word = 'Mowgli'
print(word in text)
# True


# Option 2
# ----------------------------------
word1 = 'USA'
word2 = 'Indian'
searching = re.search(word1, text)
print(searching)
# None
searching = re.search(word2, text)
print(searching)
# <re.Match object; span=(120, 126), match='Indian'>
print(searching.span())
# (120, 126)
print(searching.start())
# 120
print(searching.end())
# 126

word3 = "The"
searching = re.findall(word3, text)
print(searching)
# ['The', 'The']
for word in re.finditer(word3,  text):
    print(word.span())
"""
(0, 3)
(82, 85)
"""

text2 = "Ask for help calling to 570-384-0203"
pattern = r'\d{3}-\d{3}-\d{4}'  # r'\d\d\d-\d\d\d-\d\d\d\d'
result = re.search(pattern, text2)
print(result)
# <re.Match object; span=(24, 36), match='570-384-0203'>
print(result.span())
# (24, 36)
print(result.group())
# 570-384-0203

pattern = re.compile(r'(\d{3})-(\d{3})-(\d{4})')  # r'\d\d\d-\d\d\d-\d\d\d\d'
result = re.search(pattern, text2)
print(result.group(1))
# 570
print(result.group(2))
# 384
print(result.group(3))
# 0203

password = "2edfhjkl"  # input('Type your password: ')
# first character will be a letter and seven (7) chars (ltr or num)
pattern = r'\D{1}\w{7}'

check_pass = re.search(pattern, password)
print(check_pass)
"""
> 2edfhjkl
None
> tyyuu
None
> e98mnbgt
<re.Match object; span=(0, 8), match='e98mnbgt'>
"""

text3 = """The Jungle Book is a classic coming-of-age story about a boy who must learn to find his place in the world. 
It is also a story about the importance of family, friendship, and courage.
"""
# search family or friendship
searching = re.search(r'family|friendship', text3)
print(searching)
# <re.Match object; span=(153, 159), match='family'>

searching = re.search(r'families|friendship', text3)
print(searching)
# <re.Match object; span=(161, 171), match='friendship'>

searching = re.search(r'families|enemies', text3)
print(searching)
# None

# partial word, use wildcard
searching = re.search(r'......ory.......', text3)
print(searching)
# <re.Match object; span=(40, 56), match='age story about '>

# verify the start char
searching = re.search(r'^\D', text3)
print(searching)
# <re.Match object; span=(0, 1), match='T'>

text4 = '45 years old'
searching = re.search(r'^\d', text4)
print(searching)
# <re.Match object; span=(0, 1), match='4'>

# verify the end char
searching = re.search(r'\D$', text3)
print(searching)
# <re.Match object; span=(183, 184), match='.'>

text4 = 'Was it a time ago? 87'
searching = re.search(r'\d$', text4)
print(searching)
# <re.Match object; span=(20, 21), match='7'>

searching = re.findall(r'[^\s]', text4)
print(searching)
# [
#   'W', 'a', 's', 'i', 't', 'a', 't', 'i', 'm', 'e',
#   'a', 'g', 'o', '?', '8', '7'
# ]

searching = re.findall(r'[^\s]+', text4)
print(searching)
# ['Was', 'it', 'a', 'time', 'ago?', '87']
print('-'.join(searching))
# Was-it-a-time-ago?-87


# -----------------------------------------------------------------------------
def verify_email(email):
    check = re.search(r'\w+@\w+\.\w+', email)
    if check is not None:
        print("Ok")
    else:
        print("email address is  not correct")


verify_email("hello@br.com")
# Ok
verify_email("hello@brcom")
# email address is  not correct


def verify_greetings(salute):
    check = re.search(r'^Hello', salute)
    if check is not None:
        print("Ok")
    else:
        print("Not greetings")


greeting = 'Hello everyone'
greeting2 = 'Everyone, good morning'
verify_greetings(greeting)
verify_greetings(greeting2)


def verify_cp(cp):
    check = re.search(r'\w{2}\d{4}', cp)
    if check is not None:
        print("Ok")
    else:
        print("Postal Code is not correct")


verify_cp('AB7626')
verify_cp('#C0099')
