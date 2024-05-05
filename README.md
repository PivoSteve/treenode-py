# TreeNode

TreeNode is a Python class that represents a node in a tree structure, typically used to represent file systems or hierarchical data.

## Usage

To create a tree representing a directory structure, initialize a TreeNode object with the root directory name and use the `generate_treepath` method to generate the tree structure.

To find a specific node in the tree by its name, use the `find_node` method.

You can retrieve various information about the tree, such as the depth, number of files, number of folders, list of files, and list of folders.

## Documentation

### Creating a Tree

To create a tree:

```python
from treenode import TreeNode

tree = TreeNode("name") # << this is your primary node
child = TreeNode("child", slash=False) # << this is your child node, with slash removed
tree.add_child(child) # << here you add a child node to the tree
print(tree)
```

### TreeNode Class

#### Initialization

```py
TreeNode(name, is_path=True, is_file=False)
```
- `name` (str): The name of the node.
- `is_path` (bool, optional): Indicates whether the node represents a directory path. Defaults to True.
- `is_file` (bool, optional): Indicates whether the node represents a file. Defaults to False.
#### Methods

- `add_child(child_node)`: Adds a child node to the current node.
- `generate_treepath(path)`: Generates a tree structure for the given directory path.
- `find_node(name)`: Finds a node with the given name.
- `is_empty()`: Checks if the node is empty (has no children).
- `get_depth()`: Calculates the depth of the tree.
- `get_files()`: Retrieves a list of all files in the tree.
- `get_folders()`: Retrieves a list of all folders in the tree.
- `count_files()`: Counts the total number of files in the tree.
- `count_folders()`: Counts the total number of folders in the tree.