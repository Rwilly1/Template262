class HashTable:
    def __init__(self, n):
        ''' Initialize a hashtable of size n '''
        self.size = n
        self.table = [[] for _ in range(n)]  # create empty buckets
    
    def hash(self, item):
        ''' Compute a hash code for item '''
        return hash(item) % self.size  # get index using hash function
    
    def add(self, item):
        ''' Add item to hash table '''
        index = self.hash(item)
        if item not in self.table[index]:
            self.table[index].append(item)  # append if not present
    
    def contains(self, item):
        ''' Check if hashtable contains item '''
        index = self.hash(item)
        return item in self.table[index]  # check existence in bucket
    
    def remove(self, item):
        ''' Remove item from hashtable if it exists '''
        index = self.hash(item)
        if item in self.table[index]:
            self.table[index].remove(item)  # remove if found
    
    def print_hashset(self):
        ''' Print the contents of each bucket in hashtable '''
        for i, bucket in enumerate(self.table):
            print(f'Bucket {i}: {bucket}')  # print each bucket


