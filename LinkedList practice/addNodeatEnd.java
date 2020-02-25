/*
You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node with
 the given integer. Insert this node at the tail of the linked list and return the head node of the linked list formed
  after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.
*/

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.regex.*;

public class Solution {

    static class SinglyLinkedListNode {
        public int data;
        public SinglyLinkedListNode next;

        public SinglyLinkedListNode(int nodeData) {
            this.data = nodeData;
            this.next = null;
        }
    }

    static class SinglyLinkedList {
        public SinglyLinkedListNode head;

        public SinglyLinkedList() {
            this.head = null;
        }


    }

    public static void printSinglyLinkedList(SinglyLinkedListNode node, String sep, BufferedWriter bufferedWriter) throws IOException {
        while (node != null) {
            bufferedWriter.write(String.valueOf(node.data));

            node = node.next;

            if (node != null) {
                bufferedWriter.write(sep);
            }
        }
    }

    // Complete the insertNodeAtTail function below.

    /*
     * For your reference:
     *
     * SinglyLinkedListNode {
     *     int data;
     *     SinglyLinkedListNode next;
     * }
     *
     */
    static SinglyLinkedListNode insertNodeAtTail(SinglyLinkedListNode head, int data) {
if (head == null) {
     head = new SinglyLinkedListNode(data);
} else {
  SinglyLinkedListNode node = head;
  while (node.next != null) {
        node = node.next;
  }
  node.next = new SinglyLinkedListNode(data);
}
return head;

    }

    private static final Scanner scanner = new Scanner(System.in);