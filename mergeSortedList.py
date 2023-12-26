# merge sorted list 
# list1 = [2,3,4] ,list2 = [1,2,3] -> 1,2,2,3,3,4

def merge(list1, list2):
    i1 = i2 = 0
    sorted_list = []
    
    while i1 < len(list1) and i2 < len(list2):
        if list1[i1] < list2[i2]:
            sorted_list.append(list1[i1])
            i1 += 1
        else:
            sorted_list.append(list2[i2])
            i2 += 1
    sorted_list.extend(list1[i1:])
    sorted_list.extend(list2[i2:])
    return sorted_list

print(merge([1,2,3], [2,4,5]))