import unittest
from cls_lrucache import *

class TestLRUCache(unittest.TestCase):
    def setUp(self):
        self.cache = LRUCache(10)
        self.largecache = LRUCache(902000)

    def test_small_addnodes(self):
        for x in range(0, 900):
            self.cache.put(x,x)
            self.assertEqual(self.cache.get(x), x)        
            
            y = x + 1
            self.cache.put(x,y)
            self.assertEqual(self.cache.get(x), y)

            self.cache.put(x,x)
            self.assertEqual(self.cache.get(x), x)        
  
        for x in range(0, 100):
            self.cache.put(x,x)
            self.assertEqual(self.cache.get(x), x)        

        self.assertEqual(self.cache.get(1), 'Key does not exist')
        self.assertEqual(self.cache.get(90), 90)
        self.assertEqual(self.cache.get(91), 91)
        self.assertEqual(self.cache.get(89), 'Key does not exist')
        
    def test_large_addnodes(self):
        for x in range(0, 902100):
            self.largecache.put(x,x)
            self.assertEqual(self.largecache.get(x), x)
            y = x+10
            self.largecache.put(x,y)
            self.assertEqual(self.largecache.get(x), y)
            self.largecache.put(x,x)
            self.assertEqual(self.largecache.get(x), x)

        self.largecache.put(123, 321)
        self.assertEqual(self.largecache.get(123), 321)


        self.assertEqual(self.largecache.get(124), 124)
        self.assertEqual(self.largecache.get(125), 125)
        self.assertEqual(self.largecache.get(126), 126)
        self.assertEqual(self.largecache.get(127), 127)
        self.assertEqual(self.largecache.get(128), 128)

        self.largecache.put(124, 421)
        self.largecache.put(125, 521)
        self.largecache.put(126, 621)
        self.largecache.put(127, 721)
        self.largecache.put(128, 821)

        self.assertEqual(self.largecache.get(124), 421)
        self.assertEqual(self.largecache.get(125), 521)
        self.assertEqual(self.largecache.get(126), 621)
        self.assertEqual(self.largecache.get(127), 721)
        self.assertEqual(self.largecache.get(128), 821)
        self.assertEqual(self.largecache.get(129), 129)


unittest.main()
