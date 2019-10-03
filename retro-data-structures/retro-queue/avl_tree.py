class AVL:

    class Node:
        def __init__(self, t, c, l, r, h, s):
            self.left_time = t
            self.children = c  # número de folhas na subárvore
            self.left = l
            self.right = r
            self.height = h
            self.size = s
            self.leaf = False
    
    class Leaf:
        def __init__(self, t, v):
            self.time = t
            self.value = v
            self.leaf = True

    def __init__(self):
        self.root = None

    # número de nós internos na subárvore
    def size (self):
        return self.PRV_size(self.root)

    def PRV_size (self, node):
        if (node.leaf): return 0
        else: return node.size

    def height (self):
        return self.PRV_height(self.root)

    def PRV_height (self, node):
        if (node.leaf): return -1
        else: return node.height

    def insert (self, t, v):
        if (self.root == None):
            self.root = self.Leaf(t, v)
        else:
            self.root = self.PRV_insert(self.root, t, v)

    def PRV_insert(self, node, t, v):
        
        if (node.leaf):
            new_leaf = self.Leaf(t, v)   
            
            if(t < node.time):
                new_node = self.Node(t, 2, new_leaf, node, 0, 1)
            else:
                new_node = self.Node(node.time, 2, node, new_leaf, 0, 1)
            
            return new_node

        elif (t < node.left_time):
            node.left = self.PRV_insert(node.left, t, v)
            node.children += 1
            
            if (node.left.left_time > node.left_time):
                node.left_time = node.left.left_time
            
        else:
            node.right = self.PRV_insert(node.right, t, v)
            node.children += 1
            
        node.size = 1 + self.PRV_size(node.left) + self.PRV_size(node.right)
        node.height = 1 + max(self.PRV_height(node.left), self.PRV_height(node.right))
        return self.PRV_balance(node)

    def PRV_balance_factor (self, node):
        return self.PRV_height(node.left) - self.PRV_height(node.right)

    def PRV_balance (self, node):
        if (self.PRV_balance_factor(node) < -1):
            if (self.PRV_balance_factor(node.right) > 0):
                node.right = self.PRV_rotate_right(node.right)
            
            node = self.PRV_rotate_left(node)

        elif (self.PRV_balance_factor(node) > 1):
            if (self.PRV_balance_factor(node.left) < 0):
                node.left = self.PRV_rotate_left(node.left)
            
            node = self.PRV_rotate_right(node)

        return node
            
    def PRV_rotate_left (self, node):
        node_tmp = node.right
        node.right = node_tmp.left
        node_tmp.left = node
        node_tmp.size = node.size
        node.size = 1 + self.PRV_size(node.left) + self.PRV_size(node.right)
        node.height = 1 + max(self.PRV_height(node.left), self.PRV_height(node.right))
        node_tmp.height = 1 + max(self.PRV_height(node_tmp.left), self.PRV_height(node_tmp.right))

        return node_tmp

    def PRV_rotate_right (self, node):
        node_tmp = node.left
        node.left = node_tmp.right
        node_tmp.right = node
        node_tmp.size = node.size
        node.size = 1 + self.PRV_size(node.left) + self.PRV_size(node.right)
        node.height = 1 + max(self.PRV_height(node.left), self.PRV_height(node.right))
        node_tmp.height = 1 + max(self.PRV_height(node_tmp.left), self.PRV_height(node_tmp.right))

        return node_tmp

    def delete (self, t):
        if (self.root != None):
            self.root = self.PRV_delete(self.root, t)

    def PRV_delete (self, node, t):
        
        if (node.leaf): return None
            
        elif (t <= node.left_time):
            node.left = self.PRV_delete(node.left, t)
            
            if (node.left == None):
                node = node.right
            else:
                node.children -= 1
            
        else:
            node.right = self.PRV_delete(node.right, t)
            
            if (node.right == None):
                node = node.left
                
            else:
                node.children -= 1
        
        

        if (node.leaf):
            return node
        else:
            if (node.left_time == t):
                node.left_time = self.PRV_max(node.left)
            node.size = 1 + self.PRV_size(node.left) + self.PRV_size(node.right)
            node.height = 1 + max(self.PRV_height(node.left), self.PRV_height(node.right))
            return self.PRV_balance(node)

    def min (self):
        if (self.root != None):
            return self.PRV_min(self.root)
        return 0

    def PRV_min (self, node):
        if (node.leaf):
            return node.time

        return self.PRV_min(node.left)

    def max (self):
        if (self.root != None):
            return self.PRV_max(self.root)
        return 0

    def PRV_max (self, node):
        if (node.leaf):
            return node.time

        return self.PRV_max(node.right)
            
    
    def count (self, t):
        if (self.root != None):
            return self.PRV_count(self.root, t, 0)
        return 0

    def PRV_count (self, node, t, counter):
        if (node.leaf):
            # remover linhas 174-175 se quiser excluir o próprio instante buscado
            if (node.time <= t):
                counter += 1
            return counter
        
        elif (t < node.left_time):
            return self.PRV_count(node.left, t, counter)
        
        else:
            if (node.left.leaf):
                counter += 1
            else:
                counter += node.left.children
            return self.PRV_count(node.right, t, counter)

    def kth (self, k):
        if (not self.root.leaf and self.root.children < k):
            return
        kth = self.PRV_kth(self.root, k)
        print(kth)
        return(kth)

    def PRV_kth (self, node, k):
        if (node.leaf):
            return node.value

        elif (node.left.leaf):
            if (k == 1):
                return self.PRV_kth(node.left, k)
            return self.PRV_kth(node.right, k - 1)
        
        else:
            if (k > node.left.children):
                return self.PRV_kth(node.right, k - node.left.children)
            return self.PRV_kth(node.left, k)

    def biggest_minor (self, t):
        return self.PRV_biggest_minor (self.root, t, 0)

    def PRV_biggest_minor (self, node, t, n):
        if (node.leaf): 
            if (node.time > t): return n
            return node.time

        elif (t < node.left_time):
            return self.PRV_biggest_minor (node.left, t, n)
        elif (t > node.left_time):
            return self.PRV_biggest_minor(node.right, t, node.left_time)

    def is_inside (self, t):
        return self.PRV_is_inside (self.root, t)

    def PRV_is_inside (self, node, t):
        if (node.leaf): 
            if (node.time == t): return [True, node.value]
            return [False, None]

        elif (t <= node.left_time):
            return self.PRV_is_inside (node.left, t)
        elif (t > node.left_time):
            return self.PRV_is_inside(node.right, t)

    

    def print (self):
        self.PRV_print(self.root)
        print("-------------------")

    def PRV_print (self, node):
        if (node == None): return
        
        if (node.leaf):
            print('leaf ' + str(node.time) + ' ' + str(node.value))        
            return

        self.PRV_print(node.left)
        print('node ' + str(node.left_time) + ' ' + str(node.children))
        self.PRV_print(node.right)
