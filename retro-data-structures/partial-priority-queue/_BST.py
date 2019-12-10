class _BST:

    class Node:
        def __init__(self, k, l, r):
            self.key = k
            self.left = l
            self.right = r

    def __init__(self):
        self.root = None

    def insert (self, k):
        self.root = self.PRV_insert(self.root, k)

    def PRV_insert(self, node, k):

        if (node == None):
            return self.Node(k, None, None)
        elif (k < node.key):
            node.left = self.PRV_insert(node.left, k)
        elif (k > node.key):
            node.right = self.PRV_insert(node.right, k)

        return node

    def delete (self, k):
        if (self.root != None):
            self.root = self.PRV_delete(self.root, k)

    def PRV_delete (self, node, k):
        if (node == None):
            return None
        elif (k < node.key):
            node.left = self.PRV_delete(node.left, k)
        elif (k > node.key):
            node.right = self.PRV_delete(node.right, k)
        else:
            if (node.left == None):
                return node.right
            elif (node.right == None):
                return node.left
            else:
                new_node = self.Node(self.PRV_min(node.right), node.left, node.right)
                new_node.right = self.PRV_delete_min(new_node.right)
                node = new_node

        return node

    def contains (self, k):
        self.root = self.PRV_insert(self.root, k)

    def PRV_contains(self, node, k):

        if (node == None):
            return False
        elif (node.key == k):
            return True
        elif (k < node.key):
            return self.PRV_contains(node.left, k)
        elif (k > node.key):
            return self.PRV_contains(node.right, k)

    def min (self):
        if (self.root is None):
            return None
        return self.PRV_min(self.root)

    def PRV_min (self, node):
        if (node.left == None):
            return node.key

        return self.PRV_min(node.left)

    def delete_min (self):
        self.root = self.PRV_delete_min(self.root)

    def PRV_delete_min (self, node):
        if (node.left == None):
            return None

        node.left = self.PRV_delete_min(node.left)
        return node

    def print (self):
        self.PRV_print(self.root)
        print("-------------------")

    def PRV_print (self, node):
        if (node == None): return

        self.PRV_print(node.left)
        print(str(node.key))
        self.PRV_print(node.right)
