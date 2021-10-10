# human class thakbe jar property set korbo using hash

from hashTable import HashTable
class Human():
    def __init__(self,name, age, jobTitle, salary):
        self.name = name
        self.age = age
        self.jobTitle = jobTitle 
        self.salary = salary
    
import random

# function = getAName 
# output = name 
# step1:a to z ekta list thakbe letters
# step2:letters theke randomly 3 theke 10 ta letter niye name create korte hobe
def createName():
    letters = ["a","b", 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numberOfLetters = random.randint(3,10)
    name = "".join(random.sample(letters, numberOfLetters))
    return name
# 100k human object banate hobe 
# step1:ekta kore 100k ta random name banabo jar letter 3 theke 10 ta hobe 
# step2:ekta kore 100k ta random age banabo (age range 25 to 60)
# step3:ekta kore 100k ta jobTile banabo listOf job theke 
# step4: ekta kore 100k ta salary banabo (range 20000 theke 150000 with a difference of 1000)
# step5:

def createAge():
    age = random.randint(25, 55)
    return age

def createJob():
    listOfJob = ['engineer', 'software engineer', 'banker', 'accountant', 'HR manager']
    job = random.choice(listOfJob)
    return job

def createSalary():
    salary = random.randrange(20000, 100000, 5000)
    return salary

def createHumans(number):
    humans= []
    for human in range(number):
        name = createName()
        age = createAge()  
        jobTitle = createJob()
        salary = createSalary()
        human = Human(name, age, jobTitle, salary)
        humans.append(human)
    return humans

humans = createHumans(10)
# problem1: list of human deya thakbe. tader moddhe jader age 30 tader list return korte hobe
# step1: human list er human age property er value k key hishe and human k value hishebe set korbo
# step2: ekhon key value 30 er jonno j j value i.e human ase ta list akare return korbo

# set key and value 
# step1:listOfHuman theke ekta kore human er age property er value k key hishe and human k value hishe be set korbo

# function = setAgeWiseHuman
    # input = listOfHuman object , hashTable object
    # output = None 
    # step1:listOfHuman theke ekta kore human object nibo
    #     step1.1:hashTable object e setValue te key = human er age , value  = human object hishebe pass korbo
def setAgeWiseHuman(humanTable, listOfHuman):
    for human in listOfHuman:
        humanTable.setValue(human.age,human)
    return
ageTable = HashTable()
# print(setAgeWiseHuman(ageTable, humans))

# function = get ageTable of age 30
# input = human er hashTable , age 
# output = listofhuman  of having age 30
# step1: humanTable e 30 key er value ase kina check korbo
    # step1.1:jodi thake then linkNode of having key 30 pabo
    # step1.2:linkNode er value er name listOfpeoplrOfAge30 te add korbo

def getHumans(humanTable, key):
    LLOfThatKey = humanTable.getNode(key)
    peoples = []
    
    while LLOfThatKey != None:
        if LLOfThatKey.value.age == key:
            peoples.append(LLOfThatKey.value)
        LLOfThatKey = LLOfThatKey.nextPointer                   
    return peoples


# function = get human of age 30 
# input = list of human 
# output = Human 
# step1:list of human theke ekta kore human nibo
#     step1.1:human er age er value 30 kina check korbo 
#     step1.2:if age is 30 then append in new list 
# step2:return newList 
def getHumanWithAge(listOfHuman, age):
    humanWithAge = []
    for human in listOfHuman:
        if human.age == age:
            humanWithAge.append(human)
    return humanWithAge
# print(getHumanWithAge(humans, 30))

jobTable = HashTable()
def setJobWiseHuman(humanTable, listOfHuman):
    for human in listOfHuman:
        humanTable.setValue(human.jobTitle, human)
    return

# print(setJobWiseHuman(jobTable, humans))
def getHumansWithJob(humanTable, jobTitle):
    people = []
    linkedNode = humanTable.getNode(jobTitle)
    while linkedNode != None:
        if linkedNode.value.jobTitle == jobTitle:
            people.append(linkedNode.value)
        linkedNode = linkedNode.nextPointer
    return people
# banker = getHumansWithJob(jobTable, "banker")

    


# function = createNameFromHuman
# input = listOfHuman 
# outPut = listOf Name 
# step1:list of human area theke ekta kore human nibo and human er name property listOfNmae e add korbo 
# step2:return listOfHuman 
def createNameFromHuman(listOfHuman):
    listOfName = []
    for human in listOfHuman:
        listOfName.append(human.name)
    return listOfName

# print(ageTable.listOfNode)
# 1.setAgeWiseHuman(ageTable.listOfNode):
#     1.listOfHuman = ageTable.listOfNode
#     2.listOfHuman = [humanaddress1, ........]
#     3.for human in listOfHuman:
#         3.1:human.setValue(human.age,human):
#             3.1.1:self = human, key = human.age , value = human 
#             3.1.2:self = address1, key = address1.age , value = address1 
        



# print(getHumans(ageTable))

# def getNode(self, key):
#         index = self.getHash(key)
#         if self.listOfNode[index] == None:
#             return None
#         else:
#             if self.listOfNode[index].key == key:
#                 return self.listOfNode[index]
#             else:
#                 elementsWithSameIndex = self.listOfNode[index]
#                 return getNodeForSameIndex(elementsWithSameIndex, key)
# 1.print(getHumans(ageTable)):
#     1.listOfHuman = ageTable
#     1.listOfHuman = addressHashTable1
#     2.if listOfHuman.getNode(30):
#     3.if addressHashTable1.getNode(30):
#         3.1:self = addressHashTable1, key = 30
#         3.2:index = self.getHash(key)
#         3.3:index = addressHashTable1.getHash(30)
    #     3.4:index = 3
    #     3.5:if self.listOfNode[index] == None:
    #     3.6:if addressHashTable1.listOfNode[3] == None 
    #     3.7:if False:
    #     3.8:else:
    #     3.9:if self.listOfNode[index].key == key:
    #     3.10:if addressHashTable1.listOfNode[3].key == key 
    #     3.11:if 30 == 30:
    #     3.12:if True:
    #         3.12.1:return self.listOfNode[index]
    #         3.12.2:return addressHashTable1.listOfNode[3]
    #         3.12.3:return LLofage30
    # 4.if LLofage30 :
    # 5.if True:
    #     5.1:linkedNodeOfkey30 = listOfHuman.getNode(30)
    #     5.2:linkedNodeOfkey30 = ageTable.getNode(30)
    # 5.if linkedNodeOfkey30 != None:
    # 6.if LLofAge50 !=None:
    # 7.if True:
    #     7.1:peoples = []
    #     7.2:for human in linkedNodeOfkey30:
    #     7.3:for human in LLofAge30:
    #         7.3.1:peoples.append(human.name)






# function = getExecutionTime (ekta function er execution time ber korbo)
# input = that function 
# output = execution time 
# step1:start time ber korbo 
# step2:oi function call korbo 
# step3:end time ber korbo 
# step4:time difference return korbo
import time 
from time import process_time

def getExecutionTimeForNaive():
    startTime = process_time()
    getHumanWithAge(humans1k, 30)
    endTime = process_time()
    return endTime - startTime

def getExecutionTimeForHash():
    startTime = process_time()
    getHumans(ageTable, 30)
    endTime = process_time()
    return endTime - startTime
humans1k = createHumans(100000)
setAgeWiseHuman(ageTable, humans1k)
peoplesOfAge30 = getHumans(ageTable, 30)
# print("people having age 30:" ,createNameFromHuman(peoplesOfAge30))
# print("execution time for age 30 people using hashTable:",getExecutionTime(getHumans(ageTable, 30)))
timeForNaive = getExecutionTimeForNaive()
timeForHash = getExecutionTimeForHash()
print("execution time for age 30 people using naive approach:",timeForNaive)
print("execution time for age 30 people using hash approach:", timeForHash)

def timeRatio(time1, time2):
    ratio = time1 / time2 
    return ratio

print("ration of naive to hash function:",timeRatio(timeForNaive,timeForHash ) )
# import timeit
# executionTime = timeit.timeit("getHumans(ageTable, 30)", number = 1, globals = globals())
# print("execution time for age 30 people using hashTable", executionTime)

