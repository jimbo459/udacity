### Active Directory

I felt the cleanest solution was to make use of recursion. Given that we already have 
the list data structures defined in the group, we can simply make use of that data structure
to determine if a user is part of a group of sub-groups. 

The time complexity of this solution is O(n^2), this is due to there being a for loop within the 
`is_user_in_group` function, which will be called on each item in group. The `if user in group` line will be of time 
complexity O(n), given that each item in the input will be compared. 
I felt this was a clean solution as even if we stored the information in a new data structure we would still have the cost of looking at every group / user.
This solution also returns true as soon as the user is found, rather than having to inspect all users/groups first. 

The space complexity is O(1) given that no new data structures are created in the function, it is only 
the pre-existing lists which are being inspected. 