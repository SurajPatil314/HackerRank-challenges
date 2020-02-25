"""
A linked list is said to contain a cycle if any node is visited more than once while traversing the list.

Complete the function provided for you in your editor. It has one parameter: a pointer to a Node object named
 that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a cycle
  in the list. If there is a cycle, return true; otherwise, return false.

Note: If the list is empty,  will be null.
"""

# !/bin/python3

import math
import os
import random
import re
import sys


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    if head == None or head.next == None:
        return False
    else:
        fast = head.next
        slow = head

        while (fast != slow):
            if not fast:
                return False
            if not slow:
                return False
            if not fast.next:
                return False

            fast = fast.next.next
            slow = slow.next

        return True


if __name__ == '__main__':