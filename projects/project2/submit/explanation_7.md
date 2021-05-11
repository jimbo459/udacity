### Problem 7 - Request Rooting

For this problem the outer router class is a simple wrapper for the RouterTrie class where I placed
most of the logic and steps. 
Within the RouterTrie class we call three methods, `insert, find, _prepare_path`. 
Both the insert & find methods call `_prepare_path`. This method uses pythons '.strip' O(1) and '.split' O(n) complexity. 
Insert and find break up the input into an array and then perform an action for each item in that array. 
Given that there is no nested for loop, and we're only performing a check on each item of the input the time complexity
should be O(n)
The space complexity is O(n) as we will create new nodes for each value in the path. Each node contains a dict. 

#### Complexity

Time: O(n)
Space: O(n)
