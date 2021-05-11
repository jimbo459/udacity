def get_min_max(ints):
    if len(ints) < 1:
        return None

    min = ints[0]
    max = ints[0]

    for int in ints:
        if int < min:
            min = int
        elif int > max:
            max = int

    return (min,max)


def main():

    ### Unsorted list
    list_1 = [0,1,2,3,5,4,6,7,8,9]

    print("Pass" if ((0, 9) == get_min_max(list_1)) else "Fail")

    ### List containing negative numbers
    list_2 = [-5, 0, -1,-1,-1]

    print("Pass" if ((-5, 0) == get_min_max(list_2)) else "Fail")

    ### List of duplicates
    list_3 = [0, 0, 0, 0, 0]

    print("Pass" if ((0, 0) == get_min_max(list_3)) else "Fail")

    ### Empty list
    list_4 = []

    print("Pass" if (None == get_min_max(list_4)) else "Fail")

if __name__ == "__main__":
    main()