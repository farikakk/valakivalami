def is_valid_brackets(kifejezes):
    verem = []
    
    pairs = {')': '(', '}': '{', ']': '['}
    
    for ch in kifejezes:
        if ch in pairs.values():
            verem.append(ch)
        elif ch in pairs.keys():
            if not verem or verem.pop() != verem[ch]:
                return False
                
    return len(verem) == 0

print(is_valid_brackets("((5+3)*2+1)") == True)
print(is_valid_brackets("{[(3+1)+2]+}") == True)
print(is_valid_brackets("(3+{1-1)}") == False)
print(is_valid_brackets("[1+1]+(2*2)-{3/3}") == True)
print(is_valid_brackets("(({[(((1)-2)+3)-3]/3}-3)") == False)