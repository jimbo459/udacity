### Problem 3 - Huffman Tree

#### Huffman_encoding
This problem required multiple elements to be implemented. 

The first function we invoke `huffman_encoding` has one for loop, but it also invokes the following methods:

`huffman_tree.build_from_queue()` will take in a priority queue and reduce the queue down to one element, which is then returned as the root node of the Huffman Tree.
The priority queue is implemented as a MinHeap, with an underlying list. 
This function pops elements off the priority queue which is O(1) given the first element is returned. However this function also appends to the MinHeap. When inserting into the MinHeap we sort the Heap every time. This makes use of the list.sort() method, which is O(n logn).

`huffman_tree.encode()` this function calls another recursive method `_encode()`. This function has to traverse the entire Huffman Tree. Therefore the time complexity is O(h) where h is the height of the tree.
This method also has an additional for loop to return the actual encoded data. 
As a result we have two distinct actions occuring, the traversing of the tree to assign encoded values and then iterating over the input data to encode it using those values.
Both of these are dependent on the original input data, and there is not a nested for-loop ocurring so I would state that the time complexity for this is O(n)

Taking this into account I believe the overall time complexity for `huffman_encoding` to be O(n logn), with the biggest cost being the current implementation of the MinHeap, and having to sort it each time an element is added. 
Space complexity will be O(n) as the size of the tree will require more nodes depending on the size of the input. Other components used such as MinHeap will just make use of one list O(1).

#### Huffman_decoding
This function is far simpler, and just has a single for loop which runs for each `bit` in the input data. 
This has time complexity of O(n)
Space complexity is also fixed as O(1) as it will always simply return a string.

### `huffman_encoding` Result
Time: O(n logn)
Space: O(n)

### `huffman_decoding` Result
Time: O(n)
Space: O(1)




