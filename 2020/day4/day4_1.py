import re
import pprint

def str_to_record(str):
    record = {}
    for kv in record_str.strip().split(' '):
        key, value = kv.split(':')
        record[key] = value
    return record

records = []
record_str = ""
with open("input", 'r') as f:
    for i, l in enumerate(f.readlines()):
        if l == "\n":
            records.append(str_to_record(record_str))
            record_str = ""
        else:
            record_str = " ".join([l.strip(), record_str])
# Handle the last blank line
if l != '\n':
    records.append(str_to_record(record_str))

valid_set = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
valid_set_with_cid = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
valid_eye_colors = {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}
valid = 0
for record in records:
    if valid_set == set(record.keys()) or valid_set_with_cid == set(record.keys()):
        if 1920 <= int(record['byr']) <= 2002:
            if 2010 <= int(record['iyr']) <= 2020:
                if 2020 <= int(record['eyr']) <= 2030:
                    if ('cm' in record['hgt'] and 150 <= int(record['hgt'].split('cm')[0]) <= 193) or ('in' in record['hgt'] and 59 <= int(record['hgt'].split('in')[0]) <= 76):
                        if re.match(r'^#[0-9a-f]{6}$', record['hcl']) is not None:
                            if record['ecl'] in valid_eye_colors:
                                if re.match(r'^[0-9]{9}$', record['pid']):
                                    valid += 1
print(valid)
