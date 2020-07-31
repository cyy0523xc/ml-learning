'''
二叉树

Author: alex
Created Time: 2020年07月31日 星期五 18时54分34秒
'''
from graphviz import Digraph
from IPython.display import display


class Node:
    """节点"""
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

    def __str__(self):
        val = self.val
        parent = -1 if self.parent is None else self.parent.val
        left = -1 if self.left is None else self.left.val
        right = -1 if self.right is None else self.right.val
        return 'Node: %d, P: %d, L: %d, R: %d' % (val, parent, left, right)


class BinaryTree:
    """二叉树"""
    root = None      # 根节点

    def __init__(self):
        self.root = None

    def insert(self, node):
        """插入节点"""
        if self.root is None:
            # 如果该树为空
            self.root = node
            return self.root
        # 插入节点
        parent = self.root
        while True:
            if node.val > parent.val:
                if parent.right is None:
                    parent.right = node
                    node.parent = parent
                    break
                parent = parent.right
                continue
            if parent.left is None:
                parent.left = node
                node.parent = parent
                break
            parent = parent.left

        return self.root

    def delete(self, node):
        """删除节点"""
        if node is None or self.root is None:
            return None
        print('******', node, '********')
        child = self.delete_root(node)
        print('Child: ', child)
        print('Parent: ', node.parent)
        if child is None and node.parent is None:
            self.root = None
            return node

        if child is None:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
            return node

        if node.parent is None:    # 删除的是根节点
            self.root = child
            self.root.parent = None
            return node

        child.parent = node.parent
        if node.parent.left == node:
            print('-->left')
            child.parent.left = child
            if child.parent.right is not None:
                child.parent.right.parent = child.parent
        else:
            print('-->right')
            child.parent.right = child
            if child.parent.left is not None:
                child.parent.left.parent = child.parent

        print('*Child: ', child)
        print('*Parent: ', child.parent)
        return node

    def delete_root(self, node):
        """删除子树的根节点"""
        if node.left is None and node.right is None:
            return None
        if node.left is None:
            # 左节点为空
            return node.right
        if node.right is None:
            return node.left
        # 左右节点都存在
        if node.right.left is None:
            return node.right
        cur_node = self.min(node.right)
        cur_node.parent.left = cur_node.right
        if cur_node.right is not None:
            cur_node.right.parent = cur_node.parent

        # cur_node放到原来node的位置上
        cur_node.left = node.left
        cur_node.right = node.right
        return cur_node

    def delete_val(self, val):
        """删除某值"""
        node = self.find(val)
        if node is None:
            return None
        return self.delete(node)

    def find(self, val):
        """按值查找节点"""
        node = self.root
        while node.val != val:
            if val < node.val:
                if node.left is None:
                    return None
                node = node.left
            else:
                if node.right is None:
                    return None
                node = node.right
        return node

    def min(self, node=None):
        """获取树的最小值"""
        node = self.root if node is None else node
        while node.left is not None:
            node = node.left
        return node

    def max(self, node=None):
        """获取树的最大值"""
        node = self.root if node is None else node
        while node.right is not None:
            node = node.right
        return node

    def show(self):
        """可视化树"""
        if self.root is None:
            return

        def display_tree(node):
            val = str(node.val)
            dot.node(val, val)
            if node.left is not None:
                if node.left.parent != node:
                    print(node)
                    print(node.left)
                    print(node.left.parent)
                    raise Exception('Error')
                display_tree(node.left)
                dot.edge(val, str(node.left.val))
            if node.right is not None:
                assert node.right.parent == node
                if node.right.parent != node:
                    print(node)
                    print(node.right)
                    print(node.right.parent)
                    raise Exception('Error')
                display_tree(node.right)
                dot.edge(val, str(node.right.val), color='red')

        dot = Digraph(comment='Tree')
        display_tree(self.root)
        display(dot)
        return
