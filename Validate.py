from parser import parse
from Solve import interpret

def parse_output(file):
    inputs = []
    with open(file, 'r') as file:
        inputs = file.readlines()
    for i, number in enumerate(inputs):
        inputs[i] = int(number)
    return inputs


def validate(inputfile, items):
    number_true = items[0]
    items = items[1:]
    items_dict = dict.fromkeys(range(1,len(items)+1))
    for i, key in enumerate(items_dict.keys()):
        items_dict[key] = True if items[i] == 1 else False
    inputfile = inputfile[1:]
    count = 0
    for item in inputfile:
        if interpret(items_dict[abs(item[0])], item[0]) or interpret(items_dict[abs(item[1])], item[1]):
            count += 1
    return count == number_true

if __name__ == "__main__":
    file_name = input("Enter Input File Name:\n")
    sol_name = input("Enter the solution file:\n")
    parsed_input = parse(file_name)
    parsed_solution = parse_output(sol_name)
    print(validate(parsed_input, parsed_solution))
