class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        data = " " * self.get_level() * 3 + "|--" + f"{self.data}"
        print(data)
        # level = 0
        for child in self.children:
            # if level == self.get_level():
                # break
            child.print_tree()

def build_product_tree():
    root = TreeNode("Root Node")
    child = TreeNode("Child Node 1")
    child2 = TreeNode("Child Node 2")

    root.add_child(child)
    root.add_child(child2)
    
    childchild = TreeNode("Child Child")
    child.add_child(childchild)
    root.print_tree()


if __name__ == "__main__":
    build_product_tree()