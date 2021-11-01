"""
Part 1 : In a string , find frequency of all characters 
Part 2 : Print alphabet with higest frquency 
"""
# Approach 1
def list_occurances(input):
    # part 1 - preparing stats for each alphabet  O(n)
    n = len(input)
    my_dict = {}
    for i in range(n):
        if input[i] in my_dict:
            my_dict[input[i]] = my_dict[input[i]]+1
        else:
            my_dict[input[i]] = 1    
    # part 2 , calculating the alphabet with highest frequency O(n)
    max_value = 0
    alphabet = ""
    for key in my_dict.keys():
        if my_dict[key] > max_value:
            max_value = my_dict[key]
            alphabet = key
    return (my_dict,alphabet)

if __name__ == "__main__":
    string_list = ["aaabbbc","hgghghhhhhghghghjghghghjghgghhjyutut7etuitruegue8tyeiughjhgjdhgjkd",""]
    for pick_str in string_list:
        stats,alphabet = list_occurances(pick_str)
        print(f"Occurences : {stats}")
        print(f"Winner alphabet : {alphabet}")

