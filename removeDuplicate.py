#it will remove all the duplicated from the list
#[1,2,2,3,3,4] -> [1,2,3,4]
def removeDuplicate(var:list[int]):
    # makign index variables
    index1 = 0
    index2 = 1
    #loop exits when every ints are checked
    while index2 < len(var):
        if var[index1] == var[index2]:
            var.pop(index2)
        index1 += 1
        index2 += 1
    #returning the removed duplicated list
    return var