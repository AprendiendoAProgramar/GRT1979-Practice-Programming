def adjacentElementsProduct(inputArray):
    result = -1000
    result_temp = 0
    longitud = len(inputArray)
    longitud-=1
    for i in range (0,longitud):
        result_temp = inputArray[i] * inputArray[i+1]
        if result < result_temp:
            result = result_temp
            
    return result