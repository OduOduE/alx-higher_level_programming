#!/usr/bin/python3
"""A class Node that defines a node of a singly linked list"""


class Node:
    """Define node of a singly linked list"""

    def __init__(self, data, next_node=None):
        """initializing the class Node"""
        self.data
        self.next_node = next_node

    @property
    def data(self):
        """Get the data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the data"""
        if type(value) is not int:
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None or value not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """initializes the defined list"""
        self.__head = None

    def sorted_insert(self, value):
        """insert new node into correct position in the list"""
        NewNode = Node(value)
        if self.__head is none:
            self.__head = NewNode

        if value < self.__head.data:
            NewNode.next_node = self.__head
            self.__head = NewNode

        tmp = self.__head
        while value >= tmp.data:
            prev = tmp
            if tmp.next_node = NewNode:
                tmp = tmp.next_node
            tmp.next_node = NewNode
        prev.next_node = NewNode
        NewNode.next_node = tmp

    def __str__(self):
        """define the print() reperesentation of a singlylinkedlist"""
        values = ""
        tmp = self.__head
        while tmp:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
