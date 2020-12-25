import sys
import re

rules = {}
my_ticket = []
other_tickets = []

with open(sys.argv[1], 'r') as file:
    for i, section in enumerate(file.read().split('\n\n')):
        if i == 0:
            # Rules section
            for line in section.split('\n'):
                match = re.match(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)', line)
                if match:
                    print(match.groups())
                    rules[match.group(1)] = [range(int(match.group(2)), int(match.group(3))+1), range(int(match.group(4)), int(match.group(5))+1)]
        if i == 1:
            for line in section.split('\n'):
                # My Ticket
                match = re.match(r'^(\d+),(\d+).*', line)
                if match:
                    my_ticket = [int(x) for x in line.strip().split(',')]
        if i == 2:
            # Other ticets
            for line in section.split('\n'):
                match = re.match(r'^(\d+),(\d+).*', line)
                if match:
                    other_tickets.append([int(x) for x in line.strip().split(',')])


def validate(rules, ticket):
    invalid_fields = []
    print("{}: ".format(ticket), end='')
    for field in ticket:
        valid = False
        for rule in rules:
            if field in rules[rule][0] or field in rules[rule][1]:
                valid = True
        if not valid:
            invalid_fields.append(field)

    if len(invalid_fields):
        print('invalid', invalid_fields)
    else:
        print('valid')
    return invalid_fields

print(rules)
print(my_ticket)
print(other_tickets)

validate(rules, my_ticket)
invalid_fields = []
for ticket in other_tickets:
    invalid_fields += validate(rules, ticket)
print(invalid_fields)
print(sum(invalid_fields))