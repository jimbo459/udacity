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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


def main():
    record_exists = {}

    for column in range(2):
        for number in range(len(calls)):
            if not record_exists.get(calls[number][column]):
                record_exists[calls[number][column]] = True

    print("There are {} different telephone numbers in the records.".format(
        len(record_exists)
    ))


if __name__ == "__main__":
    main()

