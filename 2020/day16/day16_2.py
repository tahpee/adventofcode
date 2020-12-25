import sys
import re

rules = {}
my_ticket = []
other_tickets = []

# Load the input data
with open(sys.argv[1], 'r') as file:
    for i, section in enumerate(file.read().split('\n\n')):
        if i == 0:
            # Rules section
            for line in section.split('\n'):
                match = re.match(r'([\w\s]+): (\d+)-(\d+) or (\d+)-(\d+)', line)
                if match:
                    rules[match.group(1)] = [range(int(match.group(2)), int(match.group(3))+1), range(int(match.group(4)), int(match.group(5))+1)]
        if i == 1:
            for line in section.split('\n'):
                # My Ticket
                match = re.match(r'^(\d+),(\d+).*', line)
                if match:
                    my_ticket = [int(x) for x in line.strip().split(',')]
        if i == 2:
            # Other tickets
            for line in section.split('\n'):
                match = re.match(r'^(\d+),(\d+).*', line)
                if match:
                    other_tickets.append([int(x) for x in line.strip().split(',')])


def validate(rules, ticket):
    """Validate a ticket given a set of rules and a ticket"""
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


# Build a list of valid ticket
valid_tickets = []
for ticket in other_tickets:
    if len(validate(rules, ticket)) == 0:
        valid_tickets.append(ticket)


def trans(M):
    """ Transpose a 2D Array"""
    # Stack overflow https://stackoverflow.com/a/23393593
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0]))]

# Get a list of columns
transposed_tickets = trans(valid_tickets)
rule_columns = {}
# Evaluate each column of valid ticket fields and build a list of possible rule -> field mappings.
# Some rules have multiple possible columns. Each rule is a set
for i, column in enumerate(transposed_tickets):
    for rule in rules:
        valid = True
        for val in column:
            # print('\t', val)
            if val not in rules[rule][0] and val not in rules[rule][1]:
                valid = False
        if valid:
            rule_columns.setdefault(rule, set())
            rule_columns[rule].add(i + 1)

def rules_have_one_column(rule_columns):
    """ Check each rule_column set for a length of one.
    Only once all rules have a single possible column are we done"""
    for rule in rule_columns:
        if len(rule_columns[rule]) > 1:
            return False
    return True


# Thin the rules, looking for rules that only have one column and then remove that column from the possible other rules
while not rules_have_one_column(rule_columns):
    for outer_rule in rules:
        if len(rule_columns[outer_rule]) == 1:
            outer_rule_column = list(rule_columns[outer_rule])[0]
            for inner_rule in rules:
                if outer_rule != inner_rule and outer_rule_column in rule_columns[inner_rule]:
                    rule_columns[inner_rule].remove(outer_rule_column)
print(rule_columns)

# Convert the sets to values now that each only has one item
for rule in rule_columns:
    rule_columns[rule] = list(rule_columns[rule])[0]

# Finally find the columns that match the departure and calculate the final value
departure_fields = []
total = 1
for rule in rule_columns:
    if rule.startswith('departure'):
        departure_fields.append(my_ticket[rule_columns[rule]-1])
        total = total * my_ticket[rule_columns[rule]-1]
print(departure_fields)
print(total)

