"""
In this problem, your program should read two whole numbers (also called integers) from the input, and print out their sum.

As a refresher, here are some ways to read two numbers from standard input in a few different languages:

# Python 3
line = input()
a, b = line.split()
a = int(a)
b = int(b)

// C++
// make sure to first "#include <iostream>"
int a, b;
std::cin >> a >> b;

// Java
// make sure to first "import java.util.Scanner;"
Scanner s = new Scanner(System.in);
int a = s.nextInt(), b = s.nextInt();

Input

The input contains one line, which has two integers
and , separated by a single space. The bounds on these values are

.
Output

Output the sum of the two integers, 
"""
line=input()
a, b = line.split()
print(int(a)+int(b))
