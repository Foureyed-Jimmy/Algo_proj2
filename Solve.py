from parser import parse
import os

def interpret(value, statement):
    if statement < 0: 
        return not value
    return value

def get(d, value):
    b = d[abs(value)]["set"]
    if value < 0:
        return not b
    return b


def write_file(arr, count,f_name):
    if not os.path.exists("solutions"): 
        os.mkdir("solutions")
    with open(f"solutions/{f_name.split('/',100000)[-1].split('.',2)[0]}_output.txt", 'w') as file:
        file.write(str(count) + "\n")
        for item in arr:
            file.write(str(item) + "\n")


def genDict(size):
    parent = dict.fromkeys(range(1,size + 1), None)
    for key in parent.keys(): #{1:{True:2,False:1}, 2:{True:2, False:1}}
        parent[key] = dict.fromkeys([True, False, "set"], 0)
    return parent

def solve(vals):
    header = vals[0]
    vals = vals[1:]
    pos_combs = [[True, True], [True, False], [False, True], [False, False]]
    d = genDict(header[1])
    for i in range(len(vals)):
        for j in range(len(pos_combs)):
            if interpret(pos_combs[j][0], vals[i][0]) or interpret(pos_combs[j][1], vals[i][1]):
                d[abs(vals[i][0])][pos_combs[j][0]] += 1
                d[abs(vals[i][1])][pos_combs[j][1]] += 1
    for key in d.keys():
        item  = d[key]
        item["set"] = item[True] >= item[False]
    count = 0
    
    for item in vals:
        value = get(d, item[0]) or get(d, item[1])
        if value:
            count += 1 
    sol_arr = [(1 if d[key]["set"] else 0) for key in d.keys()]
    return (sol_arr, count)
    
def init_solve(filename):
    parsed_input = parse(filename)
    (arr, count) = solve(parsed_input)
    write_file(arr, count, filename)

if __name__ == "__main__":
    inp = input("Enter The Text File Name:\n")
    parsed_input = parse(inp)
    (arr, count) = solve(parsed_input)
    write_file(arr, count, inp)