"""
Hannes and Arnar are going to the cinema. They have already ordered their tickets online and they just ate, so they are not stopping in the lobby for snacks and drinks. Therefore, they will be able to enter the screening room in no time. Hannes is still a bit unsure about when he should get going. Hannes is at his house currently. Before Hannes goes to the cinema he must pick up Arnar. It will take him minutes to drive to Arnar. Then he needs to drive from Arnar’s location to the cinema which will take him minutes. If the film is scheduled to start on minute

of the day, on what minute of the day should Hannes start driving, at the latest, so they do not miss the advertisements?
Input

The input consists of three lines. The first line consists of a single integer
, the number of minutes it takes to drive from Hannes to Arnar. The second line consists of a single integer , the number of minutes it takes to drive from Arnar to the cinema. The third line consists of a single integer

, the minute of the day, on which the film is scheduled to start.
Output

Output a single integer, the latest possible minute of the day, on which Hannes can start driving without them being late.
"""
a= int(input())
b=int(input())
c=int(input())
print(c-a-b)
