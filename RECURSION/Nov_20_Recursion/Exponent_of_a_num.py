#without recursion - O(n)
def pow_3(m,n):
    product = 1
    for i in range(n):
        product = product * m
    return product    
# Recursion
def pow(m,n):
    if n == 0:
        return 1
    return pow(m,n-1)*m

# Optimized version 
def pow_2(m,n):
    if n == 0:
        return 1
    if n%2 == 0:
        return pow_2(m*m, n/2)
    else:
        return m*pow_2(m*m, (n-1)/2) 


if __name__ == "__main__":
    print(pow(2,5))
    print(pow_2(2,5))
    print(pow_3(2,5))
    print(pow(4,3))
    print(pow_2(4,3))
    print(pow_3(4,3))
    print(pow(2,0))
    print(pow_2(2,0))
    print(pow_3(2,0))