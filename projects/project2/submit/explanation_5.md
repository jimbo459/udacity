### Problem 5 - AutoComplete with Tries

The suffixes method instantiates a list and then calls the `_suffixes` method. 
This `_suffixes` method is a recursive function which will iterate over every child of the 
starting node in the trie. We are not only performing an action on each child, but we are invoking
a for loop on each child element. As a result the worst case time complexity is O(n^2)

The space complexity is constant as we only create one list which we append to, rather than 
dynamically creating more lists or data structures based on the input size. 

### Complexity
Time: O(n^2)
Space: O(1)