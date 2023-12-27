#romove element
#remove([1,2,3,4,5,5,3,3,3], 3) -> 1,2,4,5,5


def remove_element(var:list, element):
    index = 0
    while index < len(var):
        if element == var[index]:
            var.pop(index)
        else:
            index+=1
    return var
