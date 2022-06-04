# Generates all subsets
import sys

def backtrack_compact(working_set, k, n):
    global solutions

    if k == n:
        s = {k for k in working_set if working_set[k] == 1}
        solutions.append(s)
    else:
        k += 1
        for i in [0, 1]:
            working_set[k] = i
            backtrack_compact(working_set, k, n)


def main():
    if 0 < 1 < len(sys.argv):
        n = int(sys.argv[1])
    else:
        exit('Usage: subsets.py number')

    global solutions
    solutions = []

    # backtrack({}, 0, n)
    # print(solutions)

    backtrack_compact({}, 0, n)
    print(solutions)
    print('Number of subsets: {}'.format(len(solutions)))

if __name__ == '__main__':
    main()
