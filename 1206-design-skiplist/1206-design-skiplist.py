import math
import random

"""
P = 0.5

lv head
3  -1------------------>4----------------------->none   1
2  -1------------------>4------------------>8--->none   2
1  -1-------->2-------->4-------->6-------->8--->none   4
0  -1--->1--->2--->3--->4--->5--->6--->7--->8--->none   8
"""

class Node:
    
    def __init__(self, val, lv):
        self.val = val
        self.next = [None]*(lv+1) #node.next[i]: points to next node on the ith level

class Skiplist:

    def __init__(self, N = 20000, P = 0.5):
        self.MAX_LV = math.ceil(math.log2(N))-1
        self.P = P
        self.head = Node(-1, self.MAX_LV) #dummy head for each list
        self.max_lv = 0 #current max level constructed
        self.cnt = 0
        self.n = 90
    
    def _randTopLv(self):
        lv = 0
        while random.random() < self.P and lv < self.MAX_LV:
            lv += 1
        return lv

    def search(self, target: int) -> bool:
        self.cnt += 1
        curr = self.head
        for i in range(self.max_lv, -1, -1):
            while curr.next[i] and curr.next[i].val < target:
                curr = curr.next[i]
        curr = curr.next[0]
        
        """
        print("search {}".format(target))
        print(curr and curr.val == target)
        print(self.n-self.cnt)
        """
        return curr and curr.val == target

    def add(self, num: int) -> None:
        self.cnt += 1
        #1. find the previous node just before the insertion spot for each level
        update = [None]*(self.MAX_LV+1)
        curr = self.head
        for i in range(self.max_lv, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        curr = curr.next[0]
            
        #2. random the topmost level for this node to insert
        top_lv = self._randTopLv()
        if top_lv > self.max_lv: #increases levels
            for i in range(self.max_lv+1, top_lv+1):
                update[i] = self.head
            self.max_lv = top_lv

        #3. create the node with topmost level
        node = Node(num, top_lv)

        #4. insert the node into the proper location for each level
        for i in range(top_lv+1):
            node.next[i] = update[i].next[i]
            update[i].next[i] = node
                
            #print("Successfully inserted num {}".format(num))
        
        """
        print("add {}".format(num))
        self.printList()
        print(self.n-self.cnt)
        """

    def erase(self, num: int) -> bool:
        self.cnt += 1
        update = [None]*(self.MAX_LV+1)
        curr = self.head
        
        for i in range(self.max_lv, -1, -1):
            while curr.next[i] and curr.next[i].val < num:
                curr = curr.next[i]
            update[i] = curr
        curr = curr.next[0]
        
        if curr is None or curr.val != num:
            return False
        
        if curr and curr.val == num:
            for i in range(self.max_lv+1):
                if update[i].next[i] is not curr:
                    break
                update[i].next[i] = curr.next[i]
            
            while self.max_lv > 0 and self.head.next[self.max_lv] is None:
                self.max_lv -= 1
        
        """
        print("erase {}".format(num))
        self.printList()
        print(self.n-self.cnt)
        """
                
        return True
    
    def printList(self):
        for i in range(self.max_lv, -1, -1):
            print("level {}: ".format(i), end="")
            curr = self.head
            while curr:
                print(curr.val, end="")
                curr = curr.next[i]
                print(" -> ", end="")
            print("none")


# Your Skiplist object will be instantiated and called as such:
# obj = Skiplist()
# param_1 = obj.search(target)
# obj.add(num)
# param_3 = obj.erase(num)