In Staircase, the time complexity is O(n^2) due to the nested for loops, both of which have length very similar to n
The space complexity is O(n) because the size of the "line" string scales with the input size directly at its largest.

In the psuedocode for find the path, there are two recursive calls for each edge. This means it will run in O(|E|), or in linnear time scaling with the number of edges.