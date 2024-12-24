#class Solution:
#    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
def validateStackSequences(pushed, popped):
    stack = []
    pop_index = 0
    
    for num in pushed:
        stack.append(num)
        print("stack",stack)
        # Check if the current top of the stack matches the next number to pop
        while stack and stack[-1] == popped[pop_index]:
            print("stack",stack[-1],"popped",popped[pop_index])
            stack.pop()
            print("stack_pop",stack)
            pop_index += 1
            
    return not stack  # If stack is empty, then it's a valid sequence

# Example Usage
pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]
print(validateStackSequences(pushed, popped))  # Output: True

pushed = [1, 2, 3, 4, 5]
popped = [4, 3, 5, 1, 2]
print(validateStackSequences(pushed, popped))  # Output: False
