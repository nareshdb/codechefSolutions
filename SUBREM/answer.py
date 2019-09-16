
class Node:
	def __init__(self, key, index):
		self.value = key
		self.children = []
		self.index = index


def addChildNode(root, node): 
    root.children.append(node)

def removeCostlyNodesAndReturnSum(penalty, rootNode):
	sum = rootNode.value
	
	for child in rootNode.children:
		sum += removeCostlyNodesAndReturnSum(penalty, child)
	
	if(sum < -5):
		sum = -5

	return sum


noOfTestCases = input()

for n in range(0, noOfTestCases):
	
	noOfNodes, penaltyForNodeRemoval = map(int, raw_input().split())

	nodeValues = map(int, raw_input().split())

	nodes = []

	for o in range(0, noOfNodes):
		nodes.append(Node(nodeValues[o], o+1))

	for o in range(0, noOfNodes-1):
		rootIndex, childIndex = map(int, raw_input().split())
		addChildNode(nodes[rootIndex-1], nodes[childIndex-1])

	print(removeCostlyNodesAndReturnSum(penaltyForNodeRemoval, nodes[0]))
      