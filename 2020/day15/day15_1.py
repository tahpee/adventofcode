#numbers = [0, 20, 7, 16, 1, 18, 15]
numbers = [0, 3, 6]

for i in range(1, 2020):
    last_spoken = numbers[-1]
    print(f'{last_spoken=}')
    previous_spoken = None
    try:
        previous_spoken = numbers[:-1].index(numbers[-1], -1)
    except ValueError:
        numbers.append(0)
    if previous_spoken:
        print(previous_spoken)
        numbers.append(len(numbers)-previous_spoken)
    print(numbers)
    input("")