### Problem 5 - AutoComplete with Tries

To insert a node we call the insert method on the TrieNode class, which is a wrapper for the insert method
on the Trie class. 
This Trie method contains a for loop which breaks the input down into each character and performs a logic step
on each element. The time complexity for this method is O(n) as we are just performing one action on each element in input. 
The space complexity is O(1) as no new data structures are created and we're simply iterating over the input.

To find a node with a starting character we use the find method on the Trie class. 
This method is of time complexity O(n). This is ude to there just being one for loop which iterates over our
input, with no further nested loops.
The space complexity is O(1) as no other data structures are created. 

The suffixes method instantiates a list and then calls the `_suffixes` method. 
This `_suffixes` method is a recursive function which will iterate over every child of the 
starting node in the trie. We are not only performing an action on each child, but we are invoking
a for loop on each child element. As a result the worst case time complexity is O(n^2)

The space complexity is dependent on the size of input as we create new nodes for each additional character.

### Complexity
Time: O(n^2)
Space: O(n)