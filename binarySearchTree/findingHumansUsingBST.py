from BST import BinarySearchTree, Node
import sys
sys.path.append("d:\\Coding\\allGitProject\\DataStructure\\hashTable\\classUsingHash")
from humanClass import *
# from DataStructure.hashTable.classUsingHash.humanClass import *
print(sys.path)
class HumanNode(Node):
    def __init__(self, key): 
        self.humans = []
        super().__init__(key)
        
        
human1 = Human("eva", 25, "engineer", 2000)
human2 = Human("Ava", 30, "engineer", 2000)
ageNode = HumanNode( human1.age)
# 1.ageNode = human( human1.age)
# 2.ageNode = human( x123.age)
# 3.ageNode = human( 25):
#     3.1:self = abc, key = 25
#     3.2:self.humans = []
#     3.3:abe.humans = []
#     3.4:super().__init__(key)
#     3.5:super().__init__(25)
#         3.5.1:self = pqr, value = 25
#         3.5.2:self.value = value 
#         3.5.3:pqr.value = 25


print(ageNode.value)


class HumanSearchTree(BinarySearchTree):
    
    """function = assign human with age 
    input = human age 
    output = none
    step1:human age k key hishebe pathabo and check korbo j oi node key ache kina
    step2:jodi theke thake then oi human k node er humans e append korbo 
    step3:jodi human na thake then oi age er value diye humanNode create korbo and node e humans e human append korbo
    """
    def assignHumanWithAge(self, human):
        existingHuman = self.getNode(human.age)
        if existingHuman:
            existingHuman.humans.append(human)
            
        else:
            humanNode = HumanNode(human.age)
            self.insertNode(self.rootNode, humanNode)
            self.assignHumanWithAge(human)
            

humanTree = HumanSearchTree()
print(humanTree.assignHumanWithAge(human1)) 
print(humanTree.assignHumanWithAge(human2))
print("root of humanTree:", humanTree.rootNode.leftChild.value)
# 1.humanTree.assignHumanWithAge(human1)
# 2.x12.assignHumanWithAge(hum12):
#     2.1:self = x12, human = hum12
#     2.2:existingHuman = self.getNode(human.age)
#     2.3:existingHuman = x12.getNode(hum12.age)  
#     2.4: existingHuman = x12.getNode(25)
#         2.4.1:self = x12, value = 25
#         2.4.2:if self.rootNode == None:
#         2.4.3:if x12.rootNode == None 
#         2.4.4:if None == None 
#         2.4.5:return False 
#     2.5:existingHuman = False
#     2.6:else:
#         2.6.1:self.insertValue(human.age)
#         2.6.2:x12.insertValue(25)
#         2.6.3:self = x12, value = 25
#         2.6.4:node = Node(value)
#         2.6.5:node = Node(25)
#         2.6.6:node = 12node
#         2.6.7:self.insertNode(self.rootNode, node)
#         2.6.8:x12.insertNode(x12.rootNode, 12node):
#             2.6.8.1:self = x12, currentNode = None, node = 12node
#             2.6.8.2:if currentNode == None 
#             2.6.8.3:if True:
#                 2.6.8.3.1:self.rootNode = node
#                 2.6.8.3.2:x12.rootNode = 12node





class Rectangle:  
    def __init__(self, side):
        self.side = side      

class Triangle(Rectangle):
    def __init__(self,base, largeSide):
        self.base = base
        super().__init__(largeSide)
triA = Triangle(3, 2)
print(triA.side)

