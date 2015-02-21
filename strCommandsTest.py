from strCommands import *
from HTTP_examples import *

msg = 'GET http://www.lib.uwaterloo.ca/hours/ HTTP/1.1\nHost: www.lib.uwaterloo.ca\nUser-Agent: Mozilla/5.0 (Windows NT 5.1; rv:29.0) Gecko/20100101 Firefox/29.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-US,en;q=0.5\nAccept-Encoding: gzip, deflate\nConnection: keep-alive\n\n'

modmsg = """GET http://www.lib.uwaterloo.ca/hours/ HTTP/1.1\nHost:\nCookie-Agent: Mozilla/5.0 (Windows NT 5.1; rv:29.0) Gecko/20100101 Firefox/29.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\nAccept-Language: en-US,en;q=0.5\nACCept-Encoding: gzip, deflate\nConnection: keep-alive\n\n
"""
host = "Host:"
user = "User-Agent:"

def main():
    origHTTPmsg = msg1
    HTTPwithoutHostKey = msg5
    HTTPwithoutHost = msg6

    
     # Test getValue on bad input: TypeErrors      
    print("** Testing on bad input: TypeErrors **")
    
    try:
        getValue(100, host)
    except TypeError:
        print("Passed Test 1, getValue: improper anHTTPmsg type")
    except Exception:
        print("Failed Test 1, getValue: improper anHTTPmsg type")
        
    try:
        getValue(100, 100)
    except TypeError:
        print("Passed Test 2, getValue: improper anHTTPmsg type")
    except Exception:
        print("Failed Test 2, getValue: improper anHTTPmsg type")
        
    try:
        getValue("gibberish", 100)
    except TypeError:
        print("Passed Test 3, getValue: improper paramName type")
    except Exception:
        print("Failed Test 3, getValue: improper paramName type")

        
    # Test hasParam on bad input: TypeErrors
    print("\n\n** Testing hasParam on bad input: TypeErrors **")   
    
    try:
        hasParam(100, host)
    except TypeError:
        print("Passed Test 1, hasParam: improper anHTTPmsg type")
    except Exception:
        print("Failed Test 1, hasParam: improper anHTTPmsg type")
    
    try:
        hasParam(100, 100)
    except TypeError:
        print("Passed Test 2, hasParam: improper anHTTPmsg type")
    except Exception:
        print("Failed Test 2, hasParam: improper anHTTPmsg type")
        
    try:
        hasParam("gibberish", 100)
    except TypeError:
        print("Passed Test 3, hasParam: improper paramName type")
    except Exception:
        print("Failed Test 3, hasParam: improper paramName type")        
        
        
    # Test getValue on bad input: ValueErrors
    print("\n\n** Testing getValue on bad input: ValueErrors **")
    
    ## Empty string
    try:
        getValue(" ", "")
    except ValueError:
        print("Passed Test 1, getValue: input must be non-empty string")
    except Exception:
        print("Failed Test 1, getValue: input must be non-empty string")
    
    ## Empty string
    try:
        getValue("", host)
    except ValueError:
        print("Passed Test 2, getValue: input must be non-empty string")
    except Exception:
        print("Failed Test 2, getValue: input must be non-empty string")
    
    ## Actual HTTP message; host parameter with missing semi-colon
    try:
        getValue(origHTTPmsg, "Host")
    except ValueError:
        print("Passed Test 3, getValue: 'Host' parameter not found")
    except Exception:
        print("Failed Test 3, getValue: 'Host' parameter not found")
   
    ## Modified HTTP message, correct parameter
    try:
        getValue(HTTPwithoutHost, host)
    except ValueError:
        print("Passed Test 4, getValue: '%s' parameter not found") %host 
    except Exception:
        print("Failed Test 4, getValue: '%s' parameter not found") %host 
    
    ## Actual HTTP message; host parameter with colon and space
    try:
        getValue(origHTTPmsg, "Host: ")
    except ValueError:
        print("Passed Test 5, getValue: '%s' parameter not found") %user 
    except Exception:
        print("Failed Test 5, getValue: '%s' parameter not found") %user 
        
        
    # Test on good input    
    print("\n\n** Testing on good input **")
        
    if type(getValue(msg1, host)) == type("") \
       and hasParam(msg1, host) == True:
        print("Passed Test 1: parameter is in"+ \
        " HTTP command")
    
    ## Modified HTTP message, correct parameter
    if getValue(HTTPwithoutHostKey, host) == "" \
        and hasParam(HTTPwithoutHostKey, host) == True:
        print("Passed Test 2: parameter found in" + \
        " message but key value not found")
        
    if type(getValue(msg5, user)) == StringType \
        and hasParam(msg5, user) == True:
        print("Passed Test 3: correct input types and proper output")

 
    
if __name__ == "__main__":
    main()
    
