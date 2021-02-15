If you want a solution for a sudoku puzzle, it may help you. Give each line of the puzzle as input with zeroes in place of spaces.

If, like me, you're too lazy to type all of that in, you can use the generate_grid function. Put the number of preset values in the brackets, or set it to 0 if you want a default.

This program uses backtracking process to solve. The program finds the zeros i.e. empty spaces in the line and checks the number in range 9 that it unique in that row , column and square. Like that the code goes on checking each and every space in the puzzle. If any number is repeated inside the row and column, then it is backtrack and changes the number in the respective space. The program uses the recursion to backtrack in the puzzle.

The generate_grid function fill the board with numbers and removes them to be sure every grid got a solution.


If you use the generate board function the output will be as following:

=======full board========
3 8 5  | 4 6 9  | 1 7 2
9 6 4  | 1 7 2  | 5 8 3
2 7 1  | 5 8 3  | 4 6 9
- - - - - - - - - - - - -
1 2 6  | 7 3 5  | 8 9 4
4 9 8  | 6 2 1  | 7 3 5
5 3 7  | 8 9 4  | 6 2 1
- - - - - - - - - - - - -
8 4 3  | 9 1 6  | 2 5 7
7 5 2  | 3 4 8  | 9 1 6
6 1 9  | 2 5 7  | 3 4 8
======solvable board=====
3 0 0  | 0 6 9  | 0 0 0
9 0 0  | 0 0 0  | 5 0 0
0 0 0  | 0 0 0  | 0 0 0
- - - - - - - - - - - - -
0 2 0  | 0 0 5  | 8 0 0
0 0 0  | 0 0 1  | 7 0 0
0 0 0  | 8 0 0  | 0 0 1
- - - - - - - - - - - - -
0 0 0  | 0 0 6  | 0 0 7
7 5 0  | 0 4 0  | 0 1 0
6 1 0  | 0 0 0  | 0 0 8
======solved board=======
3 4 5  | 7 6 9  | 1 8 2
9 6 1  | 2 3 8  | 5 7 4
2 8 7  | 5 1 4  | 3 6 9
- - - - - - - - - - - - -
1 2 3  | 4 7 5  | 8 9 6
8 9 4  | 6 2 1  | 7 3 5
5 7 6  | 8 9 3  | 2 4 1
- - - - - - - - - - - - -
4 3 2  | 1 8 6  | 9 5 7
7 5 8  | 9 4 2  | 6 1 3
6 1 9  | 3 5 7  | 4 2 8
