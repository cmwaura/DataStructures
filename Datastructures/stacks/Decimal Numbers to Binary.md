### Convertng Decimal Numbers to Binary Numbers

The decimal number 233base10 and its corresponding binary equivalent 11101001s
interpreted as:
2 x 10^2 + 3 x 10^1 + 3 x 10^0

and
1x2^7+1x2^6+1x2^5+0x2^41x2^3+0x2^2+0x2^1+1X2^0

we can convert integer to binary by the algorith called "divide by 2" that uses a stack
to keep track of the digits for the binary result.
This algorithm is dividing a number by two while keeping track of its remainder. It is
a simple iteration that checks the number as to whether it is even or odd with even having
a remainder of 0 and odd having a remainder of 1. We will then note the remainder numbers
from top to bottom being the inverse for instance

233//2=116 rem =1
116//2 = 58 rem=0
58//2 = 29 rem =0
29//2 = 14 rem = 1
14//2 = 7 rem =0
7//2 = 3 rem = 1
3//2 = 1 rem = 1
1//2 = 0 rem = 1

Binary = 11101001

The python function will take in an argument as a dec number and repetedly divive it by two
using the modulo operator to extract the remainder and then push it back on the stack for
another division. This can be found in the "DecimalBinary.py"

## A General Case

Now that we can convert from decimal to binary what about those other numbers namely: Hexadecimal,
and octal Well we will need a way to covert decimal to those types. Before moving forward, lets find
out what these types actually are. For the number we used above 233, the Octal and Hexadecimal are
351(base8) and E9(base16)
this done numerically is
3 X 8^2 + 5 X 8^1 +1 X 8^0
and
14 X 16^1 + 9 X 16^0 respectively.

Taking the function we wrote above, we can modify it to include a base converter that would take in
any base and convert the number per that base. The problem arises when we get above the number 10.
Since they are double digit, we need a way to represent them hence we substitute them with Letter A-F
This implementation can be found on the file DecimalBase.py