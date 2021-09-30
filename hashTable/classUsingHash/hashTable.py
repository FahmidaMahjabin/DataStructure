class LLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.nextPointer = None
class HashTable:
    def __init__(self):
        self.size = 10
        self.listOfNode = [None] * self.size
    
    #function getHash(key k index dibo)
    # input = number
    # output = none
    # step1: object er key k 5 diye divide kore modulus k index hishebe define korbo
    # step4:return index


    def getHash(self, key):
        if type(key) is int:
            index = key % 10
            
        else:
            index = convertStringToInt(key)
        return index

  

    # function = setValue(object er key deya thakbe value set korte hobe)
    # input =an object which has key and value
    # output = None
    # step1:key theke index ber korbo
    # step2:oi index e empty hole index e object boshabo
    # step3:oi index e element thakle, insertValueForSameIndex er jonno value bosthabo

    def setValue(self, key, value):
        index = self.getHash(key)
        newLL = LLNode(key, value)
        if self.listOfNode[index] == None:
            self.listOfNode[index] = newLL

        else:
            valuesForSameIndex = self.listOfNode[index]
            return incertElementForSameIndex(valuesForSameIndex, newLL)

   

    def getValue(self, key):
        getNode = self.getNode(key)
        if getNode != None:
            return getNode.value
        else:
            return None
            
            
            


    
# function = getNode(search a key)
# input = key
# output = True or False
# step1:key theke index ber korbo
# step2:oi index e element na thakle return False
# step3:oi index e element thakle, and key same hole return True
#     step3.1:key same na hole linkedList e key search korbo
    def getNode(self, key):
        index = self.getHash(key)
        if self.listOfNode[index] == None:
            return None
        else:
            if self.listOfNode[index].key == key:
                return self.listOfNode[index]
            else:
                elementsWithSameIndex = self.listOfNode[index]
                return getNodeForSameIndex(elementsWithSameIndex, key)
                
   
# function = getNodes
# input = None
# outPut = all keys
# step1:loop through listOfNode
# step2:if listOfNode is not empty then append the key in a list
#     step2.1:oi index er nextPointer empty na howa porjonto add the key 
# step3:return the list
    def getKeys(self):
        keys = []
        for index in self.listOfNode:
            if index != None:
                keys.append(index.key)
                while index.nextPointer != None:
                    keys.append(index.nextPointer.key)
                    index = index.nextPointer
        return keys

def convertStringToInt(text):
    summation = 0
    for character in text:
        summation += ord(character)
    index = summation % 10
    return index



 # function  = insertValueForSameIndex
    # step1: jodi valueForSameInddex e kono elemnt thake then tar next pointer e check korbo j empty kina
    #     step1.1:empty hole value boshabo 
    # step2:jotokkhon porjonto empty na pabo step1 repeat korbo
    
def incertElementForSameIndex(linkedList,element ):
    while linkedList.nextPointer != None:
        linkedList = linkedList.nextPointer
    linkedList.nextPointer = element
    
def getNodeForSameIndex(linkNode, key):
    while linkNode.key != key:
        linkNode = linkNode.nextPointer
        if linkNode == None:
            return None
    return linkNode

#function = getValueForSameIndex
# input = linkNode that has same Index, key
# outPut = value
# step1:linkNode er key er value and inputKey er value same na howa porjonto:
#         step1.1:linkNode er nextPointer hobe linkNode
#         step1.2:linkNode empty hole return None
# step2:value same hole return that key's value
def getValueForSameIndex(linkNode, key):
    while linkNode.key != key:
        linkNode = linkNode.nextPointer
        if linkNode == None:
            return None
    return linkNode.value       
