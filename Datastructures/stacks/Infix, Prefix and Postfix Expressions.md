## Infix, Prefix and Postfix Expressions

lets take a look at operators. For instance when we have and addition and multiplication
(+, *) we know which one take precedence of the other in an example like A+B*C

However, if we werent taught the BODMAS or PEDMAS rule, how would we be able to distiguish them?
This brings about an issue of **precedence** and the fact that each operator is assigned a
precedence level. Operators of higher are used before lower precedence ops.

Lets interpret the expression of A+B*C using the operator precedence. B and C are multiplied firs and
then A is added to that result. However we know that if the addition would be


    A + B + C = (A + B) + C = A + (B + C) = A + B + C

This may be obvious to us but computers need to know which way the operators work. One way is to write
an expression that  that will guarantee no confusion with respect to the order of operations called a
**fully parenthesized operation**

these changes creates two new expression formats **prefix** and **postfix**. Prefix requires that all operators
precede the operands that they work on. the Postfix is the vice versa.

hence as per the table

Infix Expression 	Prefix Expression 	Postfix Expression
A + B 	                + A B 	              A B +
A + B * C 	            + A * B C 	          A B C * +

now consider the second example (A+B)*C. the prefix expression for (A+B) automatically becomes +AB since the
addition of A + B is done first. However, we are multiplying the addition of A and B therefore we
end up with *+ ABC.

In the same example, the postfix would be AB+ since A and B are added first. Then once we perform the multiplication
we end up with AB+C*. Hence everything is shifted right as per the operator.
lets work on some additional examples:

Infix Expression 	Prefix Expression 	Postfix Expression
A + B * C + D 	       ++ A * B C D           ABC*+D+
(A + B) * (C + D)     *+ A B + C D            A B + C D +*
A * B + C * D           +*A  B * C D          A B * C D*+
A + B + C + D           +++A B C D            AB + C + D


+