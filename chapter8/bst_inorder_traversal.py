# Searching a binary Search tree is O(log n)
import tree_node
    


 #             3
 #            /  \
 #          2      4
 #         /        \ 
 #        1          5
 
# Setup Default tree     
values = [3,2,4,1,5]
node1 = tree_node.TreeNode(2)
node2 = tree_node.TreeNode(4)
root = tree_node.TreeNode(3, node1, node2)

# Manual Insertion
# node1.left_child = tree_node.TreeNode(1)
# node2.right_child = tree_node.TreeNode(5)

# Insert values into tree (last value is not inclusive)
for index in range(3, len(values)):
    value = values[index]
    node = tree_node.TreeNode(value)
    print(f'Value: {value}')
    root.insert(value)

root.delete(5)
print(f'Row Traversal: {root}')
print(f'InorderTraversal: {root.inorder_traversal()}')


