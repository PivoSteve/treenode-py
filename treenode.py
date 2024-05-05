import os

class TreeNode:
    def __init__(self, name, is_path=True, is_file=False):
        self.name = name
        self.is_file = is_file
        self.is_path = is_path
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0, last=False):
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
        if self.name == name:
            return self
        for child in self.children:
            found = child.find_node(name)
            if found:
                return found
        return None

    def is_empty(self):
        return not self.children

    def get_depth(self):
        if not self.children:
            return 1
        return 1 + max(child.get_depth() for child in self.children)

    def get_files(self):
        files = []
        if self.is_file:
            files.append(self.name)
        for child in self.children:
            files.extend(child.get_files())
        return files

    def get_folders(self):
        folders = []
        if not self.is_file:
            folders.append(self.name)
        for child in self.children:
            folders.extend(child.get_folders())
        return folders

    def count_files(self):
        count = 0
        if self.is_file:
            return 1
        for child in self.children:
            count += child.count_files()
        return count

    def count_folders(self):
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