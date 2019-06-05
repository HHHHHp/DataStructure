# -*- coding: UTF-8 -*-
# by Hp

"""
堆是一棵完全二叉树
除了根节点的每个位置p，存储在p中的键值大于或等于存储在p的父节点的键值
导致从root到leaf的路径上键值以递减顺序排列


插入元素时，先考虑构成一棵完全二叉树，先放在最底层的最右侧，最底层满了的话新开一层并放在最左侧
但这样可能会破坏heap-order的属性，因此需要重新调整数以满足heap-order属性。即向上冒泡


移除键值最小的元组
    我们知道键值最小的元组存放在堆T的根节点上，但这样删除将产生两个不相连的子树。
    因此我们移除键值最小元组时将根节点root删除，并用最后一个元素来填充root位置
    但这样也会破坏heap-order属性
    因此删除操作后堆向下冒泡
        向下冒泡的操作：
            1. 如果p没有右孩，令c表示p的左孩
            2. 否则p有两个孩子，令c为较小键值的孩子
            3. 如果kp<=kc则满足heap-order，终止；若kp>kc，则交换两元素
"""


"""
基于数组的堆，由于数组非常适合来存储完全二叉树
可以定义：
如果p是T的根节点： 则 f(p) = 0
如果p是位置q的左孩子： 则f(p) = 2 f(q) + 1
如果p是位置q的右孩子： 则f(p) = 2 f(q) + 2
    这种定义则T的元组都落在[0,n-1] ，有些书中或题目中会从 1开始， 则相应的稍微修改下公式即可


"""

import heapq
import random
ls = []
for i in range(1000):
    ls.append(random.randint(0,100000))
print(ls)

new_ls = heapq.nsmallest(50,ls)
print(new_ls)

"""
heapq模块

heappush(L,e)   # 插入一个元素，并交换使得满足heap-order
heappop(L)      # 删除并返回最小值元素，重新调整
heappushpop(L,e)    # 插入并删除最小元素，如果插入值为最小则返回插入值
heapreplace(L,e)    # 插入并删除最小元素，与上函数区别在于即使插入最小也不会返回
heapify(L)          # 将列表L变成堆，自底向上，O(n)
nlargest(k,iterable)    # 返回可迭代对象中前k大的值     O(n+klogn)
nsmallest(k,iterable)   # 返回可迭代对象中前k小的值     O(n+klogn)  先构件堆，再k次heappop()
"""