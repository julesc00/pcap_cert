"""
OPERATOR DESCRIPTION SYNTAX
    &	Bitwise AND	x & y
    |	Bitwise OR	x | y
    ~	Bitwise NOT	~x
    ^	Bitwise XOR	x ^ y
    >>	Bitwise right shift	x>>
    <<	Bitwise left shift	x<<

    In Python, bitwise operators are used to performing bitwise calculations on integers. The integers are first
    converted into binary and then operations are performed on bit by bit, hence the name bitwise operators.
    Then the result is returned in decimal format.

    Note: Python bitwise operators work only on integers.
"""

a, b = 10, 4
"""
Bitwise Operators

In Python, bitwise operators are used to performing bitwise calculations on integers. The integers are first converted 
into binary and then operations are performed on bit by bit, hence the name bitwise operators. Then the result is 
returned in decimal format.
"""

# Print bitwise AND operation
print("a & b =", a & b)

# Print bitwise OR operation
print("a | b =", a | b)

# Print bitwise NOT operation
print("~a =", ~a)

# Print bitwise XOR operation
print("a ^b =", a ^ b)


"""
Shift Operators 

These operators are used to shift the bits of a number left or right thereby multiplying or dividing the number by 
two respectively. They can be used when we have to multiply or divide a number by two. 
Bitwise right shift: Shifts the bits of the number to the right and fills 0 on voids left( fills 1 in the case of a 
negative number) as a result. Similar effect as of dividing the number with some power of two.
"""
c, d = 10, -10

# Print bitwise right shift operator
print("a >> 1 =", c >> 1)  # 0000 0101 = 5
print("b >> 1 =", d >> 1)  # 1111 1011 = -5

# print bitwise left shift operator
print("c << 1 =", c << 1)  # 20
print("d << 1 =", d << 2)  # -40


"""
Bitwise Operator Overloading

Operator Overloading means giving extended meaning beyond their predefined operational meaning. For example 
operator + is used to add two integers as well as join two strings and merge two lists. It is achievable 
because the ‘+’ operator is overloaded by int class and str class. You might have noticed that the same built-in 
operator or function shows different behavior for objects of different classes, this is called Operator Overloading.
"""


class Geek:
    def __init__(self, value):
        self.value = value

    def __and__(self, obj):
        print("And operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __or__(self, obj):
        print("Or operator overloaded")
        if isinstance(obj, Geek):
            return self.value | obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __xor__(self, obj):
        print("Xor operator overloaded")
        if isinstance(obj, Geek):
            return self.value ^ obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __lshift__(self, obj):
        print("lshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value << obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __rshift__(self, obj):
        print("rshift operator overloaded")
        if isinstance(obj, Geek):
            return self.value & obj.value
        else:
            raise ValueError("Must be a object of class Geek")

    def __invert__(self):
        print("Invert operator overloaded")
        return ~self.value


# Driver's code
if __name__ == "__main__":
    a = Geek(10)
    b = Geek(12)
    print(a & b)
    print(a | b)
    print(a ^ b)
    print(a << b)
    print(a >> b)
    print(~a)
