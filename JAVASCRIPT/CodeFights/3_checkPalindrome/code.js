function checkPalindrome(inputString) {
    var reverseStr = inputString.split("").reverse().join("");
    if (inputString == reverseStr){
        return true;
    } else {
        return false
    }
}