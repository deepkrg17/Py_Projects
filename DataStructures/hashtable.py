class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self): return f"Node({self.key}, {self.value})"

class Bucket:
    def __init__(self):
        self.head = None

    def find_node(self, key):
        """
        Returns
        -------
        tuple(res, node)
            - res : str -- search result (empty|found|not_found)
            - node : Node 
                res == "empty"  => head (None)
                res == "found"  => node with given key
                res == "not_found"  => tail
        """
        if (curr := self.head) is None:
            return ("empty", curr)
        while curr.next is not None:
            if curr.key == key:
                return ("found", curr)
            curr = curr.next
        if curr.key == key: return ("found", curr)
        return ("not_found", curr)

    def __getitem__(self, key):
        res, node = self.find_node(key)
        if res == "found":
            return node.value
        raise KeyError(key)

    def __setitem__(self, key, value):
        res, node = self.find_node(key)
        match(res):
            case "empty": self.head = Node(key, value)
            case "found": node.value = value
            case "not_found": node.next = Node(key, value)

    def __delitem__(self, key):
        if (curr := self.head):
            if curr.key == key:
                self.head = curr.next
                return
            while curr and curr.next:
                if curr.next.key == key:
                    curr.next = curr.next.next
                    return
                curr = curr.next
        raise KeyError(key)

class Dictionary:
    def __init__(self, capacity=8):
        self.__capacity = capacity
        self.buckets = self.__make_buckets()
        self.__keys = set()

    @property
    def size(self):
        return len(self.__keys)

    def keys(self): return self.__keys

    def __make_buckets(self):
        return [Bucket() for _ in range(self.__capacity)]

    def __rehash(self):
        self.__capacity += 4
        old_bckts = self.buckets
        self.buckets = self.__make_buckets()

        for bucket in old_bckts:
            node = bucket.head
            while node:
                self[node.key] = node.value
                node = node.next

    def __get_bucket_idx(self, key):
        return abs(hash(key)) % self.__capacity

    def __getitem__(self, key):
        bucket_idx = self.__get_bucket_idx(key)
        return self.buckets[bucket_idx][key]

    def __setitem__(self, key, value):
        bucket_idx = self.__get_bucket_idx(key)
        self.buckets[bucket_idx][key] = value
        self.__keys.add(key)

        if (self.size / self.__capacity) >= 2:
            self.__rehash()

    def __delitem__(self, key):
        bucket_idx = self.__get_bucket_idx(key)
        del self.buckets[bucket_idx][key]
        self.__keys.remove(key)

    def __contains__(self, key): return key in self.__keys

    def __iter__(self): return iter(self.__keys)

    def __str__(self):
        return ', '.join([f"{key}: {self[key]}" for key in self.__keys])

# am start --user 0 -n com.duolingo/com.duolingo.app.StreakSocietyLauncher
