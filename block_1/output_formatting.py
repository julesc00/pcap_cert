"""
Formatting output using String modulo operator(%) :
The % operator can also be used for string formatting. It interprets the left argument much like a printf()-style
format as in C language string to be applied to the right argument. In Python, there is no printf() function but the
functionality of the ancient printf is contained in Python. To this purpose, the modulo operator % is overloaded
by the string class to perform string formatting. Therefore, it is often called a string modulo (or sometimes even
called modulus) operator.

The string modulo operator ( % ) is still available in Python(3.x) and the user is using it widely. But nowadays
the old style of formatting is removed from the language.
"""

# Print integer and float value
print("Geeks : %2d, Portal : %5.2f" % (1, 05.333))  # Geeks : 10, Portal :  5.33

# Print integer value
print("Total students : %3d, Boys %2d" % (240, 120))  # Total students : 240, Boys 120

# Print exponential value
print("%10.3E" % 359.08977)  # 3.591E+02


