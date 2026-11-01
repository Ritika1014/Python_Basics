# Program to print numbers from 1 to 20 except multiples of 3 using continue

for num in range(1, 21):
    if num % 3 == 0:
        continue
    print(num)
