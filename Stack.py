class Stack():
    def __init__(self):
        self.items=[]
    def push(self,item):
        self.items.append(item)
    def peek(self):
        return self.items[-1]
    def isEmpty(self):
        return self.items==[]
    def pop(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
