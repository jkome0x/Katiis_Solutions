"""
The popular streaming platform switch.tv just unveiled their newest feature: switch betting. Streamers can now get their viewers to bet on two different options using switch points (patented).

Each viewer bets some number of switch points for one of the two options. The total amount of switch points bet by everyone is called the prize pool. The streamer will choose one of the options as the winner and the prize pool is split (not necessarily equally) between all the viewers who bet on that option; the more you bet on the option, the more of the prize pool you receive. In particular, if you contributed
of all the bets for one of the options and that option wins, then you receive

of the total prize pool.

The switch.tv team has come to you to compute what the switch point payout is for each viewer if their selected option wins. To do this, they ask you to find the switch-payout-ratio for each of the two options. Since the payout to each viewer is proportional to the number of switch points they put into the bet, the switch team will be able to use this ratio to determine each viewer’s winnings.
For example, suppose a streamer created a switch bet where three viewers participated. Two viewers bet and switch points on option one and the last viewer bets switch points on option two. We can see that option one has % of the bets and option two has % of the bets.
If option one wins, then the two viewers who bet on that receive and switch points, respectively, which means that the switch-payout-ratio is : for option one. If option two wins, then the single viewer who bets on that receives 50 switch points, which means that the switch-payout-ratio is :.
Given the percentage of total bets for option one, help switch.tv by computing the switch-payout-ratio for the two options.
Input

The input consists of one integer
(

), which is the percentage of switch points bet on option one.
Output

For each option (option one, then option two), display the number x such that 1:x is the switch-payout-ratio for that option. Your answer should have an absolute or relative error of at most
."""
n=float(input())
print(100/n)
print(100/(100-n))
