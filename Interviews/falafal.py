def getUniqueCharacter(s):
    # Write your code here
    my_dict = {}
    if not len(s):
        return -1
    
    for i in s:
        if i in my_dict.keys():
            my_dict[i] = my_dict[i]+1
        else:
            my_dict[i] = 1
    unique_list = []        
    for key,value in my_dict.items():
        if value == 1:
            unique_list.append(key)
    for i in s:
        if i in unique_list:
            return s.index(i)+1        
    return -1        
            
if __name__ == "__main__":
    s = ""
    print(getUniqueCharacter(s))            
