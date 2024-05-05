import os

class TreeNode:
    def __init__(self, name, is_file=False):
        self.name = name
        self.is_file = is_file
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def __repr__(self, level=0, last=False):
        ret = ""
        if level > 0:
            ret += "│   " * (level - 1)
            ret += "├── " if not last else "└── "
        ret += repr(self.name) + "\n"
        for i, child in enumerate(self.children):
            last = i == len(self.children) - 1
            ret += child.__repr__(level + 1, last)
        return ret

def generate_tree(path):
    root = TreeNode(os.path.basename(path))
    if os.path.isdir(path):
        items = os.listdir(path)
        items.sort()
        for i, item in enumerate(items):
            item_path = os.path.join(path, item)
            last = i == len(items) - 1
            root.add_child(generate_tree(item_path))
    else:
        root.is_file = True
    return root

if __name__ == "__main__":
    path = input("Введите путь до папки: ")
    tree = generate_tree(path)
    print(tree)
