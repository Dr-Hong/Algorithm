import sys

##스택 사용, 후위 표기식 -> 연산자를 스택에 넣어놓고 그때 그때 pop해서 사용?
n = int(sys.stdin.readline())
postfix = input()   #후위표기식 -> 리스트로 
stack =[]
values = [0] * n

for k in range(n):
    values[k] = int(sys.stdin.readline())
    
for val in postfix:
    if 'A'<=val<='Z':
        stack.append(values[ord(val)-ord('A')])
    elif val == "+":
        right_operand = stack.pop()
        left_operand = stack.pop()
        stack.append(left_operand + right_operand)
    elif val == "-":
        right_operand = stack.pop()
        left_operand = stack.pop()
        stack.append(left_operand - right_operand)
    elif val == '*':
        right_operand = stack.pop()
        left_operand = stack.pop()
        stack.append(left_operand * right_operand)
    elif val == '/':
        right_operand = stack.pop()
        left_operand = stack.pop()
        stack.append(left_operand / right_operand)

