import math
def dataset_split(data, arc, val):
    newData = []
    for rec in data:
        if rec[arc]==val:
            reducedSet=list(rec[:arc]) 
            reducedSet.extend(rec[arc+1:])
            newData.append(reducedSet)
    return newData

def calc_entropy(data):
    entries=len(data)
    labels={}
    for rec in data:
        label=rec[-1]
        if label not in labels.keys():
            labels[label]=0
        labels[label] += 1
    entropy=0.0

    for key in labels:
        prob= float(labels[key])/entries
        entropy-=prob*math.log(prob,2)
    return entropy

def attribute_selection(data): 
    features=len(data[0])-1
    baseEntropy=calc_entropy(data)
    max_InfoGain=0.0
    bestAttr=-1

    for i in range(features):
        AttrList = [rec[i] for rec in data]
        uniqueVals=set(AttrList)
        newEntropy=0.0
        attrEntropy=0.0
    for value in uniqueVals:
        newData=dataset_split(data, i, value)
        prob= len(newData)/float(len(data))
        newEntropy=prob*calc_entropy(newData) 
        attrEntropy+=newEntropy


    infoGain=baseEntropy - attrEntropy 
    if infoGain> max_InfoGain: 
        max_InfoGain=infoGain
        bestAttr = i
    return bestAttr

def decision_tree(data, labels):
    classList = [rec[-1] for rec in data]
    if classList.count(classList[0])== len(classList):
        return classList[0]

    maxGainNode = attribute_selection(data) 
    treeLabel = labels[maxGainNode]
    theTree={treeLabel: {}} 
    del(labels[maxGainNode])
    nodeValues=[rec[maxGainNode]for rec in data]
    uniqueVals=set(nodeValues)
    for value in uniqueVals:
        sublabels = labels[:]
        theTree[treeLabel][value] = decision_tree(dataset_split(data, maxGainNode, value), sublabels)
        return theTree

def print_tree(tree, level): 
    if tree=='yes' or tree=='no':
        print(''*level, 'd=', tree) 
        return 
    for key,value in tree.items():
        print(''*level, key)
        print_tree(value, level*2)

with open('tennis.csv', 'r') as csvfile:
    fdata=[line.strip() for line in csvfile] 
    metadata=fdata[0].split(',')
    train_data=[x.split(',') for x in fdata[1:]]

tree=decision_tree(train_data, metadata) 
print_tree(tree, 1) 
print(tree)
