#check valid parenthse or not
PARANTHESE = {")":"(", "}":"{", "]":"["}

def isvalid_parenthese(var:str):
    stack = []
    for char in var:
        if char in PARANTHESE:
            top_element = stack.pop() if stack else ""
            if top_element != PARANTHESE[char]:
                return False
        else:
            stack.append(char)
    return not stack

print(isvalid_parenthese("({})}"))