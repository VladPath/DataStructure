# marks = [1, 2, 3, 4]

# lst = [True, 'Правда', 1, 1.0]
# lst.append('Hello')
# lst.insert(0, 0)

# l = len(marks)
# print(lst)

# ---------------------------  реализация Односвязных списков
        
                       # создаем класс Node в котором проводим работу с файлами
# class Node:
#     def __init__(self, data, next=None):
#         self.data = data 
#         self.next = next
    
#     def get_data(self):
#         return self.data
    
#     def set_data(self, data):
#         self.data = data
    
#     def get_next_data(self):
#         return self.next
    
#     def set_next_data(self, val):
#         self.next = val
    
    
        # класс ll в котором мы создаем начало и конца связного списка методы 
        # поиска, добавления, удаления и вставки в конец
        # и в начало списка.

# class LinkedList:
#     def __init__(self, data) -> None:
#         print('init')
#         self.head = data
#         self.size = 1
#         self.tail = data

    
#     def get_size(self):
#         return self.size
    
#     def get_head(self):
#         return f'head = {self.head}'
    
#     def get_tail(self):
#         return f'tail = {self.tail}'
    
#     def push_front(self, data):
#         node = Node(data, self.head)
#         self.head = node
        
#         self.size += 1
#         return True
    
#     def push_back(self, data):
#         node = Node(data)
#         self.tail = node.data
#         self.size += 1 
        
#     def remove_node(self, val):
#         prev = None # Предыдущий элемент
#         curr = self.head # нынешний элемент
#         while curr:
#             if curr.get_data() == val:
#                 if prev:
#                     prev.set_next_data(curr.get_next_data())
#                 else:
#                     self.head = curr.get_next_data()
                    
#                 self.size -= 1
#                 return True
            
#             prev = curr
#             curr = curr.get_next_data()
            
#         return False
    
#     def find_node(self, val):
#         curr = self.head
#         while curr:
#             if curr.get_data() == val:
#                 return True
#             else:
#                 curr = curr.get_next_data()
#         return False
    
#     def printLL(self):
#         curr = self.head
#         while curr:
#             print(curr.data)
#             curr = curr.get_next_data()

# first = LinkedList(1)

# first.push_back(2)
# print(first.get_head())
# print(first.get_tail())

# # first.printLL()

# ---------------------------  реализация Односвязных списков

# class Node:

#   def __init__(self,data, next=None, prev=None):
#     self.data = data
#     self.next = next
#     self.prev = prev
  
#   # defining getter and setter for data, next and prev
#   def getData(self):
#     return self.data
  
#   def setData(self, data):
#     self.data = data
  
#   def getNextNode(self):
#     return self.next
  
#   def setNextNode(self, node):
#     self.next = node
    
#   def getPrevNode(self):
#     return self.prev
  
#   def setPrevNode(self, node):
#     self.prev = node

# # class Linked List
# class LinkedList:

#   def __init__(self, head=None):
#     self.head = head
#     self.size = 0

#   def getSize(self):
#     return self.size

#   def addNode(self, data):
#     node = Node(data, None, self.head)
#     self.head = node
#     # incrementing the size of the linked list
#     self.size += 1
#     return True
  
#   # delete a node from linked list
#   def removeNode(self, value):
#     prev = None
#     curr = self.head
#     while curr:
#       if curr.getData() == value:
#         if prev:
#             prev.setNextNode(curr.getNextNode())
#         else:
#             self.head = curr.getNextNode()
#         return True
        
#       prev = curr
#       curr = curr.getNextNode()
        
#     return False
  
#   # find a node in the linked list
#   def findNode(self,value):
#     curr = self.head
#     while curr:
#       if curr.getData() == value:
#         return True
#       else:
#         curr = curr.getNextNode()
#     return False
  
#   # print the linked list
#   def printLL(self):
#     curr = self.head
#     while curr:
#       print(curr.data)
#       curr = curr.getNextNode()

# i = int()

# print(i)


# ----- ----- ----- ----- deque - очередь ----- ----- ----- ----- 

from collections import deque

# dq = deque([])

# dq.appendleft(0)
# dq.append(6)

# vl1 = dq.pop() # генерируют ошибку если его нет
# vl2 =dq.popleft() # генерируют ошибку если его нет

# dq.extend((1, 2, 3))
# dq.extendleft([-1, -2, -3, 3])
# dq.insert(1, 100)
# dq.remove(3)
# dq2 = dq.copy()
# dq2.append(1)
# print(dq2)
# dq.clear()
# print(dq)

# FIFO - первый вошел первый вышел

# dq  = deque()
# dq.appendleft(1)
# dq.appendleft(2)
# dq.appendleft(3)
# v = dq.pop()
# print(v)

# LIFO - Last in first out 

# dq1 = deque()
# dq1.append(1)
# dq1.append(2)
# dq1.append(3)

# v1 = dq1.pop()
# print(v1)


#  ---- ---- ---- ---- Стек (stack) ---- ---- ---- ---- 


# stack = deque([0, 1, 2, 3, 4, 5])
# stack.appendleft(-1)
# stack.appendleft(-2)

# value = stack.popleft()
# print(stack)
# print(value)


#  tree 
# class Node:
#         def __init__(self, data):
#                 self.data = data
#                 self.left = self.right = None

# class Tree:
#         def __init__(self) -> None:
#                 self.root = None
        
#         def __find(self, node, parent, value):
#                 if node is None:
#                         return None, parent, False
                
#                 if value == node.data:
#                         return node, parent, True
                
#                 if value < node.data:
#                         if node.left:
#                                 return self.__find(node.left, node, value)
                        
#                 if value > node.data:
#                         if node.right:
#                                 return self.__find(node.right, node, value )
                
#                 return node, parent, False
                                
                        
        
#         def append(self, obj):
#                 if self.root is None:
#                         self.root = obj
#                         return obj
                
#                 s, p, fl_find = self.__find(self.root, None, obj.data)
                
#                 if not fl_find and s:
#                         if obj.data < s.data:
#                                 s.left = obj
#                         else:
#                                 s.right = obj
#                         return obj
                
#         def show_tree(self, node):
#                 if node is None:
#                         return
                
#                 self.show_tree(node.left)
#                 print(node.data)
#                 self.show_tree(node.right)
        
#         def show_wide_tree(self, node):
#                 if node is None:
#                         return
                
#                 v = [node]
                
#                 while v:
#                         vn = []
#                         for i in v:
#                                 print(i.data, end=' ')
#                                 if i.left:
#                                         vn += [i.left]
#                                 if i.right:
#                                         vn += [i.right]
#                         print()
#                         v = vn
                        
                        
                                

                                         
                
                
                
        
#         def __del_leaf(self, s, p):
#                 if p.left == s:
#                         p.left = None
#                 elif p.right == s:
#                         p.right = None
        
#         def del_one_child(self, s, p):
#                 if p.left == s:
#                         if s.left is None:
#                                 p.left = s.right
#                         if s.right is None:
#                                 p.left = s.left
#                 elif p.right == s:
#                         if s.left is None:
#                                 p.right = s.right
#                         if s.right is None:
#                                 p.right = s.right
                        
                        
#         def find_min(self, node, parent):
#                 if node.left:
#                         return self.find_min(node.left, node)
#                 return node, parent
        
#         def del_node(self, key):
#                 s, p, fl_find = self.__find(self.root, None, key)
#                 if not fl_find:
#                         return None
                
#                 if s.left == None and s.right == None:
#                         self.__del_leaf(s, p)
                        
#                 elif s.left is None or s.right is None:
#                         self.del_one_child(s, p)

#                 else:
#                         sr, pr = self.find_min(s.right, s)
#                         s.data = sr.data
#                         self.del_one_child(sr,pr)
                        
# s = [10, 5, 7, 16, 13, 2, 20]

# a = Tree()

# for i in s:
#         a.append(Node(i))


# a.del_node(5)
# a.show_wide_tree(a.root)
 
 
#   Множества  -  SET  

a = {1, 2, 4, 6}
b = {0, 3, 4, 5}

# разница между set a и set b 

class sets:
        def __init__(self, a, b) -> None:
            self.a = a
            self.b = b
        
        def get_difference(self):
            a = self.a
            b = self.b
            c = {}
            

# a = ['11', '2', '3', '4', '5']

# a = list(map(int, a))

# a.reverse()
# reversed(a)
# print(a)


