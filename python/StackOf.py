class StackOf():
  def __init__(self):
    self.items =[]
  def push(self,data):
    self.items.append(data)
  def pop(self):
    return self.items.pop()
  def is_empty(self):
      return self.items ==[]
  def peek(self):
      if not self.is_empty():
        return self.items[-1]
  def getStack(self):
    return self.items
#stackObject = StackOf()
