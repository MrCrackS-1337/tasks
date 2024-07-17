import sys
import json

def read_file(file):
    with open(file, 'r', encoding='utf-8') as f:
        return f.read()

def read_json(file):
    file = read_file(file)
    if file:
        file = json.loads(file)
    return file

def write_file(file, data):
    with open(file, 'w', encoding='utf-8') as f:
        f.write(data)
        
values_json = read_json(sys.argv[1])
tests_json = read_json(sys.argv[2])
report_filename = sys.argv[3]

id_values = dict()
for value in values_json.get('values'):
    id_values[value.get('id')] = value.get('value')

def fill_values(name, node):
    array = node[name]
    for element in array:
        if 'id' in element and element['id'] in id_values:
            element['value'] = id_values[element['id']]
        if 'values' in element:
            fill_values('values', element)

fill_values('tests', tests_json)
write_file(report_filename, json.dumps(tests_json))
