### Problem 2 - Search rotated sorted array

Given that the problem needed to be solved in O(log n) time, binary search would be a good 
implementation. However, binary search only works on a sorted list, so we needed to find the 
pivot point at which the list had been rotated. 
The searching for the pivot is also O(log n) time as it uses a similar pattern to binary search
to determine if the pivot is the lowest number in the array. 
Given that both functions called by rotated_array_search are O(log n) we have managed to satisfy
the requirement of the assignment. 
The space complexity is O(1) as no additional data structures or space is required for the solution.

#### Complexity
Time: O(log n)
Space: O(1)