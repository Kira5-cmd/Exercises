# longest common prefix 
#["flower","flask","flat"] -> fl

def LCP(var:list):
    if not var:
        return ""
    
    var.sort()
    common = ""
    for index,i in enumerate(var[0]):
        if i == var[-1][index]:
            common += i
        else:
            break
    return common

print(LCP(["avinash","ayoush","ankit"]))