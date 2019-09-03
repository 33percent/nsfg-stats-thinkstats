# all my imports
import descriptive

def ProbRange(pmf, low, high):
    total = 0.0
    for week in range(low, high+1):
        total += pmf.Prob(week)
    return total

def ProbEarly(pmf):
    return ProbRange(pmf, 0, 37)
def ProbOnTime(pmf):
    return ProbRange(pmf, 38, 40)
def ProbLate(pmf):
    return ProbRange(pmf, 41, 50)
def ComputeRelativeRisk(first_pmf, other_pmf):
    funcs = [ProbEarly, ProbOnTime, ProbLate]
    risks = {}
    for func in funcs:
        for pmf in [first_pmf, other_pmf]:
            prob = func(pmf)
            risks[func.__name__, pmf.name] = prob
            print( func.__name__, pmf.name, prob)
    print( 'Risk ratios (first babies / others):')
    for func in funcs:
        try:
            ratio = (risks[func.__name__, 'first babies'] / 
                     risks[func.__name__, 'others'])
            print( func.__name__, ratio)
        except ZeroDivisionError:
            pass            


def main():
    pool, firsts, others = descriptive.MakeTables()
    ComputeRelativeRisk(firsts.pmf, others.pmf)

if __name__ == "__main__":
    main()