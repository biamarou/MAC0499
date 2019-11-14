class AVL(object):

    class Node(object):
        def __init__(self, t, c, l, r, h, s):
            self.min_right_time = t
            self.leafs = c  # número de folhas na subárvore
            self.left = l
            self.right = r
            self.height = h
            self.size = s
            self.is_leaf = False

    class Leaf(object):
        def __init__(self, t, v):
            self.time = t
            self.value = v
            self.is_leaf = True

    def __init__(self):
        self.root = None

    # número de nós internos na subárvore
    def size (self):
        return self._size(self.root)

    def _size (self, node):
        if (node.is_leaf): return 0
        else: return node.size

    def height (self):
        return self._height(self.root)

    def _height (self, node):
        if (node.is_leaf): return -1
        else: return node.height

    def insert (self, t, v):
        if (self.root is None):
            self.root = self.Leaf(t, v)
        else:
            self.root = self._insert(self.root, t, v)

    def _insert(self, node, t, v):

        if (node.is_leaf):
            new_leaf = self.Leaf(t, v)

            if(t < node.time):
                new_node = self.Node(t, 2, new_leaf, node, 0, 1)
            else:
                new_node = self.Node(node.time, 2, node, new_leaf, 0, 1)

            return new_node

        elif (t < node.min_right_time):
            node.left = self._insert(node.left, t, v)

        else:
            node.right = self._insert(node.right, t, v)

        node.leafs += 1
        node.size = 1 + self._size(node.left) + self._size(node.right)
        node.height = 1 + max(self._height(node.left), self._height(node.right))
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
        node_tmp.size = node.size
        node.size = 1 + self._size(node.left) + self._size(node.right)
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node_tmp.height = 1 + max(self._height(node_tmp.left), self._height(node_tmp.right))

        return node_tmp

    def _rotate_right (self, node):
        node_tmp = node.left
        node.left = node_tmp.right
        node_tmp.right = node
        node_tmp.size = node.size
        node.size = 1 + self._size(node.left) + self._size(node.right)
        node.height = 1 + max(self._height(node.left), self._height(node.right))
        node_tmp.height = 1 + max(self._height(node_tmp.left), self._height(node_tmp.right))

        return node_tmp

    def delete (self, t):
        if (self.root is not None):
            self.root = self._delete(self.root, t)

    def _delete (self, node, t):

        if (node.is_leaf): return None

        elif (t <= node.min_right_time):
            node.left = self._delete(node.left, t)

            if (node.left is None):
                node = node.right
            else:
                node.leafs -= 1

        else:
            node.right = self._delete(node.right, t)

            if (node.right is None):
                node = node.left
            else:
                node.leafs -= 1

        if (node.is_leaf):
            return node
        else:
            if (node.min_right_time == t):
                node.min_right_time = self._min(node.right)
            node.size = 1 + self._size(node.left) + self._size(node.right)
            node.height = 1 + max(self._height(node.left), self._height(node.right))
            return self._balance(node)

    def count (self, t):
        if (self.root is not None):
            return self._count(self.root, t, 0)
        return 0

    def _count (self, node, t, counter):
        if (node.is_leaf):
            if (node.time <= t):
                counter += 1
            return counter

        elif (t < node.min_right_time):
            return self._count(node.left, t, counter)

        else:
            if (node.left.is_leaf):
                counter += 1
            else:
                counter += node.left.leafs
            return self._count(node.right, t, counter)

    def kth (self, t, k):
        if (not self.root.is_leaf and self.root.leafs < k):
            return None
        node = self._kth(self.root, k)
        if (node.time > t):
            return None
        return node.value

    def _kth (self, node, k):
        if (node.is_leaf):
            return node

        elif (node.left.is_leaf):
            if (k == 1):
                return self._kth(node.left, k)
            return self._kth(node.right, k - 1)

        else:
            if (k > node.left.leafs):
                return self._kth(node.right, k - node.left.leafs)
            return self._kth(node.left, k)

    def is_inside (self, t):
        return self._is_inside (self.root, t)

    def _is_inside (self, node, t):
        if (node.is_leaf):
            if (node.time == t): return [True, node.value]
            return [False, None]

        elif (t <= node.min_right_time):
            return self._is_inside (node.left, t)
        elif (t > node.min_right_time):
            return self._is_inside(node.right, t)

    def print (self):
        self._print(self.root, 0)
        print("-------------------")

    def _print (self, node, i):
        if (node is None): return

        if (node.is_leaf):
            print(i * ' ' + 'leaf ' + str(node.time) +
                  ' ' + str(node.value))
            return

        self._print(node.left, i + 1)
        print(i * ' ' + 'node ' + str(node.min_right_time) +
              ' ' + str(node.leafs))
        self._print(node.right, i + 1)