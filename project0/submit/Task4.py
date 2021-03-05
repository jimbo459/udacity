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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Input calls,texts

Output: 
    list of numbers
        Make outgoing calls
        Never send texts
        Never receive text
        Never receive incoming calls

Mechanical solution:
    if number is in outgoing list, but not any other column then it satisfies the criteria


Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""


def main():

    not_telemarketer_numbers = []

    for index in calls:
        not_telemarketer_numbers.append(index[1])

    for index in texts:
        not_telemarketer_numbers.append(index[0])
        not_telemarketer_numbers.append(index[1])

    not_telemarketer_numbers = list(dict.fromkeys(not_telemarketer_numbers))

    telemarketer_numbers = {}

    for index in calls:
        if index[0] not in not_telemarketer_numbers:
            if not telemarketer_numbers.get(index[0]):
                telemarketer_numbers[index[0]] = True

    telemarketer_numbers = sorted(telemarketer_numbers.keys())

    print("These numbers could be telemarketers:\n",*telemarketer_numbers, sep="\n")


if __name__ == "__main__":
    main()

