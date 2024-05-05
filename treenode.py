import os

class TreeNode:
    def __init__(self, name, is_path=True, is_file=False):
        """
        Initializes a tree node.

        Args:
            name (str): The name of the node.
            is_path (bool, optional): Indicates whether the node represents a directory path. Defaults to True.
            is_file (bool, optional): Indicates whether the node represents a file. Defaults to False.
        """
        self.name = name
        self.is_file = is_file
        self.is_path = is_path
        self.children = []

    def add_child(self, child_node):
        """
        Adds a child node to the current node.

        Args:
            child_node (TreeNode): The child node to add.
        """
        self.children.append(child_node)

    def __repr__(self, level=0, last=False):
        """
        Returns a string representation of the tree.

        Args:
            level (int, optional): The level of the node in the tree. Defaults to 0.
            last (bool, optional): Indicates whether the node is the last child of its parent. Defaults to False.

        Returns:
            str: A string representation of the tree.
        """
        ret = ""
        if level > 0:
            ret += "│   " * (level - 1)
            ret += "├── " if not last else "└── "
        if self.is_path:
            ret += self.name + ("/" if not self.is_file else "") + "\n"
        else:
            ret += self.name + "\n"
        for i, child in enumerate(self.children):
            last = i == len(self.children) - 1
            ret += child.__repr__(level + 1, last)
        return ret

    def generate_treepath(self, path):
        """
        Generates a tree structure for the given directory path.

        Args:
            path (str): The directory path.

        Returns:
            TreeNode: The root node of the generated tree structure.
        """
        root = TreeNode(os.path.basename(path))
        if os.path.isdir(path):
            items = os.listdir(path)
            items.sort()
            for i, item in enumerate(items):
                item_path = os.path.join(path, item)
                last = i == len(items) - 1
                root.add_child(self.generate_treepath(item_path))
        else:
            root.is_file = True
        return root

    def find_node(self, name):
        """
        Finds a node with the given name.

        Args:
            name (str): The name of the node to find.

        Returns:
            TreeNode or None: The node if found, otherwise None.
        """
        if self.name == name:
            return self
        for child in self.children:
            found = child.find_node(name)
            if found:
                return found
        return None

    def is_empty(self):
        """
        Checks if the node is empty (has no children).

        Returns:
            bool: True if the node is empty, otherwise False.
        """
        return not self.children

    def get_depth(self):
        """
        Calculates the depth of the tree.

        Returns:
            int: The depth of the tree.
        """
        if not self.children:
            return 1
        return 1 + max(child.get_depth() for child in self.children)

    def get_files(self):
        """
        Retrieves a list of all files in the tree.

        Returns:
            list: A list of file names.
        """
        files = []
        if self.is_file:
            files.append(self.name)
        for child in self.children:
            files.extend(child.get_files())
        return files

    def get_folders(self):
        """
        Retrieves a list of all folders in the tree.

        Returns:
            list: A list of folder names.
        """
        folders = []
        if not self.is_file:
            folders.append(self.name)
        for child in self.children:
            folders.extend(child.get_folders())
        return folders

    def count_files(self):
        """
        Counts the total number of files in the tree.

        Returns:
            int: The total number of files.
        """
        count = 0
        if self.is_file:
            return 1
        for child in self.children:
            count += child.count_files()
        return count

    def count_folders(self):
        """
        Counts the total number of folders in the tree.

        Returns:
            int: The total number of folders.
        """
        count = 1 if not self.is_file else 0
        for child in self.children:
            count += child.count_folders()
        return count


if __name__ == "__main__":
    path = input("Enter the path to the folder: ")
    tree = TreeNode(os.path.basename(path)).generate_treepath(path)
    print(tree)

    node_name = input("Enter the name of the node to search for: ")
    found_node = tree.find_node(node_name)
    if found_node:
        print(f"Node '{node_name}' found: {found_node}")
    else:
        print(f"Node '{node_name}' was not found.")
