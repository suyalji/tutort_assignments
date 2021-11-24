"""
Find Element in Circularly Sorted Array in O(logn)
"""

if __name__ == "__main__":
    inputs = [[2,3,4,5,6,1],[7,8,9,1,2,3,4,5,6]]
    for arr in inputs:
        mini = min(arr)
        index = arr.index(mini)
        print(f"The Array {arr} is Rotated {index} times  ")
        
