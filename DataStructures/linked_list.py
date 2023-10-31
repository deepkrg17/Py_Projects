class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self): return f"Node({self.value})"
    def __repr__(self): return self.__str__()

class LinkedList:
    # Not completed yety

    def __init__(self, value=None):
        self.head = Node(value) if value else None
        self.size = 0

    def __len__(self): return self.size

    def insert_head(self, value):
        new = Node(value)
        new.next, self.head = self.head, new
        self.size += 1

    def __str__(self):
        if (curr := self.head) is None: return "[]"
        s = str(curr.value)
        while (curr := curr.next):
            s += f" -> {curr.value}"
        return f"[{s}]"

    def __repr__(self): return self.__str__()

    def add(self, value):
        if (curr := self.head) is None:
            self.head = Node(value)
            return
        while curr.next: curr = curr.next
        curr.next = Node(value)
