import sys
import bisect

input_file = "test_input.txt" if "test" in sys.argv else "input.txt"

numbers_left: list[int] = []
numbers_right: list[int] = []
sum = 0

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        numbers = line.split("   ")
        number_left = int(numbers[0])
        number_right = int(numbers[1])
        bisect.insort(numbers_left, number_left)
        bisect.insort(numbers_right, number_right)


for i, num in enumerate(numbers_left):
    num_right = numbers_right[i]
    sum += abs(num_right - num)

print(sum)

