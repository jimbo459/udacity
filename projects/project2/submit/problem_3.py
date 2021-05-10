def pivot_sort(list, low, high):
    left_index = low
    pivot_index = high

    while pivot_index != left_index:
        pivot_value = list[pivot_index]
        item_value = list[left_index]

        if item_value <= pivot_value:
            left_index += 1
            continue

        list[left_index] = list[pivot_index - 1]
        list[pivot_index - 1] = pivot_value
        list[pivot_index] = item_value
        pivot_index -= 1

    return pivot_index


def quick_sort(list, low, high):
    if high <= low:
        return

    pivot = pivot_sort(list, low, high)
    quick_sort(list, low, pivot -1)
    quick_sort(list,pivot+1, high)

    return list


def rearrange_digits(input_list):

    sorted_list = quick_sort(input_list, 0, len(input_list) -1)

    str_1 = ""
    str_2 = ""

    first_arr = True

    for number in range(len(sorted_list) - 1, -1, -1):
        if first_arr:
            str_1 += str(input_list[number])
        else:
            str_2 += str(input_list[number])

        first_arr = not first_arr

    return [int(str_1), int(str_2)]


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail. Expected {}, got {}". format(solution, output))


def main():

    test_function([[1, 2, 3, 4, 5], [542, 31]])
    test_function([[4, 6, 2, 5, 9, 8], [964, 852]])


if __name__ == "__main__":
    main()