from Solve import init_solve
from BatchCaller import batch

def main():
    batch("/to_solve_sets", init_solve)

if __name__ == "__main__":
    main()