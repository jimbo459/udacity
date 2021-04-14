"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

def main():
    phone_duration = {}

    for column in range(2):
        for number in range(len(calls)):
            if phone_duration.get(calls[number][column]):
                phone_duration[calls[number][column]] += int(calls[number][3])
            else:
                phone_duration[calls[number][column]] = int(calls[number][3])

    print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(
        max(phone_duration, key=phone_duration.get),
        phone_duration[max(phone_duration, key=phone_duration.get)],
    ))


if __name__ == "__main__":
    main()
