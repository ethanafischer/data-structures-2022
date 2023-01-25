from __future__ import annotations

from collections.abc import Callable
from typing import Any, List, Tuple

# An entry in the hash table is a key-value pair
HashEntry = Tuple[Any, Any]
# Each entry in the hash table array will be a list of HashEntry pairs
HashChain = List[HashEntry]


class HashTable:
    """A hash table with separate chaining."""

    def __init__(
            self,
            capacity: int = 10,
            hash_function: Callable[[Any], int] = hash):
        """Creates an empty hash table.

        Args:
            capacity:
                The initial capacity of the backing array.  The default
                capacity is 10.
            hash_function:
                The function to use to compute hash values for the given
                keys.  The default hash function is the Python builtin
                hash function.
        """
        self.table: list[HashChain] = [[] for _ in range(capacity)]

        self.size: int = 0
        self.capacity: int = capacity
        self.hash_function = hash_function


def insert(hash_table: HashTable, key: Any, value: Any) -> None:
    index = (hash_table.hash_function(key)) % hash_table.capacity
    for i in range(len(hash_table.table[index])):
        if hash_table.table[index][i][0] == key:
            hash_table.table[index][i] = key, value
            return

    hash_table.size += 1
    hash_table.table[index].append((key, value))

    if load_factor(hash_table) > 1.0:
        new_hash = [[] for _ in range(hash_table.capacity * 2)]
        for element in hash_table.table:
            for i in element:
                hash_val = hash_table.hash_function(i[0])
                new_hash[hash_val % (hash_table.capacity * 2)].append(i)
        hash_table.table = new_hash
        hash_table.capacity *= 2


def get_item(hash_table: HashTable, key: Any) -> Any:
    index = (hash_table.hash_function(key)) % hash_table.capacity
    for i in range(len(hash_table.table[index])):
        if hash_table.table[index][i][0] == key:
            return hash_table.table[index][i][1]
    raise KeyError


def contains(hash_table: HashTable, key: Any) -> bool:
    index = (hash_table.hash_function(key)) % hash_table.capacity
    for i in range(len(hash_table.table[index])):
        if hash_table.table[index][i][0] == key:
            return True
    return False


def remove(hash_table: HashTable, key: Any) -> tuple[Any, Any]:
    index = (hash_table.hash_function(key)) % hash_table.capacity
    for i in range(len(hash_table.table[index])):
        if hash_table.table[index][i][0] == key:
            hash_table.size -= 1
            return hash_table.table[index].pop(i)
    raise KeyError


def size(hash_table: HashTable) -> int:
    return hash_table.size


def keys(hash_table: HashTable) -> list[Any]:
    key_list = []
    for item in hash_table.table:
        for i in item:
            key_list.append(i[0])
    return key_list


def load_factor(hash_table: HashTable) -> float:
    return float(hash_table.size / hash_table.capacity)


def _contents(hash_table: HashTable) -> list[HashChain]:
    return hash_table.table


"""table = HashTable()
insert(table, 0, "a")
insert(table, 10, "b")
insert(table, 20, "c")
insert(table, 0, "d")
insert(table, 2, "c")
insert(table, 3, "d")
insert(table, 4, "e")
insert(table, 5, "f")
insert(table, 6, "g")
insert(table, 7, "h")
insert(table, 8, "i")
insert(table, 9, "j")
insert(table, 10, "k")
insert(table, 10, "hjk")

print(table.table)
print(get_item(table, 10))
print(keys(table))
print(remove(table, 20))
print(table.table)
"""