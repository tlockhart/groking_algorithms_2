# Mneumonic: “Find or Append, Left or Right Again.”
# class TreeNode:
    def __init__(self, value, left=None, right=None ):
        self.value = value
        self.left_child = left
        self.right_child = right
    
    def search(self, search_value, node, values=[]):
        # values = []
        # BASE CASE: If no node or match append (Find or append)
        if not node or search_value == node.value:
            # return node
            # Add node.value to values when search_value found
            values.append(str(node.value))
            return "->".join(values)
        # Recursive Case: If target < node.value, Go left (LT or RT again)
        if search_value < node.value:
            # Add node.value to values when moving left
            values.append(str(node.value))
            return self.search(search_value, node.left_child, values)
        # Recursive Case: If target > node.value, Go right
        elif search_value > node.value:
            # Add node.value to values when moving right
            values.append(str(node.value))
            return self.search(search_value, node.right_child, values)
        