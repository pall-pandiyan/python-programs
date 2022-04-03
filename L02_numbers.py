# python have 3 types of numbers
# int - full numbers
# float - numbers with floating point value
# complex - imaginery numbers

x = 5
y = 10
print( "x+y =", x + y )
print( "x-y =", x - y )
print( "x*y =", x * y )
print( "x/y =", x / y )
print( "x//y =", x // y )

# to convert one datatype to another datatype
# we can use int(), float(), complex(), str()
# functions to convert them.
print("int of 3.14 is:", int(3.14))
print("float of 54 is:", float(54))


'''
Arithmetic operators are used with numeric values to perform common mathematical operations:

Operator 	Name 	        Example
    + 	    Addition 	    x + y
    - 	    Subtraction 	x - y 	
    * 	    Multiplication 	x * y
    / 	    Division 	    x / y 	
    % 	    Modulus 	    x % y 	
    ** 	    Exponentiation 	x ** y 	
    // 	    Floor division 	x // y
'''

'''
Assignment operators are used to assign values to variables:

Operator 	Example 	Same As
    = 	    x = 5 	    x = 5 	
    += 	    x += 3 	    x = x + 3 	
    -= 	    x -= 3 	    x = x - 3 	
    *= 	    x *= 3 	    x = x * 3 	
    /= 	    x /= 3 	    x = x / 3 	
    %= 	    x %= 3 	    x = x % 3 	
    //= 	x //= 3 	x = x // 3 	
    **= 	x **= 3 	x = x ** 3 	
    &= 	    x &= 3 	    x = x & 3 	
    |= 	    x |= 3 	    x = x | 3 	
    ^= 	    x ^= 3 	    x = x ^ 3 	
    >>= 	x >>= 3 	x = x >> 3 	
    <<= 	x <<= 3 	x = x << 3
'''

'''
Comparison operators are used to compare two values:

Operator 	Name 	                    Example
    == 	    Equal 	                    x == y
    != 	    Not equal 	                x != y
    > 	    Greater than 	            x > y
    < 	    Less than 	                x < y
    >= 	    Greater than or equal to 	x >= y
    <= 	    Less than or equal to 	    x <= y
'''

'''
Logical operators are used to combine conditional statements:

Operator 	Description 	                Example
    and  	Returns True if both statements are true 	                            x < 5 and  x < 10
    or 	    Returns True if one of the statements is true 	                           x < 5 or x < 4
    not 	Reverse the result, returns False if the result is true 	        not(x < 5 and x < 10)
'''

'''
Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

Operator 	Description 	Example
    is  	Returns True if both variables are the same object 	            x is y
    is not 	Returns True if both variables are not the same object 	        x is not y
'''

'''
Membership operators are used to test if a sequence is presented in an object:

Operator 	Description 	Example
    in  	Returns True if a sequence with the specified value is present in the object 	x in y 	
    not in 	Returns True if a sequence with the specified value is not present in the object 	x not in y 	
'''

'''
Bitwise operators are used to compare (binary) numbers:

Operator 	Name 	Description
    &  	AND 	Sets each bit to 1 if both bits are 1
    | 	OR 	Sets each bit to 1 if one of two bits is 1
    ^ 	XOR 	Sets each bit to 1 if only one of two bits is 1
    ~  	NOT 	Inverts all the bits
    << 	Zero fill left shift 	Shift left by pushing zeros in from the right and let the leftmost bits fall off
    >> 	Signed right shift 	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off
'''

'''
the output will be...
x+y = 15
x-y = -5
x*y = 50
x/y = 0.5
x//y = 0
int of 3.14 is: 3
float of 54 is: 54.0
'''