"""
How many times a Sorted Array is Rotated 
"""

if __name__ == "__main__":
    inputs = [[2,3,4,5,6,1],[7,8,9,1,2,3,4,5,6],[15, 18, 2, 3, 6, 12],[7, 9, 11, 12, 5]]
    for arr in inputs:
        mini = min(arr)
        index = arr.index(mini)
        print(f"The Array {sorted(arr)} is Rotated {index} times as {arr} ")
        
