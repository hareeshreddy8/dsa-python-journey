def reversePolishNotation(tokens):
    def calculateOperation(token,operand1,operand2):
        if token == "+":
            return operand1+operand2
        elif token == "-":
            return operand1 - operand2
        elif token == "*":
            return operand1*operand2
        else :
            return int(operand1 / operand2)
    stack = []
    for token in tokens:
        if token.isdigit():
            stack.append(int(token))

        else :
            operand2 = stack.pop()
            operand1 = stack.pop()
            stack.append(int(calculateOperation(token,operand1,operand2)))

    return stack[-1]
