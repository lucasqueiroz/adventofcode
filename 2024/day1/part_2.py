import sys
import bisect

input_file = "test_input.txt" if "test" in sys.argv else "input.txt"

numbers_left: list[int] = []
numbers_right: list[int] = []
score = 0

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        numbers = line.split("   ")
        number_left = int(numbers[0])
        number_right = int(numbers[1])
        bisect.insort(numbers_left, number_left)
        bisect.insort(numbers_right, number_right)


for num in numbers_left:
    appearances = numbers_right.count(num)
    score += (num * appearances)

print(score)

