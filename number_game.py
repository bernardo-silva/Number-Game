import sys
from itertools import permutations, product


def find_goal(numbers, goal, find_all=False):
    operations = ["+", "-", "*", "/", "(", ")"]
    n_ops = len(numbers)-1
    numbers = permutations(numbers)
    operations = product(operations, repeat=n_ops)

    operation = ""
    tested = 0
    valid = []
    for N, ops in product(numbers, operations):
        tested += 1
        operation = str(N[0])
        for n, op in zip(N[1:], ops):
            operation += op + str(n)
            try:
                result = eval(operation)
            except SyntaxError:
                continue
            if(result == goal):
                valid += [operation]
                if not find_all:
                    return valid
    return valid


if __name__ == "__main__":
    try:
        numbers = list(map(int, sys.argv[1:-1]))
        if len(numbers) < 2:
            raise ValueError
        goal = int(sys.argv[-1])
    except ValueError:
        print("Invalid arguments. Please provide N >=2 numbers and one goal")
        sys.exit(1)

    result = find_goal(numbers, goal, find_all=True)
    print(result)
