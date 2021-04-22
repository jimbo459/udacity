### Problem 6 - Union & Intersection

#### Union
Given that there was no stipulation on the ordering of the returned list I decided
to introduce a `prepend` method for the linked_list as this is O(1) rather than O(n)
time complexity. 

For the Union function I made use of sets to ensure that duplicates wouldn't exist.
In order to transpose the linked_list into a set we have to iterate over the entire list, 
but this is only O(n) time complexity. 
This is called on both lists given as arguments, and then a further for loop is required to 
convert the set back to a linked_list (within the helper function iter_to_linked_list). There are no nested for loops. 

#### Union complexity
Therefore for the Union solution time complexity is O(n) and space complexity will be O(1)
given that we use the same data structures irrespective of input size. 

#### Intersection

Intersection again does not rely on returning a sorted order, so we can use the prepend
method of the linked_list to save time. 

The Intersection function makes use of lists, and relies on python's inbuilt search functionality
to determine if an item in one list exists in the other. This is O(n) time complexity.
There are no nested for loops, so time complexity remains O(n).
The use of a set ensures that no duplicates are in the return value. 

#### Intersection complexity
The time complexity for the intersection solution is O(n), and the space complexity it O(1)
given that the number of data structures remain constant regardless of input size. 


#### Overall complexity
Based on the above, the overall complexity for the solution is:
Time O(n)
Space O(1)

