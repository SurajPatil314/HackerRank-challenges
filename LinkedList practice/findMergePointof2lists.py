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

    class Solution:
        def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

            d = {}
            while headA:
                d[headA] = 1
                headA = headA.next

            while headB:
                if headB in d:
                    return headB
                headB = headB.next


if __name__ == '__main__':