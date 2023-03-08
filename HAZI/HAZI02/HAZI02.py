
import numpy as np






def column_swap(inputArray:np.array)->np.array:
    temp=np.copy(inputArray[:,0])
    inputArray[:,0]=inputArray[:,1]
    inputArray[:,1]=temp
    return inputArray




def compare_two_array(inputArray1:np.array,inputArray2:np.array)->np.array:
    return np.where(np.equal(inputArray1,inputArray2))





def get_array_shape(inputArray:np.array)->str:
   output=""
   a=np.shape(inputArray)
   if (len(a)==2):
      output+=f"sor: {a[0]}, oszlop: {a[1]}, melyseg: 1"
   else:
      output+=f"sor: {a[0]}, oszlop: {a[1]}, melyseg: {a[2]}"

   return output



def encode_Y(InputArray:np.array,classCount:int)->np.array:
    zeroMatrix=np.zeros((classCount,classCount),dtype=int)
    search=np.where(search>=0)
    
    return zeroMatrix
encode_Y(np.array([1, 2, 0, 3]), 4)









def eval_classification(itemList:list,inputArray:np.array)->str:
    index=np.where(inputArray==np.max(inputArray))
    return itemList[index[0][0]]




def repalce_odd_numbers(inputArray:np.array)->np.array:
    inputArray[(inputArray%2!=0)]=-1
    return inputArray




def replace_by_value(inputArray:np.array,compareValue:int)->np.array:
    inputArray[(inputArray<compareValue)]=-1
    inputArray[(inputArray>=compareValue)]=1
    return inputArray




def array_multi(inputArray:np.array):
    return np.prod(inputArray)



def array_multi_2d(inputArray:np.array)->np.array:
    return np.multiply.reduce(inputArray,axis=1)



