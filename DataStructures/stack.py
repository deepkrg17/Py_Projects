from linked_list import Node

class Stack:
    def __init__(self):
        self.top = None

    def isempty(self):
        return self.top is None

    def push(self, value):
        if (top := self.top) is None:
            self.top = Node(value)
        else:
            self.top, self.top.next = Node(value), top

    def pop(self):
        if self.isempty():
            return None
        data, self.top = self.top.value, self.top.next
        return data

    def __str__(self):
        if (curr := self.top) is None: return "[]"
        s = str(curr.value)
        while (curr := curr.next):
            s += f" -> {curr.value}"
        return f"[{s}]"
