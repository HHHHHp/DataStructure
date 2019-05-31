# -*- coding: UTF-8 -*-
'''
队列:也是一种基本的数据结构，与栈护卫表亲关系，一些列对象组成
    原则：先进先出，元素可以在任何时候可以插入，但只有最前的元素可以出
抽象数据类型(ADT):
    1. Q.enqueue(e): 将元素e查到队列的尾部
    2. Q.dequeue(): 将队列Q中第一个元素移除并返回
    3. Q.first(): 返回队列的第一个元素
    4. Q.is_empty(): 判断队列是否为空

'''


class Empty(Exception):
    pass

class ArrayQueue():
    DEFAULT_CAPACITY = 10
    
    def __init__(self):
        self._data = [None]*ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Empty('A empty Queue')
        return self._data[self._front]
    
    def dequeue(self):
        if self.is_empty():
            raise Empty('A empty Queue')
        answer = self._data[self._front]
        self._front = (self._front + 1)%len(self._data)
        self._size -= 1
        return answer
    
    def enqueue(self,e):
        if self._size == len(self._data):
            self._resize(2*len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
        
    def _resize(self,cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1+walk)%len(old)
        self._front = 0
        