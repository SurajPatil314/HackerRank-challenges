#!/bin/python3

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


# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def deleteNode(head, position):
    if head == None:
        return head

    temp = head
    temp1 = head
    temp2 = head.next
    i = 0
    if position == 0:
        return temp2

    while (i < position - 1):
        temp = temp.next
        i += 1

    if temp.next != None:
        temp2 = temp.next.next
        temp.next = temp2
    else:
        temp.next = None

    return head


if __name__ == '__main__':