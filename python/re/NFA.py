"""
A simple demo for regular expression re.compile(r'ac+e')
which is implemented by the NFA in the back.
"""
reg_graph = {}
reg_graph[(0, 'a')] = 1
reg_graph[(1, 'c')] = 2
reg_graph[(2, 'c')] = 2
reg_graph[(2, 'e')] = 3
nfa = (0, 3, reg_graph)

def accurate_match(nfa, s):
    def check(current, s):
        if current == end:
            return True
        elif s == '':
            return False
        else:
            next = reg_graph.get((current, s[0]))
            if next:
                return check(next, s[1:])
            else:
                return False

    start, end, reg_graph = nfa
    return check(start, s)

assert accurate_match(nfa, 'ace') is True
assert accurate_match(nfa, 'accccce') is True
assert accurate_match(nfa, 'ac') is False
assert accurate_match(nfa, '') is False
assert accurate_match(nfa, 'safsdfacefasdfsd') is False
