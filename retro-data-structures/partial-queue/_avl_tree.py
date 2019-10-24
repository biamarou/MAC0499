class AVL(object):

    class Node(object):
        def __init__(self, re):
            self.ref = re
            self.left = None
            self.right = None
            self.height = 0

    def __init__(self):
        self.root = None

    def height (self):
        return self._height(self.root)

    def _height (self, node):
        if (not node): return 0
        return node.height

    def insert (self, re):
        if (self.root is None):
            self.root = self.Node(re)
        else:
            self.root = self._insert(self.root, re)

    def _insert(self, node, re):
        if (node is None):
            return self.Node(re)
        elif (re.time < node.ref.time):
            node.left = self._insert(node.left, re)
        else:
            node.right = self._insert(node.right, re)

        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))
        return self._balance(node)

    def _balance_factor (self, node):
        return self._height(node.left) - self._height(node.right)

    def _balance (self, node):
        if (self._balance_factor(node) < -1):
            if (self._balance_factor(node.right) > 0):
                node.right = self._rotate_right(node.right)

            node = self._rotate_left(node)

        elif (self._balance_factor(node) > 1):
            if (self._balance_factor(node.left) < 0):
                node.left = self._rotate_left(node.left)

            node = self._rotate_right(node)

        return node

    def _rotate_left (self, node):
        node_tmp = node.right
        node.right = node_tmp.left
        node_tmp.left = node
        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))
        node_tmp.height = 1 + max(self._height(node_tmp.left),
                                  self._height(node_tmp.right))

        return node_tmp

    def _rotate_right (self, node):
        node_tmp = node.left
        node.left = node_tmp.right
        node_tmp.right = node
        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))
        node_tmp.height = 1 + max(self._height(node_tmp.left),
                                  self._height(node_tmp.right))

        return node_tmp

    def delete (self, t):
        if (self.root is not None):
            self.root = self._delete(self.root, t)

    def _delete (self, node, t):

        if (node is None): return node

        if (t < node.ref.time):
            node.left = self._delete(node.left, t)

        elif (t > node.ref.time):
            node.right = self._delete(node.right, t)

        else:
            if (node.left is None):
                node_tmp = node.right
                node = None
                return node_tmp

            elif (node.right is None):
                node_tmp = node.left
                node = None
                return node_tmp

            node_tmp = self._min(node.right)
            node.ref.time, node.ref = node_tmp.ref.time, node_tmp.ref
            node.right = self._delete(node.right, node_tmp.ref.time)

        if (node is None): return node

        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))
        return self._balance(node)

    def search_node (self, t):
        if (self.root is None): return None
        return self._search(self.root, t)

    def _search (self, node, t):
        if (t < node.ref.time):
            if (node.left is not None):
                return self._search(node.left, t)
        elif (t > node.ref.time):
            if (node.right is not None):
                return self._search(node.right, t)
        return node

    def min (self):
        if (self.root is not None):
            return self._min(self.root)

    def _min (self, node):
        if (node.left is None):
            return node
        return self._min(node.left)

    def max (self):
        if (self.root is not None):
            return self._max(self.root)

    def _max (self, node):
        if (node.right is None):
            return node
        return self._max(node.right)

    def print (self):
        self._print(self.root, 0)

    def _print (self, node, i):
        if (node is None): return

        self._print(node.left, i + 1)
        print(i * ' ' + 'node ' + str(node.ref.time) + ' ' + str(node.ref.value))
        self._print(node.right, i + 1)