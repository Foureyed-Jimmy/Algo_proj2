from Solve import init_solve
from BatchCaller import batch
from Validate import validate_batch

def main():
    batch("/to_solve_sets", init_solve)
    batch("/to_validate_sets", validate_batch)

if __name__ == "__main__":
    main()