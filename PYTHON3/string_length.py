def string_length(cadena):
    if  type(cadena) == str:
        return len(cadena)
    elif type(cadena) == int:
        return "Sorry integers don't have length"
    else:
        return "Sorry floats don't have length"



print(string_length("Hola "))
print(string_length(24))
print(string_length(24.1))
