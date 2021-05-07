### Problem 1 - Square root of an integer

Given that the task had to be completed in O(log n) binary search seemed the most 
appropriate method. This results in n halving on each iteration of the while loop. 
The space complexity is constant as no new data structure is created on each iteration.

I chose the round() function to ensure that the returned result was always an int. 

#### Complexity
Time - O(log n)
Space - O(1)