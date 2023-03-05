
def contains_odd(listOfNumbers : list) -> bool:
    value=False
    for num in listOfNumbers:
        if num%2!=0:
            value=True
    return value


def is_odd(listOfNumbers : list) -> list:
    list=[]
    for number in listOfNumbers:
        if number%2==0:
            list.append(False)
        else:
            list.append(True)
    return list


def element_wise_sum(list_0 : list,list_1 : list) -> list:
    output=[]
    i=0
    j=0
    while(i<len(list_0) and j<len(list_1)):
        output.append(list_0[i]+list_1[j])
        i=i+1
        j=j+1
    while(i<len(list_0)):
        output.append(list_0[i])
        i=i+1
    while(j<len(list_1)):
        output.append(list_1[j])
        j=j+1
    return output



def dic_to_list(dictionary:dict) -> list:
    output=[]
    for key,value in dictionary.items():
        output.append((key,value))
    return output


