from operator import sub
import random

def powerset(set):
    if not set:
        return [[]]
    ps = powerset(set[1:])
    return ps + [[set[0]] + n for n in ps]



# [a, b, c, d, e]

# a b
# -a b
# a -b
# -a -b
# a c
# -a c
# a -c
# b c
# -b c


gen_struct = [
    [1, 1],
    [-1, 1],
    [1, -1],
    [-1, -1]
    ]

def generateInput():
    arr = []
    # clauses = random.randint(1,50000) #clauses
    variables = random.randint(2,40)  #variables per clause
    var_array = range(1, variables + 1)
    input_array = []
    
    #generate valid clauses
    for i, num in enumerate(var_array):
        for num2 in range(i + 2, variables):
            for subArr in gen_struct:
                input_array.append([num * subArr[0], num2 * subArr[1]])
    clauses = len(input_array)
    arr.append([clauses, variables])
    arr.append(input_array)  
    return arr

def writeFile(fileName, arr):
    with open(fileName, "w") as file:
        file.write(f"{arr[0][0]} {arr[0][1]}\n")
        for item in arr[1]:
            file.write(f"{item[0]} {item[1]}\n")
    file.close()

def main():
    input = generateInput()
    writeFile("testfile.txt", input)


if __name__ == "__main__":
    main()