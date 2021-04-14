### Problem 2 - File Recursion

This problem was solved using a python list a for loop and a recursive function call. 

Using a simply python list makes it easy to both extend or append the returned items. 
This was important as find files may return multiple items, so to add this to the top level list the extend method is required. 
Otherwise you would have a list of sub-lists. 

The Time complexity for this solution is O(n^2). This is due to there being a for loop within the function, which will run on each item,
but each item could also have the find_files function called on it. 

The Space complexity is O(n) given that each directory will invoke find_files which creates an additional python list. 
