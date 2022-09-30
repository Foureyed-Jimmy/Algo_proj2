def parse(file):
    array = []
    with open(file, "r") as file:
        lines = file.readlines()
    for line in lines:
        line = line.replace("\n", '')
        arr = line.split(' ')
        for i, num in enumerate(arr):
            arr[i] = int(num)
        array.append(arr)
    return array