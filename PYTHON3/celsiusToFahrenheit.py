def celsiusToFahrenheit(celsius):
    if celsius < -273.15:
        return "Imposible, estás dando una temperatura por debajo del 0 absoluto"
    else:
        fahrenheit = celsius * 9/5 + 32
        return fahrenheit

temperatures = [10, -20, -289, 100]

for temp in temperatures:
    print(celsiusToFahrenheit(temp))

    
