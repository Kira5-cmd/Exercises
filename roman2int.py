ROMAN_NO ={"I":1, "V":5 ,"X":10, "L":50, "C":100, "D":500, "M":1000}

def roman2int(roman_var):
    result = 0
    previous_val = 0
    for i in roman_var[::-1]:
        if ROMAN_NO[i] < previous_val:
            result -= ROMAN_NO[i]
        else:
            result += ROMAN_NO[i]
        previous_val = ROMAN_NO[i]
    return result

print(roman2int("dm".upper()))