from parser import parse

conditions = {
    "main":[
        lambda header, l: header[0] == len(l),
        lambda header, l: 1 < header[0] < 50000,
    ],
    "list":[
        lambda l, h: abs(l[0]) != abs(l[1]),
        lambda l, h: 0 < abs(l[0]) <= h[1] and 0 < abs(l[0]) <= h[1],
        lambda l, h: DUPECHECK.add(str(l)) == None
    ]
}
DUPECHECK = set()



def validate(items):
    header = items[0]
    l = items[1:]
    for condition in conditions["main"]:
        if not condition(header, l): 
            return False
    for item in l: 
        for condition in conditions["list"]:
            if not condition(item, header):
                return False
    if len(DUPECHECK) != len(l):
        return False
    return True


def validateFile(file):
    parsed_input = parse(file)
    validate(parsed_input)
    


if __name__ == "__main__":
    file_name = input("Enter Input File Name:\n")
    parsed_input = parse(file_name)
    print(validate(parsed_input))
