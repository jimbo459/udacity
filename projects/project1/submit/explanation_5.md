### Blockchain

This solution is a very simplistic blockchain implementation using a linked list. 

Given the problem criteria did not state what search / methods should be implemented I went with 
simply being able to add to the Blockchain. 
To ensure the hash is unique I decided to combine the data with a string of the timestamp.

I decided to prepend the new blocks, rather than appending so that we could insert into the list in constant time O(1)

The time complexity of this solution for inserting is O(1). Given that we are inserting at the front
of the list every time, so there is no traversing required. 

The space complexity is also O(1) as the size of the block does not vary, and one block will be created for each add.