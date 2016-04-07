Stacks
------
an ordered collection where the addition of new items and the removal of existing
items always takes place at the same end. This end is referred to as the top. This is
the LIFO:
Story time:
imagine you are working in a grocery store but instead of using a "First in First out" method
implementation, the last thing that you stack on the grocery shelf will be the first thing that
the customer will buy. Think of the conclusions that might come due to this, for instance,
if we keep on adding things to the shelf at the same rate that the customer is taking things out
then this implies that some of the items towards the back will never be bought by the customer.
 Now assume we have a specific gluten free product that the customer needs to buy but this product
 is all the way to the back of the shelf. Then this customer will have to pull out everthing out
 systematically to get to the item.

 This action of pulling this out will be a reversal process.

 assume we have: 1, 2, 3, 4, 5 ,6 ,..., n-1, n, items in n respective positions
 then to get to position 3 the customer will have to go through n, n-1, n-2, n-3,
 ..., 6, 5, 4, 3

 This is a reversal order of the first ordering.

 Stack Abstract Data Type
 a stack is a structured and ordered collectin of items where items are added and removed from the
 top. Stacks are ordered LIFO and the operations are
 - Stack() creates a new stack that is empty. It needs no parameters and returns and empty stack
   This is similar to creating an empty shelf row. It has no items but its a container that can
   hold items.
 - push(item) adds an item to the top of a stack. Similar to the worker adding a product. It needs the
    item and returns nothing
 - pop() removes the top item from the stack. Similar to the customer picking the first item from the
    shelf which is the last item the worker placed
 - peek() returns the top item from the stack but does not remove it. Similar to the worker checking
    catalog to see what the last item he racked but not really removing it or even touching it.
 - isEmpty() check to see whether the stack is empty. Returns a boolean value and has no param
 - size() returns the number if items in the stack.

Stack Operation 	Stack Contents 	    Return Value
s.isEmpty() 	        []          	    True
s.push(4) 	            [4]
s.push('dog') 	        [4,'dog']
s.peek() 	            [4,'dog'] 	        'dog'
s.push(True) 	        [4,'dog',True]
s.size() 	            [4,'dog',True] 	    3
s.isEmpty() 	        [4,'dog',True] 	    False
s.push(8.4) 	        [4,'dog',True,8.4]
s.pop() 	            [4,'dog',True] 	    8.4
s.pop() 	            [4,'dog'] 	        True
s.size() 	            [4,'dog'] 	        2

lets implement a stack in Python:
