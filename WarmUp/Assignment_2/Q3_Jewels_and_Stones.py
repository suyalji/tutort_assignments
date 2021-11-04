"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""
def solution(jewels,stones):
    stone_counts = {}
    for i in stones:
        if i in stone_counts.keys():
            stone_counts[i] = stone_counts[i] + 1
        else:    
            stone_counts[i] = 1 
    print(stone_counts)        
    sum = 0
    for i in jewels:
        if i in stone_counts.keys():
            sum = sum + stone_counts[i]
    return sum

if __name__ == "__main__":
    jewels = "aA"
    stones = "aAAbbbb"
    print(solution(jewels,stones))
    jewels = "z"
    stones = "ZZ"
    print(solution(jewels,stones))