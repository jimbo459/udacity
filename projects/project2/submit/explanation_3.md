### Problem 3 - Rearrange Array Elements

This solution uses Quick Sort (O(n log n)) to sort the list into ascending order. 
We then range over the sorted list taking the highest value each time and adding 
to two strings. These strings are then returned as ints within a list. 
Sorting takes O(n log n) time, the building of the two ints to return takes O(n) time. 
However, O(n log n) is larger so the time complexity of this solution is O(n log n)
The space complexity is O(1) as we have a fixed number of data structures irrespective of n.

#### Complexity
Time: O(n log n)
Space: O(1)
