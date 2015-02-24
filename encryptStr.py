import math
# floor, ceil, sqrt

def encryptStr(inputStr):

    """
    encrypts input string
    """

    # remove white spaces
    string = inputStr.replace(" ", "")
    # take string length
    L = len(string)

    
    # minimum numRow = lowerLimit
    lowerLimit = math.floor(math.sqrt(L))     
    # maximum numCol = upperLimit
    upperLimit = math.ceil(math.sqrt(L))
    
    # range numRow: [lowerLimit, numCol]
    numRow = int(lowerLimit)
    # range numCol: [numRow, upperLimit]
    numCol = int(upperLimit)
    

    # does decrementing numCol produce smaller product?
    for x in range(numRow, numCol+1, 1):
        print("Range between row and col: ")
        print(range(numRow, numCol+1, 1))
        # starting point of numRow*numCol is smallest possible value
        if (numRow * numCol < L):
            # increment numRow (smaller num) to meet threshold: r*c must be >= L
            numRow = x
            
    if (numRow > numCol):
        print("Error: condition violation")
    else:
        print("Number of rows, columns: %d %d " % (numRow, numCol))
        
    # elements = [["ifmanwas"],["meanttos"],...,[] * number of rows]
    elements = []

    for row in range(numRow):
        elements.append([string[0:numCol]])
        string = string[numCol:]


    if (numRow * numCol < L): 
        raise ValueError, "Product must be greater than string length"


    encrypted = ""
    for col in range(numCol):
        print(col)
        word = ""
        for row in range(numRow):
            # print("Row: %d " % row)
            # print("Letter #: %d " % k)

            else:
                word += elements[row][0][col]
                k += 1

        encrypted += word + " "


    print(encrypted)




encryptStr("if man was meant to stay on the ground god would have given us roots")

        