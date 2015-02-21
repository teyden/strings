from types import IntType, StringType
# strCounts.py


class StringCounts:
    
    # Keeps track of how many times a particular string has been "seen."
    
    def __init__(self):
        # strings stored in dictionary; key = aString, 
        # value = number of times it has been seen
        self.strDict = {}
    
    def add(self, aString):
        """
        Precondition: aString is a string 
        
        Assumptions:
        
        Postcondition: add the string if this is the first time it is
        being seen. If it has been seen before, incremenet the count
        by one. 
        """   
        if type(aString) != StringType: 
            raise TypeError, "input type must be a string"
        
        if aString == "":
            raise ValueError, "input must be non-empty string"
        
        if aString not in self.strDict:
            self.strDict[aString] = 1
        else: 
            self.strDict[aString] += 1
        
            
    def report(self):
        """
        Postcondition: print a string representation of all the 
        strings that have been added and their counts with the 
        format '%-50s %4d'
        """     
        if len(self.strDict) == 0:
            pass
        for key in self.strDict:
            print "%-50s   %4d" %(key, self.strDict[key])

            

    def reset(self):
        """
        Postcondition: remove all strings in the object and
        clear counts.
        
        *Note: calling reset() on an empty StringCount object is not
        an error.*
        """
        if len(self.strDict) > 0:
            self.strDict.clear()
            # strDict now empty

            

            
        
        
            
