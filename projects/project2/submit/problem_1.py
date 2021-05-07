def sqrt(number):
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
    print("Pass" if (3 == sqrt(9)) else "Fail")
    print("Pass" if (0 == sqrt(0)) else "Fail")
    print("Pass" if (4 == sqrt(16)) else "Fail")
    print("Pass" if (1 == sqrt(1)) else "Fail")
    print("Pass" if (5 == sqrt(27)) else "Fail")


if __name__ == "__main__":
    main()