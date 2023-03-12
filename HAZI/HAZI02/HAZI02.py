
import numpy as np

def column_swap(inputArray:np.array)->np.array:
    inputArray=np.fliplr(inputArray)
    return inputArray

def compare_two_array(inputArray1:np.array,inputArray2:np.array)->np.array:
    return np.where(np.equal(inputArray1,inputArray2))

def get_array_shape(inputArray:np.array)->str:
   output=""
   a=np.shape(inputArray)
   if (len(a)==1):
      output+=f"sor: {a[0]}, oszlop: 1, melyseg: 1"
   elif(len(a)==2):
      output+=f"sor: {a[0]}, oszlop: {a[1]}, melyseg: 1"
   else:
      output+=f"sor: {a[0]}, oszlop: {a[1]}, melyseg: {a[2]}"
   return output

def encode_Y(InputArray:np.array,classCount:int)->np.array:
    zeroMatrix = np.zeros((len(InputArray),classCount),dtype=int)
    zeroMatrix[np.arange(len(InputArray)),InputArray]=1
    return zeroMatrix

def decode_Y(inputArray:np.array)->np.array:
    return np.argmax(inputArray,axis=1)

def eval_classification(itemList:list,inputArray:np.array)->str:
    index=np.where(inputArray==np.max(inputArray))
    return itemList[index[0][0]]

def repalce_odd_numbers(inputArray:np.array)->np.array:
    inputArray[inputArray%2!=0]=-1
    return inputArray

def replace_by_value(inputArray:np.array,compareValue:int)->np.array:
    inputArray[(inputArray<compareValue)]=-1
    inputArray[(inputArray>=compareValue)]=1
    return inputArray

def array_multi(inputArray:np.array):
    return np.prod(inputArray)


def array_multi_2d(inputArray:np.array)->np.array:
    return np.multiply.reduce(inputArray,axis=1)

def add_border(inputArray:np.array)->np.array:
    return np.pad(inputArray,pad_width=1,mode='constant',constant_values=0)

def list_days(startDate:str,endDate:str)->np.array:
    return np.array(np.arange(startDate+'-01',endDate+'-01',dtype=np.datetime64))

def actual_date()->np.datetime64:
    return np.datetime64('now','D')

def sec_from_1970()->int:
    return np.datetime64('now','s') - np.datetime64('1970-01-01T00:02:00')
