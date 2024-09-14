class Node(object):
    def __init__(self,elem):
        self.elem=elem
        self.next=None

class SingleLinkList(object):
    """单链表"""
    def __init__(self,node=None):
        self._head=None

    def is_empty(self):
        return self._head==None

    def length(self):
        cur=self._head
        count=0
        while cur != None:
            cur=cur.next
            count+=1

        return count

    def travel(self):
        cur=self._head
        while cur != None:
            print(cur.elem)
            cur=cur.next

    def add(self,item):
        node=Node(item)
        node.next=self._head
        self._head=node
    

    def append(self,item):
        node=Node(item)
        if self._head==None:
            self._head=node
        else:
            cur=self._head
            while cur.next != None:
                cur =cur.next
            cur.next=node

    def insert(self,pos,item):
        if pos<=0:
            self.add(item)
        elif pos==(self.length-1):
            pre=self._head
            count=0
            while count<(pre-1):
                pre=pre.next
                count +=1
            node=Node(item)
            node.next=pre.next
            pre.next=node
        elif pos>(self.length(pos)-1):
            self.append(item)

    def remove(self,item):
        pre=None
        cur=self._head
        while cur != None:
            if cur.elem==item:
                #先判断此节点是否是头节点
                if cur == self._head:
                    self._head=cur.next
                else:
                    pre.next=cur.next
                break
            else:          
                pre =cur
                cur=cur.next
            


s=SingleLinkList()
print(s.is_empty())


s.append(1)
print(s.is_empty())
s.add(10)
s.add(9)
s.add(8)
s.add(7)
s.remove(7)
s.remove(1)
s.remove(9)
s.travel()