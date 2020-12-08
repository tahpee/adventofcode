import copy

original_program = []
with open('input', 'r') as file:
    for line in file.readlines():
        line = line.strip()
        op, value = line.split(' ')
        original_program.append([op, int(value), None])

last_change = 0
success = False
while not success:
    program = copy.deepcopy(original_program)
    if program[last_change][0] == 'nop':
        program[last_change][0] = 'jmp'
    elif program[last_change][0] == 'jmp':
        program[last_change][0] = 'nop'
    if program[last_change][0] in ['jmp', 'nop']:
        # If we changed a jmp or a nop run the program
        acc = 0
        pc = 0
        order = 0
        while pc < len(program) and program[pc][2] is None:
            if pc == (len(program)-1):
                success = True
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
    last_change += 1
print(last_change, len(program), pc, acc)

