class MyHashMap:

    def __init__(self):
        self.size = 10000
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        k = key % self.size
        for i in range(len(self.map[k])):
            if self.map[k][i][0] == key:
                self.map[k][i][1] = value
                break
        else:
            self.map[k].append([key, value])

    def get(self, key: int) -> int:
        k = key % self.size
        for i in range(len(self.map[k])):
            if self.map[k][i][0] == key:
                return self.map[k][i][1]
        return -1
        
    def remove(self, key: int) -> None:
        k = key % self.size
        for i in range(len(self.map[k])):
            if self.map[k][i][0] == key:
                self.map[k].pop(i)
                break