### Problem 1 - LRU Cache

This problem was solved using a hashmap and a doubly-linked list. 
Given that the time complexity had to be O(1), this meant that we needed to be able to look up values
without traversing through a list to find a node. 

The doubly-linked list allowed us to easily keep an order of recently used items, 
but by using the hash-map to keep track of the individual nodes stops us having to traverse 
the doubly linked list, and remove nodes in constant time. 

Time efficiency is constant O(1) as items stored in cache are directly referenced, with no need to search.
Space efficiency is also constant O(1) this is due to there being no loops or recursive functions being called.
Instead the space is restricted to a Doubly linked list of 5 nodes and a dict with 5 entries. 
