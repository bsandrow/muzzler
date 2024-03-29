
import sys
import timeit

problem_namespace = 'muzzler.problem'

class ProblemDoesNotExistError(Exception):
    pass

def time_solution(solution, runs=1):
    timer = timeit.Timer(stmt=solution)
    try:
        runtime = timer.timeit(number=runs)
        return runtime / runs
    except:
        timer.print_exc()

def run_problem(problem_number, runs=1):
    module = load_problem(problem_number)

    solutions = module.solutions
    print "%s:" % module.__name__

    for solution in solutions:
        print "--> Running:", solution.__name__
        runtime = time_solution(solution,runs=runs)

        print "    Avg. Runtime: %-0.5e seconds" % runtime
        print "    Runs        : %d" % runs
        print "    Answer      : %s" % module.answer
        print

def module_args():
    """ Load command-line options.

    Used when module called directly as a script.
    """
    global problem_namespace

    import argparse
    parser = argparse.ArgumentParser(description='muzzler - A Project Euler harness.')
    parser.add_argument('-p','--problem', dest='problems', type=int, action='append', required=True,
                        help='The number of the problem to run solutions for')
    parser.add_argument('-r','--runs', type=int, default=1, help='Number of runs to average runtime over.')
    parser.add_argument('-n','--namespace', help='''The namespace to search for
                        Project Euler problems in. For example, solutions to
                        Project Euler problem #1 would be loaded from
                        \'NAMESPACE.p1\' (default: muzzler.problem)''')

    options = parser.parse_args()
    problem_namespace = options.namespace or problem_namespace

    return options

def load_problem(problem_number):
    try:
        module_name = '%s.p%d' % (problem_namespace, problem_number)
        __import__(module_name)
        module = sys.modules[module_name]
        return module
    except ImportError:
        raise ProblemDoesNotExistError("Could not load module %s: problem %d does not exist" % (module_name, problem_number))

if __name__ == '__main__':
    options = module_args()
    for problem in options.problems:
        try:
            run_problem(problem, runs=options.runs)
        except ProblemDoesNotExistError, e:
            sys.exit("Error: %s" % e.message)

