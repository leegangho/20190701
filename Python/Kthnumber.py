def out_k(array,list):
    array=array[list[0]-1:list[1]]
    array.sort()
    print(array)
    out_num=array[list[2]-1]
    return out_num

print(out_k([1,5,2,6,3,7,4],[2,5,3]))