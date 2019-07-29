class HashTable:
    def __init__(self, size = 11):
        self.size = size
        self.keyMap = [None] * self.size

    def _hash(self, key):
        total = 0
        length = len(key)
        weirdPrime = 31
        for i in range(min(length, 100)):
            total = total + (ord(key[i]) - 96)
        return (total * weirdPrime) % self.size

    def set(self, key, value):
        index = self._hash(key)
        # Separate Chaining
        if self.keyMap[index]:
            for item in self.keyMap[index]:
                if item[0] == key:
                        return "Key should be unique"
            self.keyMap[index].append([key, value])
        else:
            self.keyMap[index] = [[key, value]]

        return self.keyMap

    def get(self, key):
        index = self._hash(key)
        if self.keyMap[index] == None:
            return "Key-value pair not found"

        if len(self.keyMap[index]) == 1:
            return self.keyMap[index][0][1]

        for item in self.keyMap[index]:
            if item[0] == key:
                return item[1]
        return "Key-value pair not found"

    def keys(self):
        keysArr = []
        for entry in self.keyMap:
            if entry:
                for item in entry:
                    keysArr.append(item[0])

        return keysArr

    def values(self):
        valuesArr = []
        for entry in self.keyMap:
            if entry:
                for item in entry:
                    if item[1] not in valuesArr:
                        valuesArr.append(item[1])

        return valuesArr

hashTable = HashTable()
hashTable.set("pink", "9324530")
hashTable.set("black", "000000")
hashTable.set("blue", "1020398")
# print(hashTable.set("blue", "3344354"))
# print(hashTable.keys())
# print(hashTable.values())
# print(hashTable.keyMap)
# print(hashTable.get("black"))
# print(hashTable.get("yellow"))
# print(hashTable.get("pink"))
