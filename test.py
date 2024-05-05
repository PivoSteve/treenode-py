from treenode import TreeNode

tree = TreeNode("name") # << this is your primary node
child = TreeNode("child", slash=False) # << this is your child node, with slash removed
tree.add_child(child) # << here you add a child node to the tree
print(tree)