class Node:
    def __init__(self, x):
        self.left = None
        self.right = None
        self.label = x

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getLabel(self):
        return self.label

def preorderPrint(cur_node, preorder):
    if cur_node:
        preorder.append(cur_node.getLabel())
        preorderPrint(cur_node.getLeft(), preorder)
        preorderPrint(cur_node.getRight(), preorder)

def postorderPrint(cur_node, preorder):
    if cur_node:
        preorderPrint(cur_node.getLeft(), preorder)
        preorderPrint(cur_node.getRight(), preorder)
        preorder.append(cur_node.getLabel())

def treeHeight(string):
    count = 0
    for i in string:
        if i == ')':
            count = count + 1
    return count+1


def makeNode0(x):
    root = Node(x)
    return root

def makeNode1(x, t):
    root = makeNode0(x)
    root.setLeft(t)
    return root

def makeNode4(x, t1, t2, t3, t4):
    root = makeNode1(x, t1)
    t1.setRight(t2)
    t2.setRight(t3)
    t3.setRight(t4)
    return root

def B(string, i):
    firstB = Node(None)
    secondB = Node(None)

    if i < len(string):
        if string[i] == '(':
            i += 1
            firstB = B(string, i)
            if firstB != 'FAILED' and string[i] == ')':
                i += 1
                secondB = B(string, i)
                if secondB == 'FAILED':
                    return 'FAILED'
                else:
                    return makeNode4('B',makeNode0('('),firstB,makeNode0(')'),secondB)
            else:
                return 'FAILED'
        else:
            return makeNode1('B',makeNode0('e'))

    if i == len(string):
        return makeNode1('B',makeNode0('e'))

string = input("Enter an input for the parse tree: ")
i = 0
parseTree = B(string,0)

if (parseTree == 'FAILED'):
    exit()

preorder_string = []
preorderPrint(parseTree, preorder_string)
print("Preorder:    " + "".join(preorder_string))
postorder_string = []
postorderPrint(parseTree, postorder_string)
print("Postorder:   " + "".join(postorder_string))
height = treeHeight(postorder_string)
print("Tree Height: " + str(height))