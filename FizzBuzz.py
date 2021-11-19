startRange = 1
print("Input the maximum number")
endRange = int(input())

def isDivisibleBySecondNumber(number, secondNumber):
    return number % secondNumber == 0

def appendWordBeforeBWord(originalWordArr, appendWord):
    if len(originalWordArr) != 0:
        bWordIndex = 0
        
        for word in originalWordArr:
            if word[0] == "B":
                bWordIndex = originalWordArr.index(word)
                break
        
        originalWordArr.insert(bWordIndex, appendWord)
    else:
        originalWordArr.append(appendWord)

    return originalWordArr      


for i in range(startRange, endRange + 1):
    word = ""
    wordArr = []

    if isDivisibleBySecondNumber(i, 3):
        wordArr.append("Fizz")
    if isDivisibleBySecondNumber(i, 5):
        wordArr.append("Buzz")
    if isDivisibleBySecondNumber(i, 7):
        wordArr.append("Bang")
    if isDivisibleBySecondNumber(i, 11):
        wordArr = [ "Bong" ]
    if isDivisibleBySecondNumber(i, 13):
        appendWordBeforeBWord(wordArr, "Fezz")
    if isDivisibleBySecondNumber(i, 17):
        if len(wordArr) > 0:
            wordArr.reverse()

    if len(wordArr) != 0:
        for newWord in wordArr:
            word += newWord

    if word != "":
        print(word)
    else:
        print(i)