from collections import deque

class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left_child = left
        self.right_child = right

    def search(search_value, node):
        # Base Case: If the node is None or the node.value equals 
        # target, return the node
        if not node or node.value == search_value:
            return node
        
        # Recursive Cases:
        # if search_value < than node.value then go left
        elif search_value < node.value:
            return search(search_value, node.left_child)
        # if search_value > than node.value then go right
        else:
            return search(search_value, node.right_child)
    
    def insert(self, value):
    # Value less than current node value, go to the left.child
        if value < self.value:
            # Recursive Case: if there is not left child add a the value to the left child
            if self.left_child:
                self.left_child.insert(value)
            # Base Case: Insert value to left_child of current node
            else:
                self.left_child = TreeNode(value)
        # Value greater than current node value, go to the right.child 
        elif value > self.value:
            # Base Case: if there is not right child add a the value to the right child
            if self.right_child:
                self.right_child.insert(value)
            # Recursive Case: Insert value to right_child  of current node
            else:
                self.right_child = TreeNode(value)
                
     # If deleted node has two children, go to the right_child
     # then traverse tree of the left_child until you get to a
     # leaf node.  THis will be the successor  
     
     # Note Keep track of the successor nodes parent in order
     # to connect it to the successor node.     
    def replace_with_successor_node(node):
        successor_node = node.right_child
        
        if not successor_node.left_child:
            node.value = successor_node.value
            node.right_child = successor_node.right_child
            return
        # go down left nodes
        while successor_node.left_child:
            parent_of_successor_node = successor_node
            successor_node = successor_node.left_child
        
        # If successor node is the deleted node's right_child, 
        # place the succesor node into the spot where the deleted node
        # was
        if successor_node.right_child:
            parent_of_successor_node.left_child = successor_node.right_child
        # If the succesor has not children, replace it with None
        else:
            parent_of_successor_node.left_child = None
        
        # Plug the successor node into  
        # the spot of the Node we are deleting
        node.value = successor_node.value
        return successor_node
    
    def delete(self, value_to_delete):
        current_node = self
        parent_of_current_node = None
        node_to_delete = None
        
        while current_node:
            if current_node.value == value_to_delete:
                node_to_delete = current_node
                break
            # Move down throuth the tree, 
            # searching for the value as we go
            
            # Note: Keep track of the parent_of_current_node
            # or the node you will be deleting
            parent_of_current_node = current_node
            if value_to_delete < current_node.value:
                current_node = current_node.left_child
            elif value_to_delete > current_node.value:
                current_node = current_node.right_child
                
        # if node to delete not found, it doesn't exist
        if not node_to_delete:
            return None 
        
        # When we find the value to delete replace with successor
        if node_to_delete.left_child and node_to_delete.right_child:
            replace_with_successor_node(node_to_delete)
        # Check if child has 0 or 1 children
        else: 
            # Deleted node child set, to replace the deleted node 
            # with the deleted nodes child
            child_of_deleted_node = (node_to_delete.left_child or node_to_delete.right_child)
            if not parent_of_current_node:
                node_to_delete.value = child_of_deleted_node.value
                node_to_delete.left_child = child_of_deleted_node.left_child
                
                node_to_delete.right_child = child_of_deleted_node.right_child
            # Check if node_to_delete is left or right node
            elif node_to_delete == parent_of_current_node.left_child:
                parent_of_current_node.left_child = child_of_deleted_node
            elif node_to_delete == parent_of_current_node.right_child:
                parent_of_current_node.right_child = child_of_deleted_node
        return node_to_delete
             
            
                  
    def __str__(self):
        # Perform level-order traversal to build a string representation
        return self.level_order_traversal()
    
    # Implement inorder traversal
    def inorder_traversal(self, node=None, values=None):
        if values is None:
            values = []
        if not node: 
            node = self
            
        # if not node:
        #     return 
        # Traverse left subtree
        if node.left_child:
            self.inorder_traversal(node.left_child, values)
        
        #Visit the root
        # print(type(str(node.value)))
        # values.extend(str(node.value))
        values.append(str(node.value))
        
        # Traverse right subtree
        if node.right_child:
            self.inorder_traversal(node.right_child, values)
        # print(values)
        return " -> ".join(values)
        
    # Implement Breadth-First_Search
    def level_order_traversal(self):
        """Returns a string representation of the tree in level-order."""
        # Use a queue for BFS
        queue = deque([self])
        values = []

        while queue:
            # Dequeue the front node
            current = queue.popleft()
            if current:
                # Append current node's value
                values.append(str(current.value))
                # Enqueue left and right children
                if current.left_child:
                    queue.append(current.left_child)
                if current.right_child:
                    queue.append(current.right_child)

        # Join values for output
        return " -> ".join(values)