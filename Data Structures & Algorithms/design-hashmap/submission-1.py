class MyHashMap:

    def __init__(self):
        self.capacity = 512
        self.buckets = [[] for _ in range(self.capacity)]

    def put(self, key: int, value: int) -> None:
        index = key % self.capacity
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                pair[1] = value
                return
        self.buckets[index].append([key, value])

    def get(self, key: int) -> int:
        index = key % self.capacity
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                return pair[1]
        return -1

    def remove(self, key: int) -> None:
        index = key % self.capacity
        for i, pair in enumerate(self.buckets[index]):
            if pair[0] == key:
                self.buckets[index].pop(i)
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)