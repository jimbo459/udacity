def get_pivot(arr, low, high):
    if low > high:
        return -1
    if low == high:
        return low

    mid = (low + high) // 2

    if mid < high and arr[mid] > arr [mid + 1]:
        return mid
    elif low < mid and arr[mid] < arr[mid - 1]:
        return mid - 1
    elif arr[low] >= arr[mid]:
        return get_pivot(arr, low, mid -1)

    return get_pivot(arr, mid+1, high)


def binary_search(arr, value):
    start = 0
    end = len(arr) - 1

    while start <= end:
        target = (start + end) // 2
        if arr[target] == value:
            return target
        elif arr[target] < value:
            start = target + 1
        else:
            end = target - 1

    return -1


def rotated_array_search(input_list, number):
    for digit in input_list:
        if digit is None:
            return "Error, only int data type allowed"

    pivot = get_pivot(input_list, 0, (len(input_list) - 1))

    if pivot == -1:
        return -1

    if input_list[pivot] == number:
        return pivot
    elif input_list[0] <= number:
        return binary_search(input_list[:pivot+1], number)
    else:
        return (pivot+1) + binary_search(input_list[pivot+1:], number)


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


def main():
    ### General test cases - should print 0
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 6))

    ### General test cases - should print 5
    print(rotated_array_search([6, 7, 8, 9, 10, 1, 2, 3, 4], 1))

    ### Handles negative numbers - should print 3
    print(rotated_array_search([6, 7, 8, -1, 2, 3, 4], -1))

    ### Handles null value - returns error "Error, only int data type allowed"
    print(rotated_array_search([None, 1,2,3], 3))


if __name__ == "__main__":
    main()