#int to roman with recursion not iteration
# defining romanNO
ROMAN_NO = {
        1000 : "M",
        900: "CM",
        500 : "D",
        400 : "CD",
        100 : "C",
        90 : "XC",
        50 : "L",
        40 : "XL",
        10 : "X",
        9 : "IX",
        5 : "V",
        4 : "IV",
        1 : "I",
        0:""
    }

def roman(var:int):
    """return roman no"""
    if var in ROMAN_NO:
        return ROMAN_NO[var]
    else:
        for n,val in ROMAN_NO.items():
            if var>=n:
                return val + roman(var - n)
        
print(roman(809))