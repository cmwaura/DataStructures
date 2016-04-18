### Introduction
** Now for the fun part of programming. Drawing stuff.**
We will use the turtle module to complete these exercises.
To begin with, we will draw a recursive spiral. we will create a turtle and then we will define the drawspiral
function.
##### Base Case:
The len of the line is zero or less.
##### recursion step
if len > 0 then the turtle will move forward by len units and turn 90 degrees right.  Then we will draw the spiral again
with a reduced length(recursion step)

This script will be found on visRec.py

lets do something even more cooler.

Assume that we want to make a tree based on the recursion principle. Then the code would probably look something like
this::
        def tree(branchLen, t):
            if branchLen > 5:
                t.forward(branchLen)
                t.right(20)
                tree(branchLen -15, t)
                t.left(40)
                tree(branchLen - 10, t)
                t.right(20)
                t.backward(branchLen)

Lets talk about this script a little bit. What this script says is:

##### Base Case:
len < = 5
##### Recursion step:

if the length of the branch is greater than 5 then we will move the turtle forward the length of the branch and then
turn it right 20 degrees.Once we have done that we will subtract 15 from the branchLen and then call the function again
but this time we need to move the turtle left 20 degrees but since we were 20 degrees right, we subtract 40 to move it
left.

Run the complete code on treeturt.py