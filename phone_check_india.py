#! /bin/usr/python3

def find_phone_number_india(text):
    numbers=[] #list 
    digits="" #string

    for ch in text:
        if ch.isdigit():
            digits+=ch
        else:
            # when a non-digit appears, check the collected chunk
            if len(digits) >=10:
                start_in= max(0,text.find(digits)-3)
                prefix=text[start_in:start_in+3]

                if len(digits) == 12 and digits.startswith("91"):
                    numbers.append("+{}".format(digits))
                elif len(digits) == 10 and digits[0] in "6789":
                    numbers.append(digits)
            digits=""

    if len(digits) >=10:
        if len(digits) ==12 and digits.startswith("91"):
            numbers.append(f"+{digits}")
        elif len(digits) == 10 and digits[0] in "6789":
            numbers.append(digits)
    return numbers

text="Contact +917737072823 or 8764225729 or 23148231094890213"
print(find_phone_number_india(text))
