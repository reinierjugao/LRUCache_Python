class DoubleLinkedList(object):
    def __init__(self):
	""" 
        " double linked list class contains
        " head pointer and tail pointer
        " Each node contains a next pointer and previous pointer
        " Head node is always the least used item,
        " Tail node is the recently used item
        """
        self.head = None
        self.tail = None

    def addnode(self, cls, key, data):
        """
        " Adds node to end of list. 
        " Use cls to typecast node
        """
        node = cls(key, data)
        self.insertnode(node)
        return node

    def insertnode(self, node):
        """
        " Inserts node at end of list.
        " Use this to avoid recreating the same node if
        " we are just moving it
        """

        node.prev = self.tail
        node.next = None

        # if tail is defined
        if self.tail:
            self.tail.next = node

        # if head is None
        if not self.head:
            self.head = node

        # if tail is None
        if not self.tail:
            self.tail = node

        self.tail = node

    def movetoend(self, node):
        """
        " Moves node to end of list
        """

        self.removenode(node)
        self.insertnode(node)

    def removenode(self, node):
        """
        " Removes node from list.
        " Node can be anywhere in the list
        """

        if node is self.head:
            self.head = node.next
        else:
            if node.prev:
                node.prev.next = node.next

        if node is self.tail:
            self.tail = node.prev
        else:
            if node.next:
                node.next.prev = node.prev

        # clean up node
        node.prev = None
        node.next = None
        

    
