import random 
import string

# random solution generates
def random_solution(length=13):
    return [random.choice(string.printable) for _ in range(length)]

# evaluate a solution
def evaluate_sol(solution):
    target = list('HelloxWorld')
    diff = 0
    for i in range(len(target)):
        s = solution[i]
        t = target[i]
        diff += abs(ord(s)-ord(t))
    return diff 

# mutating a solution 
def mutate_sol(solution):
    index = random.randint(0, len(solution)-1)
    solution[index] = random.choice(string.printable)

# hill climbing
def main():
    best = random_solution()
    best_score = evaluate_sol(best)
    while True:
        print('Best score so far', best_score, 'Solution', "".join(best))
        print(best)
        if best_score == 0:
            break
        new_solution = list(best)
        mutate_sol(new_solution)

        score = evaluate_sol(new_solution)
        if score < best_score:
            best_score = score
            best = new_solution

if __name__ == '__main__':
    main()