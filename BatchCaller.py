from os import listdir, getcwd, path


def batch(os_path:str, func):
    os_path = getcwd() + os_path
    if not path.exists(os_path):
        print(f"{os_path} does not exist, please place files to run function on")
        return
    for name in listdir(os_path):
        func(f"{os_path}/{name}")
        
if __name__ == "__main__":
    batch(".", print)