#!/usr/bin/python3
"""Simple module with singly linked list need classes"""


class Node:
    """Simple class with attrs validation.

    Args:
        data (int): Node's data
        next_node (Node): Pointer to next node
    """
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """data: Node's data"""
        return self.__data

    @data.setter
    def data(self, value):
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """next_node: Pointer to next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Class to manage a list of nodes"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Method to insert a node in correct order"""
        new_node = Node(value)

        if self.__head is None:
            self.__head = new_node
        elif self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            curr, prev = self.__head, None
            while curr is not None and curr.data < value:
                prev, curr = curr, curr.next_node
            new_node.next_node = curr
            prev.next_node = new_node

    def __str__(self):
        str_ls = ""
        curr = self.__head
        n = ""
        while curr is not None:
            str_ls += str(curr.data) + n
            n = "\n"
            curr = curr.next_node
        return str_ls
