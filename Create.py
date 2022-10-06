from operator import sub
import random

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
MAX_CLAUSE = 50000
def generateInput():
    arr = []
    clauses = random.randint(1,50000) #clauses
    variables = random.randint(2,40)  #variables per clause
    var_array = range(1, variables + 1)
    input_array = []
    
    #generate valid clauses
    # for i, num in enumerate(var_array):
    #     for num2 in range(i + 2, variables):
    #         for subArr in gen_struct:
    #             if random.randint(0, 10) == 5:
    #                 input_array.append([num * subArr[0], num2 * subArr[1]])
    # if len(input_array) > MAX_CLAUSE:
    #     input_array = input_array[splice(MAX_CLAUSE)]
    while len(input_array) <= clauses:
        struct = gen_struct[random.randint(0,3)]
        input_array.append([struct[0] * var_array[random.randint(0, len(var_array)-1)], struct[1] * var_array[random.randint(0, len(var_array)-1)]])
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
    inp = generateInput()
    fileName = input("Enter your file name:\n")
    writeFile(fileName, inp)


if __name__ == "__main__":
    main()