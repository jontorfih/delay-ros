MyStack = []
StackSize = 3
def DisplayStack():
 print("Stack currently contains:")
 for Item in MyStack:
  print(Item)
def Push(Value):
 if len(MyStack) < StackSize:
  MyStack.append(Value)
 else:
  print("Stack is full!")
def Pop():
 if len(MyStack) > 0:
  MyStack.pop()
 else:
  print("Stack is empty.")
Push(1)
Push(2)
Push(3)
DisplayStack()
Push(4)
DisplayStack()
Pop()
DisplayStack()
Push(4)
DisplayStack()
Pop()
Pop()
DisplayStack()
Pop()
DisplayStack()