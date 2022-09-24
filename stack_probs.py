from collections import deque

def is_parentheses_balanced(brackets):
    
    bracket_map = {')': '(', ']': '[', '}': '{'}
    open_brackets = deque()
    
    for bracket in brackets:
        print(open_brackets)
        if bracket in bracket_map:
            last_open = open_brackets.pop()
            if last_open != bracket_map[bracket]:
                return False
        else:
            open_brackets.append(bracket)
    return len(open_brackets) == 0



print(is_parentheses_balanced('{[]{()}}'))
print(is_parentheses_balanced(r'[{}{}(]'))