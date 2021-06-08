

def shift_array(array,num):
    if not( type(array) == type([]) ): # If not array
        return 'error' # 1 time only
    if len(array)%2==0:
        midpoint = len(array)//2
        array= array[0:midpoint] + [num]+array[midpoint:]
        print(array)
    else:
        midpoint=len(array)//2 +1
        array= array[0:midpoint] + [num]+array[midpoint:]
        print(array)
shift_array([1,2,3,4,],0)