class LRUNode(object):
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.prev = None
        self.next = None

