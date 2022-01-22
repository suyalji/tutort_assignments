def TOH(n,A=1,B=2,C=3):
    if n > 0:
        TOH(n-1,A,C,B)
        print(f"move a disc from {A} to {C}")
        TOH(n-1,B,A,C)


if __name__ == "__main__":
    inputs = [0,1,2,3,4,5,20]
    for n in inputs:
        print(f"=== n = {n} ======================================")
        TOH(n,1,2,3)