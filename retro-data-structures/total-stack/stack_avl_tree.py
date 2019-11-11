class AVL:

    class Node:
        def __init__(self, t, o, w, l, r, h, s):
            self.min_right_time = t
            self.top = o
            self.weight = w
            self.left = l
            self.right = r
            self.height = h
            self.size = s      # número de nós internos na subárvore
            self.leaf = False

    class Leaf:
        def __init__(self, t, v, w):
            self.time = t
            self.value = v
            self.weight = w

            if (w == -1): self.top = 0
            else: self.top = 1
            self.leaf = True

    def __init__(self):
        self.root = None

    def size (self):
        return self._size(self.root)

    def _size (self, node):
        if (node.leaf): return 0
        else: return node.size

    def height (self):
        return self._height(self.root)

    def _height (self, node):
        if (node.leaf): return -1
        else: return node.height

    def insert (self, t, v, w):
        if (self.root == None):
            self.root = self.Leaf(t, v, w)
        else:
            self.root = self._insert(self.root, t, v, w)

    def _insert(self, node, t, v, w):
        if (node.leaf):
            new_leaf = self.Leaf(t, v, w)
            w_sum = node.weight + w

            if(t < node.time):
                if (w < node.weight): top = 1
                elif (w == node.weight and w > 0): top = 2
                else: top = 0

                new_node = self.Node(node.time, top, w_sum, new_leaf, node, 0, 1)
            else:
                if (node.weight < w): top = 1
                elif (w == node.weight and w > 0): top = 2
                else: top = 0

                new_node = self.Node(t, top, w_sum, node, new_leaf, 0, 1)

            return new_node

        elif (t < node.min_right_time):
            node.left = self._insert(node.left, t, v, w)

        else:
            node.right = self._insert(node.right, t, v, w)

        top_sum = node.left.top + node.right.weight
        if (top_sum <= 0): node.top = 0
        else: node.top = top_sum

        node.weight += w
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

        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))
        node_tmp.height = 1 + max(self._height(node_tmp.left),
                                  self._height(node_tmp.right))

        node.weight = node.left.weight + node.right.weight
        node_tmp.weight = node_tmp.left.weight + node_tmp.right.weight

        top_sum = node.left.top + node.right.weight
        if (top_sum <= 0): node.top = 0
        else: node.top = top_sum

        top_sum = node_tmp.left.top + node_tmp.right.weight
        if (top_sum <= 0): node_tmp.top = 0
        else: node_tmp.top = top_sum

        return node_tmp

    def _rotate_right (self, node):
        node_tmp = node.left
        node.left = node_tmp.right
        node_tmp.right = node

        node_tmp.size = node.size
        node.size = 1 + self._size(node.left) + self._size(node.right)

        node.height = 1 + max(self._height(node.left),
                              self._height(node.right))
        node_tmp.height = 1 + max(self._height(node_tmp.left),
                                  self._height(node_tmp.right))

        node.weight = node.left.weight + node.right.weight
        node_tmp.weight = node_tmp.left.weight + node_tmp.right.weight

        top_sum = node.left.top + node.right.weight
        if (top_sum <= 0): node.top = 0
        else: node.top = top_sum

        top_sum = node_tmp.left.top + node_tmp.right.weight
        if (top_sum <= 0): node_tmp.top = 0
        else: node_tmp.top = top_sum

        return node_tmp

    def delete (self, t, w):
        if (self.root != None):
            self.root = self._delete(self.root, t, w)

    def _delete (self, node, t, w):
        if (node.leaf): return None

        elif (t < node.min_right_time):
            node.left = self._delete(node.left, t, w)

            if (node.left == None):
                node = node.right
            else:
                node.weight -= w
                top_sum = node.left.top + node.right.weight
                if (top_sum <= 0): node.top = 0
                else: node.top = top_sum
        else:
            node.right = self._delete(node.right, t, w)

            if (node.right == None):
                node = node.left
            else:
                node.weight -= w
                top_sum = node.left.top + node.right.weight
                if (top_sum <= 0): node.top = 0
                else: node.top = top_sum

        if (node.leaf):
            return node
        else:
            if (node.min_right_time == t):
                node.min_right_time = self._min(node.right) # chamado so uma vez por delete
            node.size = 1 + self._size(node.left) + self._size(node.right)
            node.height = 1 + max(self._height(node.left), self._height(node.right))
            return self._balance(node)

    def min (self):
        if (self.root != None):
            return self._min(self.root)
        return 0

    def _min (self, node):
        if (node.leaf):
            return node.time

        return self._min(node.left)

    def max (self):
        if (self.root != None):
            return self._max(self.root)
        return 0

    def _max (self, node):
        if (node.leaf):
            return node.time
        return self._max(node.right)

    def weight_count (self, t):
        if (self.root != None):
            return self._weight_count(self.root, t, 0)
        return 0

    def _weight_count (self, node, t, counter):
        if (node.leaf):
            if (node.time <= t):
                counter += node.weight
            return counter

        elif (t < node.min_right_time):
            return self._weight_count(node.left, t, counter)

        else:
            if (node.left.leaf):
                counter += node.left.weight
            else:
                counter += node.left.weight
            return self._weight_count(node.right, t, counter)

    def kth (self, t, k):
        if (self.weight_count(t) == 0 or t < self.min()):
            return None
        kth = self._kth(self.root, t, k)[0]
        print(kth)
        return(kth)

    def _kth (self, node, t, k):
        if (node.leaf):
            if (node.weight == -1 or k != 1):
                return [None, node.weight]
            else:
                return [node.value]

        elif (t < node.min_right_time):
            return self._kth(node.left, t, k)
        else:
            kth_right = self._kth(node.right, t, k)
            if (kth_right[0] == None):
                k -= kth_right[1]
                if (node.left.top >= k):
                    return [self.get_value(node.left, k)]
                else:
                    return [None, kth_right[1] + node.left.weight]
            else: return kth_right

    def get_value (self, node, k):
        if (node.leaf):
            return node.value

        elif (node.right.top >= k):
            return self.get_value(node.right, k)

        else:
            return self.get_value(node.left, k - node.right.weight)


    def print (self):
        self._print(self.root, 0)
        print("-------------------")

    def _print (self, node, i):
        if (node == None): return

        if (node.leaf):
            print(i*' ' + 'leaf ' + str(node.time) + ' ' + str(node.value))
            return

        self._print(node.left, i+1)
        print(i*' ' + 'node ' + str(node.min_right_time) +
                ' ' + str(node.weight) + ' ' + str(node.top))
        self._print(node.right, i+1)