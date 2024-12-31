import tree_node_with_path
    


 #             3
 #            /  \
 #          2      4
 #         /        \ 
 #        1          5
 
# Setup Default tree     
values = [3,2,4,1,5]
node1 = tree_node_with_path.TreeNode(2)
node2 = tree_node_with_path.TreeNode(4)
root = tree_node_with_path.TreeNode(3, node1, node2)

# Manual Insertion
node1.left_child = tree_node_with_path.TreeNode(1)
node2.right_child = tree_node_with_path.TreeNode(5)

print(root.search(5, root))