# -*- coding: UTF-8 -*-
# by Hp

# 树的python定义

class Tree:
    class Position:
        def element(self):
            raise NotImplemented('must be implemented by subclass')
        
        def __eq__(self, other):
            raise NotImplemented('must be implemented by subclass')
        
        def __ne__(self, other):
            return not (self == other)
    
    def root(self):
        raise NotImplemented('must be implemented by subclass')
    
    def parent(self,p):
        raise NotImplemented('must be implemented by subclass')
    
    def num_children(self,p):
        raise NotImplemented('must be implemented by subclass')
    
    def children(self,p):
        raise NotImplemented('must be implemented by subclass')
    
    def __len__(self):
        raise NotImplemented('must be implemented by subclass')
    
    def is_root(self,p):
        return self.root() == p
    
    def is_leaf(self,p):
        return self.num_children(p) == 0
    
    def is_empty(self,p):
        return len(self) == 0
    
    def depth(self,p):      # 递归计算树的深度
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent())
        
    def _height(self,p):    # 递归计算树的高度
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height(c) for c in self.children(p))
        
        
# 二叉树
class BinaryTree(Tree):
    def left(self,p):
        raise NotImplemented('must be implemented by subclass')
    
    def right(self,p):
        raise NotImplemented('must be implemented by subclass')
    
    def sibling(self,p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
            
# 二叉树也可以有链式存储结构
# 即每个节点存储值，父指针，左孩指针，右孩指针