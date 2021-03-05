"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

## Inputs: List of calls caller | callee

## parameters:
Find Bangalore numbers in left collumn: (080) prefix
Get Area code (Fixed lines enclosed in brackets || start with 140)/ mobile prefix (first four digits)

Bangalore numbers (080) start
## Banglore number => captureNumber in list. 

## Output: Area code, Mobile prefix. One per line, no duplicates in lexicographic order

##: mechanical solution: 
# If caller starts with (080)
#   if callee start with (
        get number in brackets
    if callee starts with 140
        get 140
    else 
       get first four digits of number

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""


def main():

    called_codes = []

    for index in calls:
        if index[0].startswith("(080)"):
            if index[1].startswith("("):
                called_codes.append(index[1][1:index[1].find(")")])
            elif index[1].startswith("140"):
                called_codes.append("140")
            else:
                called_codes.append(index[1][0:4])

    bangalore_count = 0
    for i in called_codes:
        if i == "080":
            bangalore_count += 1

    bangalore_percent = (bangalore_count/len(called_codes))

    # Remove duplicates from list b
    called_codes = list(dict.fromkeys(called_codes))

    list.sort(called_codes)

    print("The numbers called by people in Bangalore have codes:", *called_codes, sep="\n", end="\n\n")
    print("{:.2%} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(
        bangalore_percent
    ))


if __name__ == "__main__":
    main()
