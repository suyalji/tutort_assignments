import datetime

date = ["24.12.2020",
"21/12/2010",
"30-10-2009",
"24.12.2020",
"17.9.2006",
"20/7/2010"]

def format_date(input_date):
    seperator = ['/','-','.']
    for i in seperator:
        if i in input_date:
            sep = i
            break 
    arr = []
    arr.append(input_date.split(sep))
    dd = arr[0][0] 
    mm = arr[0][1]
    yyyy = arr[0][2]
    return  f"{yyyy}-{mm}-{dd}"  

for i in date:
    print(format_date(i))
