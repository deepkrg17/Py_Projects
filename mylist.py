from ctypes import py_object

class MyList:
    def __init__(self):
        self.capacity = 8
        self.size = 0
        self.items = self.__make_array()

    def __make_array(self):
        return (self.capacity*py_object)()

    def __resize(self):
        self.capacity += 8
        temp = self.__make_array()
        for idx in range(self.size):
            temp[idx] = self.items[idx]
        self.items = temp

    def __len__(self): return self.size

    def __str__(self):
        items_str = map(str, self.items[:self.size])
        return f"[{', '.join(items_str)}]"

    def __repr__(self): return self.__str__()

    def __getitem__(self, subs): return self.items[subs]

    def __setitem__(self, idx, item):
        if not 0 <= idx < self.size:
            raise IndexError("list index out of range")
        self.items[idx] = item

    def add(self, item):
        if self.size == self.capacity:
            self.__resize()
        self.items[self.size] = item
        self.size += 1

    def insert(self, pos, item):
        if self.size == self.capacity:
            self.__resize()
        for idx in range(self.size, pos, -1):
            self.items[idx] = self.items[idx - 1]
        self.items[pos] = item
        self.size += 1

    def extend(self, iterable):
        for item in iterable:
            self.add(item)

    def __add__(self, other):
        new = MyList()
        new.extend(self)
        new.extend(other)
        return new

    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.items[self.size]
        raise IndexError("pop from empty list")

    def __delitem__(self, pos):
        if not 0 <= pos < self.size:
            raise IndexError("index out of range")
        for idx in range(pos, self.size - 1):
            self.items[idx] = self.items[idx + 1]
        self.size -= 1

    def remove(self, item):
        del self[self.find(item)]

    def clear(self):
        self.capacity = 8
        self.size = 0
        self.items = self.__make_array()

    def find(self, item):
        for idx in range(self.size):
            if self.items[idx] == item:
                return idx
        raise ValueError(f"{item} is not in list")

    def sort(self):
        for idx, item in enumerate(sorted(self.items)):
            self.items[idx] = item
