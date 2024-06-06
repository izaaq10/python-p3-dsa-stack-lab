class Stack:

    def __init__(self, items=None, limit=100):
        self.items = items if items is not None else []
        self.limit = limit

    def isEmpty(self):
        return len(self.items) == 0

    def push(self, item):
        if not self.full():
            self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        else:
            return None
  
    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            return None
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) == self.limit

    def search(self, value):
        try:
            index = self.items.index(value)
            return len(self.items) - index - 1
        except ValueError:
            return -1
