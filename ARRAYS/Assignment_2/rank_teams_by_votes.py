def solution(A):

    voters = len(A)
    if voters == 1:
        return A
    candidates = len(A[0])
    my_dict = {}
    for i in A:
        str = ''
        for j in range(candidates):
            





if __name__ == "__main__":
    input = ["ABC","ACB","ABC","ACB","ACB"]
    print(solution(input))