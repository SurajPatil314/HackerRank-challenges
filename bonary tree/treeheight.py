"""
The height of a binary tree is the number of edges between the tree's root and its furthest leaf. For example, the following binary tree is of height :

"""


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 


       // this is a node of the tree , which contains info as data, left , right
'''


def sideheight(root1):
    if root1 == None:
        return 0
    else:
        lh = sideheight(root1.left)
        rh = sideheight(root1.right)
        if (lh > rh):
            return lh + 1
        else:
            return rh + 1


def height(root):
    lhight = sideheight(root.right)
    rheight = sideheight(root.left)

    return max(lhight, rheight)

