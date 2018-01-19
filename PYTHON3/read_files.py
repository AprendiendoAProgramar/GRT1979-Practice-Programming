#Printar todos los elementos del fichero
file = open("fruits.txt", "r")
content = file.read()
file.close()
print(content)
print(type(content))

#Printar longitud de cada ítem del fichero
# file = open("fruits.txt", "r")
# content = file.readlines()
# file.close()
# for i in content:
#      print(len(i) - 1)
