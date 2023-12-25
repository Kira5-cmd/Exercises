from functools import reduce

def roman(var:int):
    # defining the roman no 
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
        1 : "I"
    }
    #some variables
    remainder = var
    roman_num = ""
    #appending roman nums 
    for no,roman_no in ROMAN_NO.items():
        for i in range(remainder//no):
            roman_num += roman_no
        remainder = remainder % no
    # returning roman no if roman nums are appended.
    return roman_num

# Example to check()
if __name__ == "__main__":
    print(roman(989))