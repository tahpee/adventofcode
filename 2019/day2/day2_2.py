import sys
import copy

program = []
with open(sys.argv[1], 'r') as file:
    for line in file.readlines():
        for opcode in line.split(','):
            program.append(int(opcode))
print(program)

def run(test_noun, test_verb, program):
    program[1] = test_noun
    program[2] = test_verb
    valid_opcodes = [1, 2]
    pc = 0
    while program[pc] != 99:
        opcode = program[pc]
        assert program[pc] in valid_opcodes, f'Invalid opcode {opcode}'
        noun = program[pc+1]
        verb = program[pc+2]
        destination = program[pc+3]
        print(pc, program[pc:pc+4], opcode, noun, verb, destination)
        if opcode == 1:
            # Add
            program[destination] = noun + verb
        if opcode == 2:
            # Multiply
            program[destination] = noun * verb
        pc = pc + 4
        print(program)
    # print(program[0])
    return program[0]

# test_noun = -1
# result = 0
# target = 19690720
# while result != target:
#     test_noun += 1
#     test_verb = -1
#     while result != target and test_verb < 256:
#         test_program = copy.copy(program)
#         result = run(test_noun, test_verb, test_program)
#         print(test_noun, test_verb, result)
#         test_verb += 1

print(run(12, 2, program))