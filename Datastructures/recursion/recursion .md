### Recursion

Recursion is a methid of solving problems that involves breaking a problem down into smaller and smaller
subproblems until you get small enough to be solved trivially. It usually involves calling a function itself

#### Calculating the sum of a list of numbers
Suppose that you want to calulate the sum of a list of numbers such as [1,3,5,7,9], you could write an iterative
function that computes the sum as shown below.

        def listsum(numList):
            theSum = 0
            for i in numList:
                theSum = theSum + i
            return theSum
        print listsum([1,3,5,7,9])

this will definitely work and while the loop takes care of the list, assume we lived in a world where we did not
have loops(for and while) and all we had was sheer will power of solving problems, how would we attempt to solve
this problem? Well inorder to be able to solve this, we have to figure out what the problem entails us to do

Mathematically:
    1+3+5+7+9 = 25
    well this can be written as
    (1+3+5+7+9) = ((((1+3)+7)+9) = (1+(3+(5+(7+9))))
    starting with the inner most digits we have that
    (1+(3+(5+(7+9)))) = (1+(3+(5+16))) = (1+(3+21)) = (1+24) = 25

similarly we can do the same by using python to recursively solve the list for us. We would need a base case which in
our case would be the first number and then recursively go through the other four numbers. so in short we would have an
eqn similar to

    listSum(numList) = first(numList) + listSum(rest(numList))

how about we write some code for this:

    def listsum(numList):

        if len(numList) ==1 :
            return numList[0]
        else:
            return numList[0] + listsum(numList[1:])
    print listsum([1,3,5,7,9])

#### Things to note in this eqn.

1) we are checking to see that the problem has more than one element in the first position. This is because the sum of
    a list one element long is trivial and is just the number on the list.
2) The function calls itself on the else clause. This is where recursion occurs.


### Three Laws of Recursion

1) A recursive algorithm must have a base case
2) A recursive algorithm must change its state and move toward the base case
3) a recursive algo must call itself, recursively

** side note yet to be verified: it seems that recursion is more or less like a form of induction process where you
start with the trivial aspect, then you assume that n is true and solve for n+1 but in this case we are solving
backwards to the basecase.**

A base case is a condition that will allow recursion to halt. its trivial and we can solve the base case directly. For
instance in our problem, the base case was 1

In the second law, we must change the state and move towards the base case. To change the state, it means that the
algorithm is modified and the data is getting smaller in some way.

The final law is that the algorithm must call itself.

### Converting an Integer to a String in any Base
assume that we are trying to convert an integer like 769 to a string. We would need an algorithm that involves three
components:
1) Reduce the original number to a series of single-digit numbers.
2) convert the single digit-number to a string using lookup.
3) concatenate the single digit strings together to form the final result.

we will be using division to convert the strings. Assume that we have the number 769 and we divide by base 10, then we
will have 76 with a remainder of 9. Hence the remainder can be converted to a string via a lookup.
We will then divide the integer again by 10 and get 7 and 6 respectfully.  at this point we have reached the part where
the actual number n< base where the base = 10.

This will be done in the "intostring.py"

### Stack Frames: Implementing Recursion.
Suppose instead of concatenating the result of the recursion we modified the algo to push the strings onto a stack prior
to making the recursive call.