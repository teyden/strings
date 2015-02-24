import math

def encryptStr():

    """
    encryptStr encodes input string and 
    returns encrypted message 

    Determine rows and columns based on constraints:
        1) floor(sqrt(length)) <= rows <= columns <= ceil(sqrt(length))
        2) rows * columns >= L


    Sample input: "if man was meant to stay on the ground god would have given us roots"
    Sample output: "imtgdvs fearwer mayoogo anouuio ntnnlvt wttddes aohghn sseoau"

    """
    inputStr = raw_input("Input message: ")
    delimiter = " "
    string = inputStr.replace(delimiter, "")
    L = len(string)


    
    # minimum numRow = lowerLimit
    lowerLimit = math.floor(math.sqrt(L))     
    # maximum numCol = upperLimit
    upperLimit = math.ceil(math.sqrt(L))
    
    # range numRow: [lowerLimit, numCol]
    numRow = int(lowerLimit)
    # range numCol: [numRow, upperLimit]
    numCol = int(upperLimit)
    


    for x in range(numRow, numCol+1, 1):
        # starting point of numRow*numCol is smallest possible value
        if (numRow * numCol < L):
            # increment numRow (smaller num) to meet threshold: r*c must be >= L
            numRow = x
            
    if (numRow > numCol):
        print("Error: condition violation")
    

    # Separate sentence sections into appropriate row + col
    # elements = [["ifmanwas"],["meanttos"],...,[] * number of rows]
    elements = []
    for row in range(numRow):
        elements.append([string[0:numCol]])
        string = string[numCol:]


    # Handle case where r*c > L
    trailSpaces = (numRow*numCol)-L
    if (trailSpaces != 0): 
        for i in range(numCol-trailSpaces, numCol, 1):
            # replace trailSpaces in last row with spaces
            elements[numRow-1][0] += delimiter


    # Encode message and store in encrypted
    encrypted = []
    for col in range(numCol):
        word = ""

        for row in range(numRow):
            word += elements[row][0][col]

        encrypted += [word.strip()]


    print(delimiter.join(encrypted))







encryptStr()

        