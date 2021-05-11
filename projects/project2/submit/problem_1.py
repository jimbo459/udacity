def sqrt(number):
    try:
        number = int(number)
    except ValueError:
        return "Error, Input should be an int"

    start = 0
    end = number

    if number == 0 or number == 1:
        return number

    while start <= end:
        mid = (start+end) // 2

        if (mid * mid) == number:
            break
        elif (mid*mid) < number:
            start = mid + 1
        else:
            end = mid - 1

    return round(mid)


def main():
    ### Should print 3
    print(sqrt(9))

    ### Should print 5 (non-whole-number test)
    print(sqrt(27))

    ### Converts string to int - should print 2
    print(sqrt("2"))

    ### Errors if non-int string given - should print "Error, Input should be an int"
    print(sqrt(""))


if __name__ == "__main__":
    main()