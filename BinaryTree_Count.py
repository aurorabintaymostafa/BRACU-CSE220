def count_nodes(root):
  if root == None
    return 0
  left_count = count_nodes(root.left)
  right_count = count_nodes(root.right)
  return left_count + right_count + 1

#Count the leaf nodes 
def count_leaf(root):
  if root.left == None and root.right == None:
    return 1
    left_leaf_nodes = count_leaf(root.left)
    right_leaf_nodes = count_leaf(root.right)
    return left_leaf_nodes + right_leaf_nodes
