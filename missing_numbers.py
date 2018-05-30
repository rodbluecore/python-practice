#!/usr/bin/env python3

# you are given an array of values that either count


def find_missing_num(arr):
    answer = -1
    skip = find_skip(arr)
    if skip is not False:
        for i in range(0, len(arr) - 1):
            if arr[i] + skip != arr[i + 1]:
                answer = arr[i] + skip
        return answer


def find_skip(arr):
    skip = arr[1] - arr[0]
    skip2 = arr[-1] - arr[-2]
    if skip == skip2:
        return skip
    else:
        skip = arr[-2] - arr[-3]
        skip2 = arr[2] - arr[1]
        if skip == skip2:
            return skip
    return False


if __name__ == '__main__':
    assert find_missing_num([2, 4, 8, 10]) == 6, 'error1'

# next we want to be able to do it for skips
# then we want to be able to do it counting down


