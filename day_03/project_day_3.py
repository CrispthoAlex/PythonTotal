# input text
text_input = input("Type your text |>  ").lower()

# input letters
letter_1 = input("letter 1: ").lower()
letter_2 = input("letter 2: ").lower()
letter_3 = input("letter 3: ").lower()

# counting letters
# ----------------
# letter 1
nb_1 = text_input.count(letter_1)
# letter 2
nb_2 = text_input.count(letter_2)
# letter 3
nb_3 = text_input.count(letter_3)

# counting words
# ----------------
nb_words = len(text_input.split())

# first letter
# ----------------
first_ltr = text_input[0]

# last letter
# ----------------
last_ltr = text_input[-1]

# text inverse
# ----------------
text_reverse = text_input[::-1]

# find 'python' word
find_word = 'python' in text_input

show_result = {
    "text": text_input,
    "count_letters": {
        "letter_1": f"{letter_1}=> {nb_1} letters",
        "letter_2": f"{letter_2}=> {nb_2} letters",
        "letter_3": f"{letter_3}=> {nb_3} letters"
    },
    "count_words": f"# {nb_words} words",
    "first_letter": f"first letter=> {first_ltr}",
    "last_letter": f"last letter=> {last_ltr}",
    "text_inverse": f"Reverse=>\n{text_reverse}",
    "python_word": f"Have Python word? {find_word}"
}
"""Lo que aprenderás... Dominarás la programación profesional en Python. Crearás programas sólidos, avanzados y útiles. Trabajarás en programas del mundo real todos los días. Cada sección finaliza con un proyecto que podrás completar con lo aprendido en el día. Aplicarás Python en aplicaciones como: Juegos, Inteligencia Artificial, Machine Learning, Data Science, Gestión Administrativa y mucho más. Comprenderás la Programación Orientada a Objetos (OOP). Aprenderás con claridad los temas más complejos"""
print(f"Analize your text...\n{show_result['text']}\n"
      f"{show_result['count_letters']}\n"
      f"{show_result['count_words']}\n"
      f"{show_result['first_letter']}\n"
      f"{show_result['last_letter']}\n"
      f"{show_result['text_inverse']}\n"
      f"{show_result['python_word']}\n"
      )
"""
Analize your text...
lo que aprenderás... dominarás la programación profesional en python. crearás programas sólidos, avanzados y útiles. trabajarás en programas del mundo real todos los días. cada sección finaliza con un proyecto que podrás completar con lo aprendido en el día. aplicarás python en aplicaciones como: juegos, inteligencia artificial, machine learning, data science, gestión administrativa y mucho más. comprenderás la programación orientada a objetos (oop). aprenderás con claridad los temas más complejos
{'letter_1': 'o=> 39 letters', 'letter_2': 'q=> 2 letters', 'letter_3': 's=> 30 letters'}
# 70 words
first letter=> l
last letter=> s
Reverse=>
sojelpmoc sám samet sol dadiralc noc sárednerpa .)poo( sotejbo a adatneiro nóicamargorp al sárednerpmoc .sám ohcum y avitartsinimda nóitseg ,ecneics atad ,gninrael enihcam ,laicifitra aicnegiletni ,sogeuj :omoc senoicacilpa ne nohtyp sáracilpa .aíd le ne odidnerpa ol noc ratelpmoc sárdop euq otceyorp nu noc azilanif nóicces adac .saíd sol sodot laer odnum led samargorp ne sárajabart .selitú y sodaznava ,sodilós samargorp sáraerc .nohtyp ne lanoiseforp nóicamargorp al sáranimod ...sárednerpa euq ol
Have Python word? True
"""


