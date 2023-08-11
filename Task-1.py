#!/usr/bin/env python3
"""
Module Docstring
"""


def main():
    """ Main entry point of the app """
    
    inp = "Hello"
    print(inp[:2])


    # Problem 2
    inp = "Hello"
    print(inp[-2:]*3)

    # Problem 3
    test_string ="WooHoo"
    string_lenght = len(test_string)//2
    print(test_string[:string_lenght])

    #Problem 4 
    inp = "Hello"
    string_lenght = len(inp)
    print(inp[1:string_lenght-1])

    #Problem 5
    inp ="Hi"
    inp2 = "Bye"
    print(inp+inp2+inp2+inp)  

    #Problem 7
    inp = "Hello"
    inp2 ="There"
    print(inp[1:]+inp2[1:])  

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()