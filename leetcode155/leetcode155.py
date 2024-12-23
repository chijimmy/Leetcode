class MinStack:
  def __init__(self):
    self.vals = []
    self.mins = []

  def push(self, val: int) -> None:
    self.vals.append(val)
    self.mins.append(min(self.mins[-1] if self.mins else val, val))

  def pop(self) -> None:
    self.mins.pop()
    self.vals.pop()
      
  def top(self) -> int:
    return self.vals[-1]

  def getMin(self) -> int:
    return self.mins[-1]


  # Make MinStack iterable
  def __iter__(self):
    return iter(self.vals)  # Allow iteration over the `vals` list


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
def test_min_stack():
    min_stack = MinStack()

    # Test push and getMin
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    
    assert min_stack.getMin() == -3, "Test Case 1 Failed"
    print (min_stack.getMin())
    min_stack.push(-4)
    print (list(min_stack))
    
    # Test pop and getMin
    min_stack.pop()
    assert min_stack.getMin() == -2, "Test Case 2 Failed"
    
    # Test top
    assert min_stack.top() == 0, "Test Case 3 Failed"
    
    # Test push and getMin again
    min_stack.push(-3)
    assert min_stack.getMin() == -3, "Test Case 4 Failed"
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_min_stack()
