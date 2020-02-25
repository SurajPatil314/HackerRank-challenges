import java.io. *;
import java.math. *;
import java.security. *;
import java.text. *;
import java.util. *;
import java.util.concurrent. *;
import java.util.regex. *;

public


class Solution {

static


class SinglyLinkedListNode {
public int data;
public SinglyLinkedListNode next;

public SinglyLinkedListNode(int nodeData) {
this.data = nodeData;
this.next = null;
}
}


static


class SinglyLinkedList {
public SinglyLinkedListNode head;
public SinglyLinkedListNode tail;

public SinglyLinkedList() {
this.head = null;
this.tail = null;
}

public void insertNode(int nodeData) {
SinglyLinkedListNode node = new SinglyLinkedListNode(nodeData);

if (this.head == null) {
this.head = node;
} else {
this.tail.next = node;
}

this.tail = node;
}
}


public
static
void
printSinglyLinkedList(SinglyLinkedListNode
node, String
sep, BufferedWriter
bufferedWriter) throws
IOException
{
while (node != null) {
bufferedWriter.write(String.valueOf(node.data));

node = node.next;

if (node != null) {
bufferedWriter.write(sep);
}
}
}

// Complete
the
insertNodeAtPosition
function
below.

/ *
* For
your
reference:
*
*SinglyLinkedListNode
{
*int
data;
*SinglyLinkedListNode
next;
*}
*
* /
static
SinglyLinkedListNode
insertNodeAtPosition(SinglyLinkedListNode
head, int
data, int
position) {

SinglyLinkedListNode
node = new
SinglyLinkedListNode(data);
if (head == null){
return node;
}

int
u = 0;
SinglyLinkedListNode
temp;
SinglyLinkedListNode
temp1;
temp = head;
temp1 = head.next;

if (position == 0)
{
node.next = head;
return node;
}
while (u < position - 1){
temp = temp.next;
u++;
}

temp1 = temp.next;
temp.next = node;
node.next = temp1;

return head;
}

private
static
final
Scanner
scanner = new
Scanner(System. in);