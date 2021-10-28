"""Q9. Write a program to find the sum of the given series 1+2+3+ . . . . . .(N terms)"""

n = int(input())

# Approach 1
sum = n*(n+1)/2;  # direct formula
print(int(sum))

# Approach 2
sum = 0
for i in range(n+1):
    sum = sum+i
print(sum)    
