import sys

total = 0
with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        module_fuel = int(line) // 3 - 2
        print(module_fuel)
        last_fuel = module_fuel
        while last_fuel > 0:
            last_fuel = last_fuel // 3 - 2
            print('\t', last_fuel)
            if last_fuel > 0:
                module_fuel += last_fuel
        total += module_fuel
        # input('')

print(total)