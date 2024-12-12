from collections import deque

stack = deque()

# Push operation
stack.append(10)  # Stack: [10]
stack.append(20)  # Stack: [10, 20]
stack.append(30)  # Stack: [10, 20, 30]
print("Stack after pushes:", stack)

# Pop operation
top = stack.pop()  # Removes 30
print("Popped item:", top)
print("Stack after pop:", stack)

# Peek operation
if stack:
    print("Top item:", stack[-1])

# Check if stack is empty
print("Is stack empty?", len(stack) == 0)
