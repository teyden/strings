from WebFilter import *

# strCommands.py 
# University of Waterloo
# CS 234 A3: 2a,2b
# Thuy Tien (Teyden) Nguyen 
# ID: 20337534


# getValue(str, str) --> str
def getValue(anHTTPmsg, paramName):
   """ 
   Preconditions: anHTTPmsg and paramName
   are strings
   
   Assumptions: anHTTPmsg is an HTTP command
   message containing the GET function with
   associated paramater names ("Host:", 
   "User-Agent:", ...)
   
   Postconditions: returns the associated
   parameter value if paramName is a parameter
   in anHTTPmsg and raises a ValueError otherwise
   """
   # Raise TypeError
   if type(anHTTPmsg) != type(""):
      raise TypeError, "in getValue, expecting a string, got " + \
            str(anHTTPmsg)
   if type(paramName) != type(""):
      raise TypeError, "in getValue, expecting a string, got " + \
            str(paramName)
   
   # Raise ValueError if input is empty string
   if (anHTTPmsg == "") or (paramName == ""):
      raise ValueError, "getValue, expecting non-empty string"
   
   # Raise ValueError if parameter length less than msg 
   if len(anHTTPmsg) < len(paramName):
      raise ValueError, "getValue, invalid input"
   
   try: 
      # Always ignore the first line, because in a real HTTP command
      # the first line contains the function name GET
      aMsg = anHTTPmsg.splitlines()
      aMsg = aMsg[1:]
      for aline in aMsg:
         rowWords = aline.split()
         if (rowWords[0] == paramName) and (len(rowWords)==1):
             return ""
#             raise ValueError, "keyword for %s not found" %(paramName)
         elif (rowWords[0] == paramName) and (len(rowWords)>1):
             s = rowWords[1]
             for word in rowWords[1:]:
                 if s == word:
                     pass
                 else:
                     s = s + " " + word
             return s
      # Raises ValueError
      raise ValueError, "cannot find '%s' in HTTP message" %(paramName)
   except Exception:
      raise ValueError, "cannot find '%s' in HTTP message" %(paramName)

   
   
# hasParam --> bool
def hasParam(anHTTPmsg, paramName):
   """
   Preconditions: anHTTPmsg and paramName
   are strings
   
   Assumptions: anHTTPmsg is an HTTP command
   message
   
   Postconditions: returns boolean, True if 
   paramName is a parameter in the HTTP 
   command message and false otherwise. 
   """
   # Raise TypeError
   if type(anHTTPmsg) != type(""):
      raise TypeError, "in anHTTPmsg, expecting a string, got " + \
            str(anHTTPmsg)
   if type(paramName) != type(""):
      raise TypeError, "in paramName, expecting a string, got " + \
            str(paramName)

   # Raise ValueError if input is empty string
   if (anHTTPmsg == "") or (paramName == ""):
      raise ValueError, "hasParam, expecting non-empty string"
   
   # Raise ValueError if parameter length less than msg 
   if len(anHTTPmsg) < len(paramName):
      raise ValueError, "hasParam, invalid input"
   
   # Assumption that all inputs for anHTTPmsg will be actual
   # HTTP commands, then we can omit the first line of the msg
   # containing the function name, GET.
   aMsg = anHTTPmsg.splitlines()[1:]
   for aline in aMsg:
      rowWords = aline.split()
      if rowWords[0] == paramName:
         return True
   return False
