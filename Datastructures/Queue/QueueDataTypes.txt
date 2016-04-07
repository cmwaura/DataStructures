## Queue Data Types

A queue is structured as an ordered collection of items which are added at one end
and retrieved at the other end.(rear and front resp.)

Queue operatiosn are given as:

Queue(): Creates a new queue that is empty. It needs no parameters and returns an
          empty queue.

enqueue(item): adds a new item to the rear of the queue. It needs the item and returns
                nothing

Dequeue(): removes the front item from the queue. t needs no parameters and returns an
          an item. The queue is modified.

isEmpty(): tests to see whether the queue is empty.  It needs no parameters and returns an
          a boolean value
size(): # of items in the queue. Returns an int.

Queue Operation 	Queue Contents  	Return Value
q.isEmpty() 	          [] 	            True
q.enqueue(4) 	          [4]
q.enqueue('dog') 	    ['dog',4]
q.enqueue(True) 	[True,'dog',4]
q.size() 	        [True,'dog',4] 	         3
q.isEmpty() 	    [True,'dog',4] 	        False
q.enqueue(8.4) 	    [8.4,True,'dog',4]
q.dequeue() 	    [8.4,True,'dog'] 	     4
q.dequeue() 	    [8.4,True] 	            'dog'
q.size() 	        [8.4,True]          	  2


Lets implement a queue. We need rto decide which side will be the last and which side will be
the front. This allows the use of insert to ad new elements to the rear of the queue and pop to
remove the front element. Hence enqueue will be O(n) and dequeue will be O(1). "queueimplementation.py"