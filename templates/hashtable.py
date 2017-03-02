#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size"""
        self.buckets = [LinkedList() for i in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table"""
        items = ['{}: {}'.format(repr(k), repr(v)) for k, v in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table"""
        return 'HashTable({})'.format(repr(self.items()))

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored"""
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table"""
        # Collect all keys in each of the buckets

        # O(bl) = O(n)
        all_keys = []  # O(1)
        for bucket in self.buckets:  # b iterations
            for key, value in bucket.items():  # l = n/b iterations
                all_keys.append(key)  # O(1)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table"""
        # TODO: Collect all values in each of the buckets

        #  l = n/b (load factor, avg length of linked list)
        all_values = []  # O(1)
        for bucket in self.buckets:  # O(b)
            for key, value in bucket.items():  # O(l)
                all_values.append(value)  # O(1)
        return all_values
        pass

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table"""
        # Collect all pairs of key-value entries in each of the buckets
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the length of this hash table by traversing its buckets"""
        # TODO: Count number of key-value entries in each of the buckets
        length = 0
        for bucket in self.buckets:
            length += 1
        return length

    def contains(self, key):
        """Return True if this hash table contains the given key, or False"""
        # TODO: Check if the given key exists in a bucket
        for bucket in self.buckets:
            for bucket_key, value in bucket.items():
                if bucket_key == key:
                    return True
        return False
        pass

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError"""
        # TODO: Check if the given key exists and return its associated value
        for bucket in self.buckets:
            for bucket_key, value in bucket.items():
                if bucket_key == key:
                    return value
        raise KeyError('Key not found')
        pass

    def set(self, key, value):
        """Insert or update the given key with its associated value"""
        # TODO: Insert or update the given key-value entry into a bucket
        index = self._bucket_index[key]
        bucket = self.buckets[index]

        tup = bucket.find(lambda tup: tup[0] == key)
        if tup is not None:
            bucket.delete(tup)
        tup = (key, value)
        bucket.append(tup)
        pass

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError"""
        # TODO: Find the given key and delete its entry if found
        pass


def test_hash_table():
    ht = HashTable()
    print(ht)

    print('Setting entries:')
    ht.set('I', 1)
    print(ht)
    ht.set('V', 5)
    print(ht)
    ht.set('X', 10)
    print(ht)
    print('contains(X): ' + str(ht.contains('X')))
    print('get(I): ' + str(ht.get('I')))
    print('get(V): ' + str(ht.get('V')))
    print('get(X): ' + str(ht.get('X')))
    print('length: ' + str(ht.length()))

    # Enable this after implementing delete:
    # print('Deleting entries:')
    # ht.delete('I')
    # print(ht)
    # ht.delete('V')
    # print(ht)
    # ht.delete('X')
    # print(ht)
    # print('contains(X): ' + str(ht.contains('X')))
    # print('length: ' + str(ht.length()))


if __name__ == '__main__':
    test_hash_table()
