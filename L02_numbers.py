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