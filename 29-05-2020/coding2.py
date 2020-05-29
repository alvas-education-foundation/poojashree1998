#yatin plays pubg
#Yatin is playing PUBG and he has reached a place with a large staircase in front of him. And there is an enemy at each landing of the staircase.
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def FeedNode(node,val):
    if node is None:
        return TreeNode(val)
    if node.val < val:
        node.right = FeedNode(node.right , val)
    else:
        node.left = FeedNode(node.left, val)
    return node
def Height(node):
    if node is None: 
        return 0 ;  
    else : 
        left = Height(node.left) 
        right = Height(node.right) 
        if (left > right): 
            return left+1
        else: 
            return right+1
testcases = int(input())
for i in range(testcases):
    n = int(input())
    nums = input().split()
    root = TreeNode(int(nums[0]))
    for i in range(1,len(nums)):
        FeedNode(root, int(nums[i]))
    print(str(Height(root))+"\n")
