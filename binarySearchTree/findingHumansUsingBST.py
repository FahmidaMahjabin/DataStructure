from BST import BinarySearchTree, Node
import sys
sys.path.append("d:\\Coding\\allGitProject\\DataStructure")
from DataStructure.hashTable.classUsingHash.humanClass import *
# from DataStructure.hashTable.classUsingHash.humanClass import *
print(sys.path)
class HumanNode(Node):
    def __init__(self, key): 
        self.humans = []
        super().__init__(key)
        
        
# human1 = Human("eva", 25, "engineer", 2000)
# eva = HumanNode( human1.age)


class HumanSearchTree(BinarySearchTree):
    """function  = search human
    input =key (it could be agevalue, job title )
    outPut =return node  or False 
    """
    """function = assign human with age 
    input = human age 
    output = none
    step1:human age k key hishebe pathabo and check korbo j oi human ache kina 
    step2:jodi theke thake then oi human k node er humans e append korbo 
    step3:jodi human na thake then age wise human assign korbo 
    """
    def assignHumanWithAge(self, human):
        existingHuman = self.hasValue(human.age)
        if existingHuman:
            existingHuman.humans.append(human)
            
        else:
            self.insertValue(human.age)
            self.assignHumanWithAge(human)
            


class Rectangle:  
    def __init__(self, side):
        self.side = side      

class Triangle(Rectangle):
    def __init__(self,base, largeSide):
        self.base = base
        super().__init__(largeSide)
triA = Triangle(3, 2)
print(triA.side)

