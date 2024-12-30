class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    """Insert a value into the BST."""
    if root is None:
        return Node(data)
    else:
        if data < root.data:
            root.left = insert(root.left, data)
        else:
            root.right = insert(root.right, data)
    return root

def inorder_traversal(root):
    """Perform in-order traversal of the BST."""
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

def convert_to_bst(tree, root_key):
    """
    Convert the given tree structure (as a dictionary) to a BST.

    Args:
      tree: Dictionary representing the adjacency list of the tree.
      root_key: Root node key for the tree.

    Returns:
      Root node of the constructed BST.
    """
    root = Node(root_key)  # Create the root node
    nodes_to_process = [root_key]  # Use a list to track nodes to process

    # Process all nodes in the tree structure
    while nodes_to_process:
        current = nodes_to_process.pop()
        for neighbor in tree.get(current, []):
            root = insert(root, neighbor)  # Insert each neighbor into the BST
            nodes_to_process.append(neighbor)  # Add the neighbor for further processing

    return root

# Tree/Graph structure as dictionary
#                                   A
#                                   |
#                    --------------------------
#                   /                          \
#                  B                            C
#            /          \                  /        \
#           D           E                 F          G

tree = {
    "A": ["B", "C"],
    "B": ["D", "E"],
    "C": ["F", "G"],
    "D": [],
    "E": [],
    "F": [],
    "G": []
}

# Example usage
root_node = convert_to_bst(None, "A")
print("Inorder Traversal of the BST:")
inorder_traversal(root_node)