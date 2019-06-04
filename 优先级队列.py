# -*- coding: UTF-8 -*-
# by Hp

"""
与普通队列不一样
优先级队列是一个包含优先级元素的集合，允许插入任意的元素，并允许删除拥有最高优先级的元素
P.add(key,value)        插入一个拥有键值对的元素，key为优先级，value为元素值
P.min()                 返回一个元组(key,value)，该元组中key值时队列中最小的，
P.remove_min()          移除key值最小的元素
P.is_empty()            判断队列是否为空
len(P)                  返回队列长度

"""

class PriorityQueueBase:
    
    class _Item:
        __slots__ = '_key','_value'
        
        def __init__(self,k,v):
            self._key = k
            self._value = v
            
        def __lt__(self, other):
            return self._key < other._key
    
    def is_empty(self):
        return len(self) == 0