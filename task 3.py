import random


# Выбрал сортировку Хоара, так как временная сложность у нее O(n*log(n)), в наихудшем случае O(n^2).
def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = random.choice(numbers)
    lesser_numbers = [number for number in numbers if number < pivot]
    greater_numbers = [number for number in numbers if number > pivot]
    equal_numbers = [pivot] * numbers.count(pivot)
    return quick_sort(lesser_numbers) + equal_numbers + quick_sort(greater_numbers)


nums = [random.randint(1, 50) for i in range(50)]
if __name__ == '__main__':
    print(quick_sort(nums))
