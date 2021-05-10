### Problem 4 - Dutch National Flag Problem

In this problem we need to ensure we only traverse the list once. 
We use an algorithm similar to quick sort. The front index is replaced by 
whatever is in our next_0 or next_2 index and we set those values to 0 or two respectively. 
This ensures that we move the 0's and 2's to the correct position, leaving the 1's in their right place. 

The time complexity of this solution is O(n) as every element in the list is inspected. 
The solution uses an in-place swap, so no extra space is required resulting in O(1).

#### Complexity
Time: O(n)
Space: O(1)


