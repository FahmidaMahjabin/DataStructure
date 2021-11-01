#node and element same
# 1.ekta element er 3 property. value, leftchild, rightchild
# 2.leftchild itself is an element
# 3.so ekta kore leftchild add kora or rightchild add kora mane element create kora.
class Node:
    def __init__(self,value):
        self.value = value
        self.leftChild = None
        self.rightChild = None
        self.parentNode = None

class BinarySearchTree:
    def __init__(self):
        self.rootNode = None

    # function = insert
    # input = value
    # output = insert the value as a node
    #1.value theke ekta node banabo
    #2.oi node ta right place e insert korbo
    def insertValue(self, value):
        node = Node(value)
        self.insertNode(self.rootNode, node)
        
    """function = insert node
    input = rootNode, node
    output = None
    step1:jodi rootNode None hoy then node ta rootNode e assign korbo 
    step2:rootNode None na hole, definde rootNode as current node and currentNode er kothay node insert korte hobe ta ber korbo
        """
    def insertNode(self, currentNode, node):
        if currentNode == None:
            self.rootNode = node 
        else: 
            self.insert(currentNode, node)
    """function = insert
    input = currentNode, node
    step1:compare the rootNode value with the nodeValue:
        step2.1:jodi rootNode er cheye choto hoy:
            step2.1.1:then currentNode hobe rootNode er leftChild 
            step2.1.2:currentChild None hole assign the Node
            step2.1.3:else go to step 1
        step2.2:jodi rootNode er cheye boro hoy:
            step2.2.1:then currentNode hobe rootNode er rightChile
            step2.2.2:currentChildNode hole assign the Node 
            step2.2.3:else go to step 1"""   
        
        
    def insert(self, currentNode, node):
        if currentNode.value > node.value:
            if currentNode.leftChild == None:
                currentNode.leftChild = node
                return
            else:
                self.insert(currentNode.leftChild, node)
        else:
            if currentNode.rightChild == None:
                currentNode.rightChild = node
                return
            else:
                self.insert(currentNode.rightChild, node)


    #     2.if rootNode value == value:
    #         1.return rootNode
    #     3.elif rootNode.value > value:
    #         1.rootNode = rootNode.leftChild
    #         2.if rootNode == None:
    #             return False
    #         3.else:
    #             go to step 1
    #     4.elif rootNode.value < value:
    #         1.rootNode = rootNode.rightChild
    #         2.if rootNode == None:
    #             return False
    #         3.else:
    #             go to step 1
    # 1.value khujte node keno banano lagse

    #     function = getNode
    #     input = value
    #     output = return node if it is found, else False if not found
    #   1.rootNode empty kina check korbo , jodi empty hoy then return False
    #     2.else rootNode er value er sathe input value same kina check korbo 
        # 2.same hole return rootNode 
        # 3.else searchNode call korbo
    def getNode(self, value):
        if self.rootNode == None:
            return False
        elif self.rootNode.value == value:
            return self.rootNode
        else:
            return self.searchNode(self.rootNode, value)
    
       

    
    """function = searchNode
    input = currentNode, value
    output = return the node if found , else False
    1.if currentNode er value node er value same hoy:
        1.then return current node
    2.if currentNode er value > node er value
        1.return function searchInLeft where currentNode = currentNode's leftChild
        
    3.else currentNode er value < value 
        1.return function searchInRight where currentNode = currentNode's rightChild"""

    

    def searchNode(self,currentNode, value):
        if currentNode.value == value:
            return currentNode
        elif currentNode.value > value:
            currentNode = currentNode.leftChild
            return self.searchInDescendents(currentNode, value)
        else:
            currentNode = currentNode.rightChild 
            return self.searchInDescendents(currentNode, value)

    # function = searchInLeft 
    # input = currentNode, value 
    # outPut = node else False 
    # step1: jodi currentNode None hoy return False 
    # step2:jodi None na hoy then return the searchNode
    def searchInDescendents(self, currentNode, value):
        if currentNode == None:
            return None
        else: 
            return self.searchNode(currentNode, value)
        


    # function = searchInRight 
    # input = currentNode, value 
    # outPut = node else False 
    # step1: jodi currentNode None hoy return False 
    # step2:jodi None na hoy then return the searchNode


    """function = find parent of a node
    input = currentNode, node
    output = None
    step1:if currentNode.leftChild or currentNode.rightchild is node then assign node.parentNode = currentNode
    step2:elif currentNode.value > node.value then assign currentNode = currentNode.leftChild then return the function again
    step3:elif currentNode.value < node.value then assign currentNode = currentNode.rightChild then return the function again"""
    
    def assignParentOfaNode(self, currentNode, node):
        if currentNode.leftChild == node or currentNode.rightChild == node:
            node.parentNode = currentNode
        elif currentNode.value > node.value:
            self.assignParentOfaNode(currentNode.leftChild, node)
        else:
            self.assignParentOfaNode(currentNode.rightChild, node)
            

    """function = findoutWhichChild
    inout = parentNode, childNode
    output = None
    1.if perentNode.value > childNode.value then 
        parentNode.leftChild = childNode
    2.else:
        parentNode.rightChild = childNode"""

    def assigningChildToaParent(self, parentNode, childNode):
        if parentNode.value > childNode.value:
            parentNode.leftChild = childNode
        else:
            parentNode.rightChild = childNode

    """function = remove node from parent
    input = parent,node
    step1:if node is leftChild of the parent then assign parent.leftChild = None
    step2:else assign parent.rightchild = None"""
    def removeNodeFromParent(self, parent, node):
        if parent.leftChild == node:
            parent.leftChild = None
        else:
            parent.rightChild = None
        

#     delete node means oi node object ta parent node theke delete hoye jabe.  
#     to delete a node means remove the address of the node from it's parent node
#     function = delete
#     input = value
#     output = None 
#     step1: find out the node using getNode function
#     step2:if the node has no leftChild and no rightChild then parentNode er ei child er jaygay None assign korbo
#     step3:if the node has a leftChild and rightChild None then assign leftChild to the node
#     step4:if the node has rightChild and leftChild None the assign the rightChild to the node
#     step5:if the node has both leftChild and rightChild then 
#         1.get the left Child's rightmost child as ChildNode
#         2.assign the childNode to the node position  

# 100 er parent e 70 

    
    def deleteNode(self, value):
        node = self.getNode(value)
        if node.leftChild == None and node.rightChild == None:
            return self.removeNodeFromParent(node.parentNode, node)
              
        elif node.rightChild == None:
            return self.assigningChildToaParent(node.parentNode, node.leftChild)
        elif node.leftChild == None:
            return self.assigningChildToaParent(node.parentNode, node.rightChild)
        else:
            childNode = self.findImmediateSmallerNode(node) 
            return self.assigningChildToaParent(node.parentNode, childNode)
        
#     def findImmediateSmallerNode(self, currentNode):"""
        
    """function = find right most child
    input = currentNode
    output = rightmost node
    1.if currentnode.rightChild == None:
        return currentNode
    2.else:
        currentNode = currentNode.rightChild
        return function again"""
    def findRightMostNode(self,currentNode):
        if currentNode.rightChild == None:
            return currentNode
        else:
            return self.findRightMostNode(currentNode.rightChild)
    
    """function = findImmediateSmallerNode
    input = currentNode
    output = return immediate smaller node
    1.if currentNode.leftChild == None:
        return currentNode
    2.else:
        currentNode = currentNode.leftChild
        return findRightMostNode(self,currentNode)"""
    def findImmediateSmallerNode(self, currentNode):
        if currentNode.leftChild == None:
            return currentNode
        else:
            currentNode = currentNode.leftChild
            return self.findRightMostNode(currentNode)  
    
    
    """function = printInorderTree
    leftsubtree- root- rightsubTree
    input = rootNode
    output =None
    step1:if node jodi empty hoy then return nothing
    step2:else go to the left node and do step1 
        step2.1:print(node.value + " ")
        step2.2:go to step1 where root is egual to rightChild"""
    def printInorderTree(self, node):
        if node == None:
            return
        self.printInorderTree(node.leftChild)
        print( node.value)
        self.printInorderTree(node.rightChild)
    

    
#     tree1.printInorderTree(node30):
#         1.self = tree1, node = node30
#         2.if node == None
#         3.if node30 == None
#         4.if False
#         5.self.printInorderTree(node.leftChild)
#         6.tree1.printInorderTree(node30.leftChild)
#             1.self = tree1, node = None
#             2.if node == None
#             3.if None == None
#             4.if True
#                 1.return
#         7. 
#         8.print(node.value , end = " ")
#         9.print(node30.val, end = " ")
#         10.print(30 )
#         11.self.printInorderTree(node.rightChild)
#         12.tree1.printInorderTree(node30.rightChild)
#         13.self = tree1, node = node30.rightChild
#             1.if node == None
#             2.if node30.rightChild == None
#             3.if node100 == None
#             4.if False
#             5.self.printInorderTree(node.leftChild)
#             6.tree1.printInorderTree(node100.leftChild):
#                 1.self = tree1, node = node100.leftChild 
#                 2.if node == None
#                 3.if node100.leftChild == None
#                 4.if node60 == none
#                 5.if False
#                 6.self.printInorderTree(node.leftChild)
#                 7.tree1.printInorderTree(node60.leftChild)
#                     1.self = tree1, node = node60.leftChild
#                     2.if node == None
#                     3.if node60.leftChild == None
#                     4.if None == None
#                     5.if True
#                         1.return 
                    
#                 8.return
#                 9.print(node.value, end = " ")
#                 10.print(node60.value, end = " ")
#                 11.print(60 )
#                 12.self.printInorderTree(node.rightChild)
#                 13.tree1.printInorderTree(node60.rightChild):
#                     1.self = tree1, node = node60.rightChild
#                     2.if node == None
#                     3.if node60.rightChild == None
#                     4.if None == None:
#                         1.return
#                 14.return 
#                 15.
            
                
        
    """function = printPreOrderTree
    input = node
    output = node valu in pre order (left- root-right)
    step1:if node is empty then return nothing
    step2:else
        step2:print node value
        step3:call printPreOrderTree where node = node.leftChild
        step4:call printPreOrderTree where node = node.rightChild"""

    def printPreOrderTree(self, node):
        if node == None:
            return 
        else:
            print(node.value )
            self.printPreOrderTree(node.leftChild)
            self.printPreOrderTree(node.rightChild)

    """function = print post order tree(right-left-root)
    input = rootNode
    output = tree values
    step1:jodi node empty hoy then ber hoye ashbo
    step2:else: node hobe noder left child and go to step1 
        step2.1:node hobe node er rightChild and go to step1 
        step2.2:print node value """
    def printPostOrder(self, node):
        if node == None:
            return 
        else:
            self.printPostOrder(node.leftChild)
            self.printPostOrder(node.rightChild)
            print(node.value)

    
    """function = getParentandNode
    input = value
    output = parent, node
    step1:IF rootNode HAS The same value as value then return parent = None, node = rootNode
    step2: searchNode = Node(value)
    step2:else return getParenrtfromAnchestor(rootNode, searchNode)"""
    
    
    def getParentandNode(self, value):
        if self.rootNode.value == value:
            return None, self.rootNode
        else:
            return self.getParentandNodefromAncestor(self.rootNode, value)
            
    """function = getParentfromAnchestor(ancestor, searchValue)
    input = ancestor, searchValue
    output = parent, node
    step1: if ancestor.leftChild and rightChild is not None then,
        1.:if ancestor.leftChild has same value as searchvalue, then return parent = ancestor , node = ancestor.leftChild
        2.:if ancestor.rightChild has same value as searchValue return ancestor, ancestor.rightChild
    step2:if ancestor's value is greater than the searchvalue ,
        1.if ancestor.leftChild is none then return parent = none, node = none
        2.else return getParentfromAncestor(ancestor.leftChild, searchValue)
        
    step3:if ancestor's value is less than the searchvalue ,
        1.if ancestor.rightChild is none then return parent = none, node = none
        2.else return getParentfromAncestor(ancestor.rightChild, searchValue)"""
            
    def getParentandNodefromAncestor(self, ancestor, searchValue):
        if ancestor.leftChild is not None:
            if ancestor.leftChild.value == searchValue:
                return ancestor,ancestor.leftChild
        if ancestor.rightChild is not None:
            if ancestor.rightChild.value == searchValue:
                return ancestor,ancestor.rightChild
        
        elif ancestor.value > searchValue:
            if ancestor.leftChild is None:
                return None, None
            else:
                return self.getParentandNodefromAncestor(ancestor.leftChild, searchValue)
        elif ancestor.value < searchValue:
            if ancestor.rightChild is None:
                return None, None
            else:
                return self.getParentandNodefromAncestor(ancestor.rightChild, searchValue)
if __name__ == "__main__":
    age = BinarySearchTree()
    age.insertValue(15)
    # evaluation of age.insertValue(15)
    # 1.xyz.insertValue(15):
    #     self = xyz, value = 15
    #     1.node = Node(value)
    #     2.node = nodex
    #     3.self.insertNode(self.rootNode, node):
    #         3.1:xyz.inserNode(xyz.rootNode, nodex):
    #             3.1.1 self = xyz, currentNode = xyz.rootNode = None, node = nodex
    #             3.1:2 if currentNode == None:
    #             3.1.3:if None == None:
    #             3.1.4: if True 
    #             3.1.5: self.rootNode = node
    #             3.1.6: xyz.rootNode = nodex
    age.insertValue(10)
    age.insertValue(50)
    age.getNode(50)
    print(age.getNode(50))

    print(age.rootNode.rightChild.value)
    age.printInorderTree(age.rootNode)

    age.printPreOrderTree(age.rootNode)
    age.printPostOrder(age.rootNode)