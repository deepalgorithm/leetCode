stack = []
min_stack = []

def push(val):
    stack.append(val)
    val = min(val, min_stack[-1] if min_stack else val)
    min_stack.append(val)
    
def pop():
    min_stack.pop()
    stack.pop()

def top():
    return stack[-1]

def getMin():
    return min_stack[-1]

push(-1)
push(0)
push(-1)
print(top())
print(getMin())
pop()
print(top())
print(getMin())
push(-2)
print(top())
print(getMin())
