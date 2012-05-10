
import imp
import sys
import timeit

def time_solution(solution, runs=1):
    timer = timeit.Timer(stmt=solution)
    try:
        runtime = timer.timeit(number=runs)
        return runtime
    except:
        timer.print_exc()

def run_problem(problem_number, runs=1):
    module_name = 'project_euler.problem.p%d' % problem_number
    __import__(module_name)
    module = sys.modules[module_name]

    solutions = module.solutions
    print "%s:" % module.__name__

    for solution in solutions:
        print "--> Running:", solution.__name__
        runtime = time_solution(solution,runs=runs)

        print "    Avg. Runtime: %-0.5e seconds" % runtime
        print "    Runs        : %d" % runs
        print "    Answer      : %s" % module.answer
        print

if __name__ == '__main__':
    run_problem(1, runs=100)
