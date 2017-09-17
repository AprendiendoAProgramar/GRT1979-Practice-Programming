def centuryFromYear(year):
    resultado = year // 100
    resto = year % 100
    if (resto == 0):
        return resultado
    else:
        resultado+=1
        return resultado