from Solve import init_solve
from os import listdir, getcwd, path

def main():
    solve_path = getcwd() + "/to_solve_sets"
    if not path.exists(solve_path):
        print("No to_solve_sets folder found, please place files to solve in to_solve_sets folder")
        return -1
    for name in listdir(solve_path):
        init_solve(f"{solve_path}/{name}")
            

if __name__ == "__main__":
    main()