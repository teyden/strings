from strCounts import *

# strCountsTest.py


def main():
    # __init__, add, reset, report

    
    print ("Testing StringCounts on bad input")
    
    # Initialize object
    sc = StringCounts() 
    
    # Add integer
    try:
        sc.add(100)  
    except TypeError:
        print ("Passed Test 1.1, add: improper type")
    except Exception:
        print ("Failed Test 1.1, add: improper type")
    
    # Add empty string
    # *** There was no indication that an empty string
    # would raise a ValueError, but it doesn't make 
    # sense not to. ***
    try: 
        sc.add("")  
    except ValueError:
        print("Passed Test 1.2, add: empty string")
    except Exception:
        print("Failed Test 1.2, add: empty string")
        
####################################################
    print ("\nTesting StringCounts on good input")
    
    # Initialize object
    sc = StringCounts()
    
    # Add website names
    for k in range(0,10):
        sc.add("www.google.ca")
        for i in range(0, 5):
            sc.add("www.ticketmaster.com")
            
    # Test whether added correctly   
    if sc.strDict["www.google.ca"] == 10:
        print ("Passed Test 2, add: correct addition")
    
    if sc.strDict["www.ticketmaster.com"] == 5:
        print ("Passed Test 3, add: correct addition")
    
    # Clears strings and counts  
    sc.reset()
    
    # Test whether reset worked
    if sc.strDict == {}:
        print ("Passed Test 4, reset: strings and counts cleared")
        
    # Test report
    if sc.report() == None:
        print ("Passed Test 5, report: all cleared; no output")
        
        
    for i in range(0, 5):
        sc.add("www.ticketmaster.com") 
    
    # Readd site
    if sc.strDict["www.ticketmaster.com"] == 5:
        print ("Passed Test 5, add: re-add site")
    
    print("\n\n")

    print("If these two print statements are identical\r\n" + \
    "then enter 1 for True and 0 for False:\n*************")    
    sc.report()
    print("%-50s   %4d" %("www.ticketmaster.com", 5))
    print("*************\n")
    
    print("*Please enter 1 or 0*")    
    if raw_input("Answer: ") == '1':
        print("\nPassed Test 6, report: correct print statement\r\n" + \
        "\nCongratulations, you've made it to the end of" + \
        " the testing module! Until next time, Mr./Ms. Marker!" + \
        " Have yourself a good day :)\n")
    else: 
        print("\nFailed Test 7, report: incorrect print statement\r\n" + \
        "\nOh no! My program failed the last test. Must debug.")

        

if __name__ == "__main__":
    main()