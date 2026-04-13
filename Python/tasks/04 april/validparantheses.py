s = ""
stack = []
valid_map = {'}':'{',')':'(',']':'['}
for ch in s:
    if ch in valid_map :
        top_element = stack.pop() if stack else '_'
        if valid_map[ch] != top_element:
            # return False
            pass
        
        else:
            stack.append(ch)

# return not stack