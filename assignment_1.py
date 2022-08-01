
def give_remainder_dict(dividend, divisor, no_of_digits):

    # divides the dividend by divisor and rounds off upto no_of_digits decimal points using round() function
    # convert it into a string using str()
    ans = str(round(dividend/divisor, no_of_digits))

    # trims decimal parts and neglects the integer part
    ans = ans[-10:]

    # default dictionary
    result = {
        "1" : 0,
        "2" : 0,
        "3" : 0,
        "4" : 0,
        "5" : 0,
        "6" : 0,
        "7" : 0,
        "8" : 0,
        "9" : 0,
        "0" : 0,
    }
    
    # loops through each characters of that string
    for i in ans:
        # checks for matches of the dict key and the character 
        if i in result:
            # if there is a match with the key and char then increase the value by 1
            result[f"{i}"] = result[f"{i}"] + 1    

    print(result)

if __name__ == '__main__':

    dividend = 22 
    divisor = 7
    no_of_digits = 10

    give_remainder_dict(dividend, divisor, no_of_digits)    