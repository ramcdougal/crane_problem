import random

NUM_SETS = 100
PATTERN_SIZE = 4
reset_freq = 0.000001
colors = ['black', 'lightblue', 'darkblue', 'lightgreen', 'darkgreen', 'purple', 'pink', 'red', 'orange', 'yellow']

num_end_colors = NUM_SETS / len(colors)

def random_set_with_end_color(i):
    my_colors = list(colors)
    my_colors[-1], my_colors[i] = my_colors[i], my_colors[-1]
    a = my_colors[: -1]
    random.shuffle(a)
    return a + [my_colors[-1]]

def patterns_in_set(my_set):
    return [','.join(my_set[j : j + PATTERN_SIZE]) for j in xrange(len(colors) - PATTERN_SIZE)]

def check_for_repeats(sets):
    for i in xrange(NUM_SETS - 1):
        for j in xrange(len(colors) - PATTERN_SIZE):
            pattern = sets[i][j : j + PATTERN_SIZE]
            for k in xrange(i + 1, NUM_SETS):
                repeat = False
                for m in xrange(len(colors) - PATTERN_SIZE):
                    pattern2 = sets[k][m : m + PATTERN_SIZE]
                    if all(p1 == p2 for p1, p2 in zip(pattern, pattern2)):
                        return True
    return False


patterns = []
sets = []
successes = 0
false_hits = 0
while True:
    new_set = random_set_with_end_color(int(len(sets) / num_end_colors))
    new_patterns = patterns_in_set(new_set)
    if all(p not in patterns for p in new_patterns):
        sets.append(new_set)
        patterns += new_patterns
        if len(sets) == NUM_SETS:
            # gratuitous second validation
            if check_for_repeats(sets):
                print 'repeat... algorithm failed'
                false_hits += 1
            else:                
                # success!
                successes += 1
                for i, set in enumerate(sets):
                    print '    Set %d: %r' % (i + 1, set)
                print '    (That is %d successes so far; %d false hits!)' % (successes, false_hits)
                print '---'
                sets = []
                patterns = []
    else:
        if random.random() < reset_freq:
            sets = []
            patterns = []
