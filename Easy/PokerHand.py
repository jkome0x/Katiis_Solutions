"""
You are given a five-card hand drawn from a standard -card deck. The strength of your hand is the maximum value such that there are

cards in your hand that have the same rank.

Compute the strength of your hand.
Input

The input will consist of a single line, with five two-character strings separated by spaces.

The first character in each string will be the rank of the card, and will be one of A23456789TJQK. The second character in the string will be the suit of the card, and will be one of CDHS.

You may assume all the strings are distinct.
Output

Output, on a single line, the strength of your hand.
"""



n=str(input()).split()
okay=[]
s=0
for i in n:
    okay.append(i[0])
for i in okay:
    b=okay.count(i)
    if b>s:
        s=b
print(s)
