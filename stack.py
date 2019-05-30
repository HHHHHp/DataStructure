"""
栈：栈是由一系列对象组成的一个集合，这些对象的插入删除操作遵循后进先出原则
应用：1. 浏览网页时的后退按键
     2. 计算后缀表达式
     3. 文编编辑器的撤销机制

抽象数据类型(ADT)：
    1. S.push(e)        压栈，将一个元素e添加到栈S的顶部
    2. S.pop(e)         弹栈，从S中移除并返回顶部元素，如果栈为空即报错
    3. S.top()          不移除顶部元素，返回栈顶的元素
    4. S.is_empty()     判断栈是否为空
    5. len(S)           返回栈S中的元素数量

list类的append()   pop()方法和栈的操作非常类似，但列表的接口完全不止于此

"""

class Empty(Exception):
    """
    raise an error when pop an empty stack
    """
    pass

class ArrayStack:
    """
    define a class about the data structure of Stack
    """
    
    def __init__(self):
        self._data = []
        
    def __len__(self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self,e):
        self._data.append(e)
        
    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[-1]
    
    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data.pop()

