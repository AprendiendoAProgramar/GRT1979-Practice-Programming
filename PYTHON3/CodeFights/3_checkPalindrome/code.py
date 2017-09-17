def checkPalindrome(inputString):
    if len(inputString) == 1:
        return True
    index_min = 0
    index_max = len(inputString)
    index_max -=1
    print(inputString[0])
    result = False
    while index_min <= index_max :
        if inputString[index_min] == inputString[index_max]:
            result = True
            index_min +=1
            index_max -=1
        else:
            result = False
            break
    return result