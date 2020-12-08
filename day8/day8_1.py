program = []
acc = 0
pc = 0
with open('input', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        op, value = line.split(' ')
        program.append([op, int(value), None])

order = 1
while program[pc][2] is None:
    program[pc][2] = order
    order += 1
    old_pc = pc
    if program[pc][0] == 'nop':
        pc += 1
    elif program[pc][0] == 'acc':
        acc += program[pc][1]
        pc += 1
    elif program[pc][0] == 'jmp':
        pc += program[pc][1]
    print(old_pc, program[old_pc], pc, acc)
print(acc)