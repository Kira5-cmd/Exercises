#making a integer palindrome checker.

def reverse_int(no:int) -> str:
    """reverse a integer."""
    if no<10:
        return no
    else:
        last_digit = no%10
        rest_digit = no//10
        # adding last digit to rest last digit
        return str(last_digit) + str(reverse_int(rest_digit))

def ispalindrome(n:int):
    """return True if int is palindrome else False"""
    # reversing inteer
    reversed_n = int(reverse_int(n))
    #returning value
    return n == reversed_n

#Example
print(ispalindrome(90))
print(ispalindrome(50))
print(ispalindrome(909))