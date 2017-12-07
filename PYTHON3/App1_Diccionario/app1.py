import json
from difflib import get_close_matches
data  = json.load(open("data.json"))
def translate(word):
    word = word.lower()
    word_1 = word
    word_1 = word_1[0].upper() +  word_1[1:]
    word_2 = word.upper()
    if word in data:
        return data[word]
    elif word_1 in data:
        return data[word_1]
    elif word_2 in data:
        return data[word_2]
    elif len(get_close_matches(word,data.keys())) > 0:
        response = input("¿Quizás querías decir %s? Introduce S si es Sí y N si es No: " % get_close_matches(word,data.keys())[0])
        if response == "S":
            return data[get_close_matches(word,data.keys())[0]]
        elif response == "N":
            return "Por favor vuelve a revisar la palabra que quieres encontrar"
        else:
            return "Opción no válida"
    else:
        return "Palabra no encontrada en el diccionario"

word = input ("Introduce una palabra para buscar en el diccionario: ")

output = translate(word)

if type(output) == list:
    for item in output:

        print(item)
else:
    print(output)
