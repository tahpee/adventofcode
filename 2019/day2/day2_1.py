import sys

program = []
with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        for opcode in line.split(','):
            program.append(int(opcode))
print(program)

# Replace with 1202
program[1] = 12
program[2] = 2
valid_opcodes = [1, 2]
pc = 0
while program[pc] != 99 and program[pc] in valid_opcodes:
    print(pc, program[pc:pc+4])
    if program[pc] == 1:
        # Add
        program[program[pc+3]] = program[program[pc+1]] + program[program[pc+2]]
    if program[pc] == 2:
        # Multiply
        program[program[pc+3]] = program[program[pc+1]] * program[program[pc+2]]
    pc = pc + 4


print(program[0])
