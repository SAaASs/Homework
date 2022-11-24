import math
import time
import random

NUMBER_OF_ELEMENTS_IN_TEST_LIST = 10000
NUMBER_OF_TESTS = 10
RAND_MAX = 10000

def generate_list(number_of_elements):
    list_ = [0] * number_of_elements
    for index in range(number_of_elements):
        list_[index] = random.randint(-RAND_MAX, RAND_MAX)
    return list_

def BubbleSort(list_):
    swapped = True
    last_index = len(list_)
    while swapped:
        swapped = False
        for index in range(last_index - 1):
            if list_[index] > list_[index + 1]:
                list_[index], list_[index + 1] = list_[index + 1], list_[index]
                swapped  = True
        last_index -= 1
    return list_

def sort_check(list_):
    for index in range(len(list_) - 1):
        if list_[index] > list_[index + 1]:
            return False
    return True
def bin_ins_sort(sample: list[int]) -> list[int]:
    sorted = [sample[0]]
    for i in sample[1:]:
        left = 0
        right = len(sorted) - 1
        while left < right:
            middle = (left + right) // 2
            if i > sorted[middle]:
                left = middle + 1
            elif i < sorted[middle]:
                right = middle - 1
            else:
                sorted.insert(middle, i)
                break
        if left == right:
            if sorted[left] >= i:
                sorted.insert(left, i)
            else:
                sorted.insert(left + 1, i)
        elif left > right:
            if i > sorted[left]:
                sorted.insert(left + 1, i)
            else:
                sorted.insert(left, i)
    return sorted

def test(func):
    total_timer = 0
    for test_number in range(NUMBER_OF_TESTS):
        test_list = generate_list(NUMBER_OF_ELEMENTS_IN_TEST_LIST)
        timer = time.time()
        test_list = func(test_list)
        timer = time.time() - timer
        total_timer += timer
        if sort_check(test_list):
            print("Required time in test №", test_number + 1, "is", timer, "seconds")
        else:
            print("Error in test №",test_number + 1)
    print("Required time for",NUMBER_OF_TESTS, "tests is", total_timer, "seconds")
    print("Average time for",NUMBER_OF_TESTS, "tests is", total_timer/NUMBER_OF_TESTS, "seconds")


print(bin_ins_sort(generate_list(20)))
print(bin_ins_sort(generate_list(20)))
print(bin_ins_sort(generate_list(20)))
print(bin_ins_sort(generate_list(20)))
    
    
