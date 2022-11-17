def binary_insert_sort(sample: list[int]) -> list[int]:
    sorted_sample = [sample[0]]
    for i in sample[1:]:
        left = 0
        right = len(sorted_sample) - 1
        while left < right:
            middle = (left + right) // 2
            if i > sorted_sample[middle]:
                left = middle + 1
            elif i < sorted_sample[middle]:
                right = middle - 1
            else:
                sorted_sample.insert(middle, i)
                break
        if left == right:
            if sorted_sample[left] >= i:
                sorted_sample.insert(left, i)
            else:
                sorted_sample.insert(left + 1, i)
        elif left > right:
            if i > sorted_sample[left]:
                sorted_sample.insert(left + 1, i)
            else:
                sorted_sample.insert(left, i)
    return sorted_sample
