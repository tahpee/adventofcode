import sys
import re
import pprint

program = {}
mask = [0] * 36
with open(sys.argv[1], 'r') as file:
    for l in file.readlines():
        mask_match = re.match(r'mask = ([01X]{36})', l)
        if mask_match:
            mask = mask_match.group(1)
            print(mask)
        mem_match = re.match(r'mem\[(\d+)\] = (\d+)', l)
        if mem_match:
            address = mem_match.group(1)
            value = int(mem_match.group(2))
            s = ''
            for i, m in enumerate(mask):
                if m == '1':
                    s = s + '1'
                elif m == '0':
                    s = s + '0'
                else:
                    s = s + '{:036b}'.format(value)[i]
            program[address] = int(s, 2)
pprint.pprint(program)
print(sum(program.values()))