def binary_search(input_list, value):
    string = "Value not found"
    low = 0
    high = len(input_list) - 1
    while low <= high:
        mid = int((low +  high) / 2)
        if input_list[mid] == value:
            print(value)
            return
        elif input_list[mid] < value:
            low = mid + 1
        else:
            high = mid - 1

    print(string)
    return 


def test_cases():
    list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    binary_search(list, 3)
    binary_search(list, 5)
    binary_search(list, 20)

def main():
    test_cases()



main()