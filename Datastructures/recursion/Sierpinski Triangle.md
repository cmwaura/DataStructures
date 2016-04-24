##Sierpinski Triangle

Another fractal that exhibits the property of recursion. Simply start with a triangle then divide this triangle into
three triangles by connecting the midpoint of each side. Ignore the middle triangle and apply the same procedure to
each of the three corner triangles.

Each time you create a new set of triangles apply this procedure to the three smaller corner triangles.

#### BASE CASE.
it will be the degree of the fractal or the number of times we want to divide the triangle into pieces.

#### Recursion Step.
Each time we draw then triangle we subtract 1 from the degree until we reach 0. The code will be available on
"sierpinski.py"
