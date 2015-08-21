import random

NUM_SETS = 100
PATTERN_SIZE = 5

colors = ['black', 'lightblue', 'darkblue', 'lightgreen', 'darkgreen', 'purple', 'pink', 'red', 'orange', 'yellow']

successes = 0
tries = 0
while True:
    tries += 1
    #print 'attempt %d' % tries
    sets = [list(colors) for i in xrange(NUM_SETS)]
    for set in sets:
        random.shuffle(set)
    for i in xrange(NUM_SETS - 1):
        for j in xrange(len(colors) - PATTERN_SIZE):
            pattern = sets[i][j : j + PATTERN_SIZE]
            for k in xrange(i + 1, NUM_SETS):
                repeat = False
                for m in xrange(len(colors) - PATTERN_SIZE):
                    pattern2 = sets[k][m : m + PATTERN_SIZE]
                    if all(p1 == p2 for p1, p2 in zip(pattern, pattern2)):
                        repeat = True
                        #print '    pattern from set %d matched one in set %d' % (i, k)
                        #print '    set %d: %r' % (i, sets[i])
                        #print '    set %d: %r' % (k, sets[k])
                    if repeat:
                        break
                if repeat:
                    break
            if repeat:
                break
        if repeat:
            break
    if not repeat:
        successes += 1
        print 'Found a solution! This one took %d tries to find.' % tries
        for i, set in enumerate(sets):
            print '    Set %d: %r' % (i + 1, set)
        print '    (That is %d successes in %d tries so far!)' % (successes, tries)
        print '---'

