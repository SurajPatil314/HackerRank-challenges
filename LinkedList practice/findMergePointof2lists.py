"""
Given pointers to the head nodes of  linked lists that merge together at some point, find the Node where the two lists
 merge. It is guaranteed that the two head Nodes will be different, and neither will be NULL.

In the diagram below, the two lists converge at Node x:
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


# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def findMergeNode(head1, head2):
    ans = []
    head11 = head1
    head22 = head2
    while (head1 != head2):
        if head1 == None:
            head1 = head11
        else:
            head1 = head1.next
        if head2 == None:
            head2 = head22
        else:
            head2 = head2.next

    return head1.data


if __name__ == '__main__':