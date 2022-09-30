from parser import parse



def interpret(value, statement):
    if statement < 0: 
        return not value
    return value

def genDict(size):
    parent = dict.fromkeys(range(1,size), None)
    for key in parent.keys():
        parent[key] = dict.fromkeys([True, False], 0)
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
    print(d)

if __name__ == "__main__":
    inp = input("Enter The Text File Name:\n")
    parsed_input = parse(inp)
    solve(parsed_input)