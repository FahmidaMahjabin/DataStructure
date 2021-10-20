from BST import BinarySearchTree
import sys
sys.path.insert(1, "D:/Coding/allGitProject/DataStructure/hashTable/classUsingHash")
from humanClass import *
# function = assign age wise human 
# input = humans 
# output = None 
# step1:ekta huamn nibo, human er age k node key hishebe nibo 
# jodi human age ta theke thake tahole node e append korbo 
# na thakle new node create kore assign korbo
class Node:
    def __init__(self, key):
        self.key = key 
        self.value = []
        self.leftChild = None 
        self.rightChild = None
        
