
######## Package ################
"""
- collection of folders and python files
- Identification : __init__.py

"""


########## Ways to Import Package and its Modules ###########

# Way 1
# Dependent on Package everytime
# Syntax : import packageName
# Relevant Function :: packageName.Module()
'''
import math

print( "SquareRoot of Number : ", math.sqrt( 100 ) )
print( "Cos of Number : ", math.cos( 100 ) )
print( "Exponential of Number : ", math.exp( 2 ) )
print( "Log of Number : ", math.log( 11 ) )


print( "SquareRoot of Number : ", math.sqrt( 25 ) )
print( "Exponential of Number : ", math.exp( 3 ) )

'''

# Way 2
# Syntax : from packageName import Module_1, Module_2 , ....
# Dependent to the Modules you have extracted from the package
# 

'''
from math import sqrt, exp

print( "SquareRoot of Number : ", sqrt( 100 ) )
print( "Exponential of Number : ", exp( 2 ) )
print( "SquareRoot of Number : ", sqrt( 25 ) )
print( "Exponential of Number : ", exp( 3 ) )

print( "Cos of Number : ", cos( 100 ) )
print( "Log of Number : ", log( 11 ) )
'''


# Way3
# Syntax: from packageName import *
# Import all the Modules from the package
'''
import math
from math import *

print( "SquareRoot of Number : ", sqrt( 100 ) )
print( "Exponential of Number : ", exp( 2 ) )
print( "SquareRoot of Number : ", sqrt( 25 ) )
print( "Exponential of Number : ", exp( 3 ) )

print( "Cos of Number : ", cos( 100 ) )
print( "Log of Number : ", log( 11 ) )


print( "Cos of Number : ", math.cos( 100 ) )
'''
































