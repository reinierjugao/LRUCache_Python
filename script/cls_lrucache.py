from cls_lrunode import *
from cls_doublelinkedlist import *
from cls_debuglog import *

class LRUCache(DoubleLinkedList):
    def __init__(self, capacity):
        DoubleLinkedList.__init__(self)
        self.keys = dict()
        self.capacity = capacity
        self.count = 0
        self.dbg = debuglog()
        self.dbg.enabled = None
        self.dbg.writelog('Initialized LRUCache')

    def debugstr(self, msg):
        self.dbg.writelog(msg)

    def dumpdlist(self):
        if not self.dbg.enabled:
            return None

        self.debugstr('dumping list')
        node = self.head
        dumpstring = ''
        while node:
            dumpstring = dumpstring + ' [' + str(node.key) + ':' + str(node.data) + ']'
            node = node.next
        self.debugstr('  ListDump:' + dumpstring)
        dumpdict = ''
        for i in self.keys:
            dumpdict = dumpdict + ' [' + str(i) + ':' + str(self.keys[i].data) + ']'
        self.debugstr('  DictDump:' + dumpdict)


    def get(self, key):
        """
        " Gets value of key.
        " If item already exists, remove it from double linked list
        " and move it to tail
        """

        self.debugstr('DEBUG: GET ' + str(key))

        # if self.keys[key] doesn't exist, return error
        if key not in self.keys:
            return "Key does not exist"
        else:
            # get value from self.keys[key]
            node = self.keys[key]

            # Update double linked list and move item to tail
            self.movetoend(node)
            return node.data
    
    def put(self, key, value):
        """
        " If key already exists, remove item from double linked list
        " and move it to tail with the updated value.
        " If key doesn't already exist, check if self.count > capacity.
        "   If count = capacity, remove item at self.head.
        "   Add new item to tail
        " Increment self.count if less than self.capacity
        """

        self.debugstr('DEBUG: PUT ' + str(key) + ' ' + str(value) + ' cnt.' + str(self.count) + ' cap.' + str(self.capacity))

        if key not in self.keys:
            # item not already in list
            self.debugstr('DEBUG: PUT not in keys')
            if self.count == self.capacity:
                # already reached capacity, make room for new item
                self.debugstr('DEBUG: PUT count == capacity')
                hnode = self.head
                # remove head from linked list
                self.removenode(hnode)
                # remove item from hash map
                del self.keys[hnode.key]
            else:
                # still within capacity, increment count
                self.count += 1

            # add item to end of list
            self.debugstr('DEBUG: PUT adding node')
            node = self.addnode(LRUNode, key, value)
            self.keys[key] = node           
        else:
            # item already in list, move to end and update value
            self.debugstr('DEBUG: PUT key in list')
            node = self.keys[key]
            self.movetoend(node)
            node.data = value

"""
obj = LRUCache(2)
for x in range(0,15):
    obj.put(x,x)
    obj.dumpdlist()
    y=x+1
    obj.put(x,y)
    obj.dumpdlist()
    obj.put(x,x)
    obj.dumpdlist()
    print(obj.get(x))
"""
