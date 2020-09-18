#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This is an O(n) case since we have an operation that depends on the input. This is considered linear due each time n changes, a then will change because it is incremented by n^2.


b) The first operation just states that we are setting the sum equal to 0 so that is constant. Once we move along there is a for loop which sets j = 1 n number of times, making that O(n).  The next includes a while loop that restarts j at a multiple of 2 each time.  This is similary to binary search which is O(logn).  However, these two exist together we would need to use the product of O(n) and O(log n) to get a resulting O(nlogn)

c) Recursive function is going to be O(n) due the input size having a linear impact on the runtime.  If bunnies is small it will be quicker than if it is large and then has to repeat the run bunnies-1 one each time until there are no bunnies left :) 

## Exercise II


We are in a building that goes from the 0th floor to the nth floor.  Somewhere inside of that range we have a floor, f where if we drop an egg it won't break. From that floor below it is a no break eggs zone. 

Because we have a range, and a target within that range, we could go with a binary search and start with a midpoint.  We could determine at that midpoint if the egg breaks.  If at the midpoint floor the egg breaks is True we would then set our position to the next floor below and check if the eggs breaks and so on as to reduce the number of eggs broken.  Our other case would be that at that midpoint the egg does not break and now we would go up a floor until the egg actually breaks and our ideal floor would be the -1 of the first breaking floor.

Because we are using a binary search, the runtime will be O(logn) since we are essentially cutting the number of floors we need to check in half. 