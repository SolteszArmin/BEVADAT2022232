
def subset(input_list:list, start:int, end:int) -> list:
    i=start
    output=[]

    while(i<len(input_list) and i<end):
        output.append(input_list[i])
        i=i+1

    return output


def every_nth(inputList:list,n:int)->list:
    return inputList[0::n]


def unique(inputList:list) -> bool:
    for element in inputList:
        if inputList.count(element)>1:
            return False
    return True


def flatten(inputList:list) -> list:
    i=0
    j=0
    output=[]
    while(i<len(inputList)):
        while(j<len(inputList[0])):
            output.append(inputList[i][j])
            j=j+1
        j=0
        i=i+1
    return output


def merge_lists(*args)->list:
    output=[]
    for list in args:
        for element in list:
            output.append(element)
    return output


def reverse_tuples(inputList:list)->list:
    output=[]
    for element in inputList:
        output.append((element[1],element[0]))
    return output


def remove_duplicates(inputList:list)->list:
    output=[]
    for element in inputList:
        if output.__contains__(element)==False:
            output.append(element)
    return output


def split_into_chunks(InputList:list,chunkSize:int)->list:
    output=[]
    start=0
    for i in range(start,len(InputList),chunkSize):
        x=i
        output.append(InputList[x:x+chunkSize])
    return output


def merge_dicts(*dict)->dict:
    output={}
    for d in dict:
        output.update(d)
    return output


def by_parity(inputList:list)->dict:
    evenList=[]
    oddList=[]
    for i in inputList:
        if i%2==0:
            evenList.append(i)
        else:
            oddList.append(i)
    return {"even":evenList,"odd":oddList}



def mean_key_value(dictionary:dict)->dict:
    outputDict={}
    for k,v in dictionary.items():
        sum=0
        for i in v:
            sum=sum+i
        outputDict[k]=sum/len(v)
    return outputDict


