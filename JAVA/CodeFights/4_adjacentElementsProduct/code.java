int adjacentElementsProduct(int[] inputArray) {
    int result = -1000;
    int result_temp = 0;
    int longitud = inputArray.length;
    for (int i = 0; i <= (longitud-2); i++)
    {
        result_temp = inputArray[i] * inputArray[i+1];
        if (result < result_temp)
        {
            result = result_temp;
        }
    }
    return result;