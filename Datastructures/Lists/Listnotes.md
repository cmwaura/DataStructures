A list is a collection of items where each item holds a relative position with respect
to each other. More, specifically it is an unordered list. For Example [54, 26, 93, 11]

### The unordered list Abstract Data Type
- List(): creates a new list that is empty. returns an empty list.
- add(item): adds a new item to the list. It needs an item and returns nothing.
    Assume the item is not already on the list.
- remove(item) removes the item from the list. it needs the item and modifies the lost.
    Assume the item is present in the list.
- Search(item): searches for an item in the list. Takes in the param item and returns a
    boolean value.
- size(): returns the number of items in the list
- append(item): adds a new item to the end of the list making it the last item in the collection.
    it needs an item and returns nothing. Assume the item is not already in the list
- index(item): returns the position of the item in the list. it needs the item and returns the index
    Assume the item is in the list.
- insert(pos, item): adds a new item to the list at position pos. it nees the item and returns
    nothing. Assume the item is not already in the list and there are some items in the list to
    make pos valuable
- pop(): removes and returns the last item in the list. it needs nothing and returns the item. Assume
    the list has at least one item.
- pop(pos): pop + positional marker

### Implementing an unordered List: Linked Lists.

inorder to implement an unordered list we will create a **linked list**. I will try to explain this in the
best possible way without using a diagram. Imagine we have an array of items on a table spread out haphazardly.
For instance we have a coffee cup, napkins, spoons. Assume that there is a hierachy as to how each item is used.
In our example we use a spoon and grab the sugar. After, we grab the coffee cup and sip then wipe our mouth
with a napkin, why 'cause we fancy like that. This whole process can be summarized as

    spoon |-------> Coffee cup |--------> napkin

In a similar fashion, linked lists operate the same way. We have an object and a pointer. This pointer points to the
next item and there is a head and an end as to how the hierachy is executed.

Can we take away the coffee cup? Certainly, we would have two items in the list but the spoon pointer will now point to
the napkin.

### The Node Class

The basic building block of a linked list implementation is the node. Each node must hold two pieces of information.
    1) The list item (data field)
    2) Reference to the next node( pointer)

How about we do this in a practical way: check out "linkedlists.py"

### Lets talk about size, search and remove.

The process of doing this entails more than adding to the linked list. It is a process known as
**linked list traversal** and refers to the process of systematically visiting each node. To do this we use an
external reference that will start at the first node then as we move systematically to each next node, we move
the reference to the next node thereby  traversing the next ref.

Traversal definition: to pass or move over, along, or through(dictionary.com)

#### Lets implement a size.

for size implementation method we will traverse the list and keep a count of the number of nodes that appear.
Knowing this, you probably have figured out that we will have a variable count which will start at 0 and as we move
we will add one. Finally count gets returned when the iteration stops.

#### Lets implement a search method.

For searching it will use a similar method to size. However, it will compare the text to the item provided and if
they are the same, it will return that found= True. Else, it will move on to the next element.

#### Lets remove a node.


