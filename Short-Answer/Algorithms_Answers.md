#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `O(n)` - There's one while loop and it's multiplying `n` a few times, but time complexity is always going to rely on size of `n`. Therefore I'm reading it as O(n).


b) `O(n^2)` - There first `forLoop` depends on the size of `n` which would be `O(n)`. All operations inside loops are `O(1)`. The second `forLoop` is dependent on `n` as well. The nested loops would be dominant over the `O(1)` operations inside the loops.


c) `O(n)` - The time depends on the number of `bunnies (n)` being passed in. Then it's essentially looping by recursion `n` times until it reaches its base case.

## Exercise II

I would use a binary search which has a runtime complexity of `O(log n)`.
Start at the middle of n floors and drop an egg. if the egg breaks we throw away the upper half and focus on the lower half
We can use recursion and repeat the above step to keep halving until we find the floor `f`


