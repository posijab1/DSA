What is a linked list?

A linked list is a sequential list of node that hold data 
which point to others node also containing data.

Where are linked list used?

Used in many List, Queue & Stacks implementations.
- Great for creating circular lists.
- Can easily model real world objects such as trains.
- Used in separate chaining, which is present certain Hashtable
implementations to deal with hashing collisions.
- Often used in the implementation of adjacency lists for graphs.

Terminology:

Head: The first node in a linked list.
Tail: The last node in a linked list.
Pointer: Reference to another node.
Node: An object containing data and pointer(s).

Complexity:

Search: O(n)
Insert at head: O(1)
Insert at tail: O(1)