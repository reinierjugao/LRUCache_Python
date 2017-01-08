# LRUCache_Python
LRUCache Implementation in Python

Least Recently Used Cache

Supports the following operations:

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return "Key does not exist".

put(key, value) - Set or insert the value if the key is not already present. When the cache reaches its capacity, it should invalidate the least recently used item before inserting a new item.

Implemented with a dictionary hash map for keys and values and a modified queue structure in the form of a double linked list to keep track of the least recently used.
The queue behaves the same as a normal queue where first in first out with the exception that we can remove a node from anywhere in the queue.

