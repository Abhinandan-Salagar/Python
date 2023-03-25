
##################### Function Declarations ##########################

## Current Date Time
def getTime2() : # Function Creation / Declaration
    import datetime
    currentTimeStamp = datetime.datetime.now()
    currentStamp = currentTimeStamp.strftime("%H : %M")
    return currentStamp

## Factorial
def findFactorial(num) : 
    fact = 1
    for i in range( num , 0, -1 ) : 
        fact = fact * i
    return fact

## Find if a number is even or odd?
def even_odd(n) : 
    if n%2 == 0 : 
        return "Even"
    else : 
        return "Odd"
    
## Palindrome
def palindrome(word) :
    if word[ : :1] == word[ : :-1] :
        return "Palindrome"
    else :
        return  "Not a Palindrome"

##################### Function Calling ##########################

'''
# Get time
print( getTime2() )

# Finding Palindrome
word = str(input("Enter the word to check Palindrome : ")).strip().lower()
print( palindrome(word) )

# Factorial
num = int( input("Write the Number for which Factorial needs to be Found : ") )
print(f"Factorial of {num} = {findFactorial(num)}")

# Even Odd
num = int( input("Write the Number for which Even Odd needs to be Found : ") )
print( num, " is ", even_odd(15) )

'''




