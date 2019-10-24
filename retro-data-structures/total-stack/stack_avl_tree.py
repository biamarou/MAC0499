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
        return self.PRV_size(self.root)

    def PRV_size (self, node):
        if (node.leaf): return 0
        else: return node.size

    def height (self):
        return self.PRV_height(self.root)

    def PRV_height (self, node):
        if (node.leaf): return -1
        else: return node.height

    def insert (self, t, v, w):
        if (self.root == None):
            self.root = self.Leaf(t, v, w)
        else:
            self.root = self.PRV_insert(self.root, t, v, w)

    def PRV_insert(self, node, t, v, w):
        
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
            node.left = self.PRV_insert(node.left, t, v, w)

        else:
            node.right = self.PRV_insert(node.right, t, v, w)

        top_sum = node.left.top + node.right.weight
        if (top_sum <= 0): node.top = 0
        else: node.top = top_sum
        
        node.weight += w
            
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
        
        node.weight = node.left.weight + node.right.weight
        node_tmp.weight = node_tmp.left.weight + node_tmp.right.weight
        
        top_sum = node.left.top + node.right.weight
        if (top_sum <= 0): node.top = 0
        else: node.top = top_sum

        top_sum = node_tmp.left.top + node_tmp.right.weight
        if (top_sum <= 0): node_tmp.top = 0
        else: node_tmp.top = top_sum

        return node_tmp

    def PRV_rotate_right (self, node):
        node_tmp = node.left
        node.left = node_tmp.right
        node_tmp.right = node
        
        node_tmp.size = node.size
        node.size = 1 + self.PRV_size(node.left) + self.PRV_size(node.right)
        
        node.height = 1 + max(self.PRV_height(node.left), self.PRV_height(node.right))
        node_tmp.height = 1 + max(self.PRV_height(node_tmp.left), self.PRV_height(node_tmp.right))
        
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
            self.root = self.PRV_delete(self.root, t, w)

    def PRV_delete (self, node, t, w):
        
        if (node.leaf): return None
            
        elif (t < node.min_right_time):
            node.left = self.PRV_delete(node.left, t, w)
            
            if (node.left == None):
                node = node.right
            else:
                node.weight -= w
                top_sum = node.left.top + node.right.weight
                if (top_sum <= 0): node.top = 0
                else: node.top = top_sum
            
        else:
            node.right = self.PRV_delete(node.right, t, w)
            
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
                node.min_right_time = self.PRV_min(node.right) # chamado so uma vez por delete
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
            
    def weight_count (self, t):
        if (self.root != None):
            return self.PRV_weight_count(self.root, t, 0)
        return 0

    def PRV_weight_count (self, node, t, counter):
        if (node.leaf):
            if (node.time <= t):
                counter += node.weight
            return counter
        
        elif (t < node.min_right_time):
            return self.PRV_weight_count(node.left, t, counter)
        
        else:
            if (node.left.leaf):
                counter += node.left.weight
            else:
                counter += node.left.weight
            return self.PRV_weight_count(node.right, t, counter)

    def kth (self, t, k):
        if (self.weight_count(t) == 0 or t < self.min()):
            return None
        kth = self.PRV_kth(self.root, t, k)[0]
        print(kth)
        return(kth)

    def PRV_kth (self, node, t, k):
        if (node.leaf):
            if (node.weight == -1 or k != 1):
                return [None, node.weight]
            else:
                return [node.value]
        
        elif (t < node.min_right_time):
            return self.PRV_kth(node.left, t, k)
        
        else:
            kth_right = self.PRV_kth(node.right, t, k)
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
        self.PRV_print(self.root, 0)
        print("-------------------")

    def PRV_print (self, node, i):
        if (node == None): return
        
        if (node.leaf):
            print(i*' ' + 'leaf ' + str(node.time) + ' ' + str(node.value))        
            return

        self.PRV_print(node.left, i+1)
        print(i*' ' + 'node ' + str(node.min_right_time) + ' ' + str(node.weight) + ' ' + str(node.top))
        self.PRV_print(node.right, i+1)