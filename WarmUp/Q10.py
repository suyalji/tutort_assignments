"""Q10. Given a number N. Your task is to check whether it is fascinating or not.
Fascinating Number: When a number(should contain 3 digits or more) is multiplied by 2 and 3 ,and
when both these products are concatenated with the original number, then it results in all digits from 1
to 9 present exactly once."""

# Approach 1
def facinating(n):
    if n > 99:
        p1 = n * 2
        p2 = n * 3
        num = f"{n}"+f"{p1}"+f"{p2}"
        a = []
        for i in num:
            a.append(i)
        for i in range (1,9):
            if str(i) not in a:
               print("NotFascinating")
               return 
        print("Fascinating")    
                
# Approach 2 


if __name__ == "__main__":
    n = int(input())
    facinating(n)
