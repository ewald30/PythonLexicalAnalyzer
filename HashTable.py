from Node import Node


class HashTable:
    def __init__(self):
        self.size = 10
        self.buckets = [None] * self.size


    def hash(self, key):
        hashSum = 0

        for idx, c in enumerate(key):
            hashSum += (idx + len(key)) ** ord(c)
            hashSum = hashSum % self.size
        return hashSum


    def insert(self, token, value):
        key = self.hash(token)
        node = self.buckets[key]

        if node is None:
            self.buckets[key] = Node(token, value);
            return key


        offset = 1
        while node.next is not None:
            node = node.next
            offset += 1

        node.next = Node(token, value)
        return offset * self.size + key


    def find(self, token):
        key = self.hash(token)
        node = self.buckets[key]
        offset = 0

        while node is not None :
            if node.symbol == token:
                return offset * self.size + key
            node = node.next
            offset += 1

        return -1


    def get(self, position):
        offset = int(position / self.size)
        key    = position % self.size

        node = self.buckets[key]
        while node is not None:
            if offset == 0:
                return node.symbol
            node = node.next
            offset -= 1

        return -1


    def __str__(self):
        result = '\n/----------------- Symbol Table ---------------/\n'
        for item in self.buckets:
            if item:
                result += str(item) + "\n"
        return result + "/----------------------------------------------/"






