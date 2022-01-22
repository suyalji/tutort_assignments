def solution(num):
    my_list = []
    num = str(num)
    for i in num:
        my_list.append(i)
    my_list.sort(reverse=True)
    my_str = ''
    for i in my_list:
        my_str = my_str+i
    
    num = int(num)
    
    my_str = int(my_str)
    
    if my_str > num: 
        return my_str 
    else: return -1
   

if __name__ == "__main__":
    inputs = [12,21,123]
    for num in inputs:
        print(solution(num))