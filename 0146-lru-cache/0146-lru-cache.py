class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
        
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = dict() #key to node
        self.size = 0
        self.capacity = capacity
        self.head = self.tail = None #linked list
        
    def _add_head(self, node):
        
        """
        2 >< 1 >< 3 >< 5
        """
        if self.head:
            self.head.prev = node
            node.next = self.head
            self.head = node
        else:
            self.head = self.tail = node
        
        return
    
    def _remove_node(self, node):
        
        """ 
        1 >< 5
        3
        """
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
            
        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next
        
        node.prev = node.next = None
        return
    
    def _pop_tail(self):
        """
        1 >< 3
        3
        """
        node = self.tail
        self._remove_node(node)
        return node

    def get(self, key: int) -> int:
        """
        1.exist => remove node, add to head, return val
        2.not exist => return -1
        """
        node = self.cache.get(key, None)
        if node:
            self._remove_node(node)
            self._add_head(node)
            return node.val
        else:
            return -1
            
    def put(self, key: int, value: int) -> None:
        """
        1. exist => update val, remove node, add to head
        2. not exist => create node, add to head, add to cache, size+1
        3. if size > capacity => remove tail, delete cache, size-1
        """
        node = self.cache.get(key, None)
        if node:
            node.val = value
            self._remove_node(node)
            self._add_head(node)
        else:
            node = Node(key, value)
            self._add_head(node)
            self.cache[key] = node
            self.size += 1
            
            if self.size > self.capacity:
                node = self._pop_tail()
                del self.cache[node.key]
                self.size -= 1
                
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)