import math

class AVL:

    class Node:
        def __init__(self, t, o, w, max_, min_, l, r, h, s):
            self.min_right_time = t
            self.top = o
            self.weight = w     
            self.max_out = max_ # maximo valor fora de Qnow (weight = 1)
            self.min_in = min_  # minimo valor em Qnow (weight = 0)
            self.left = l       # filho esquerdo
            self.right = r      # filho direito
            self.height = h     # altura da subarvore
            self.size = s       # número de nós internos na subárvore
            self.leaf = False
    
    class Leaf:
        def __init__(self, t, v, w):
            self.time = t
            self.value = v
            self.weight = w
            
            if (w == -1 or w == 0): self.top = 0
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

    def insert (self, t, v):
        if (self.root == None):
            self.root = self.Leaf(t, v, 0)
            value_Qnow = v
        
        elif(v != None):
            t_bridge = self.last_bridge_before(t)
            max_bridge = self.max_after_bridge(t_bridge)
            
            if (v > max_bridge[1]):
                self.root = self.PRV_insert(self.root, t, v, 0)
                value_Qnow = v

            else:
                self.PRV_set_weight_zero(self.root, max_bridge[0])
                self.root = self.PRV_insert(self.root, t, v, 1)
                value_Qnow = max_bridge[1]

        else:
            t_bridge = self.first_bridge_after(t)
            min_bridge = self.min_before_bridge(t_bridge)
            self.PRV_set_weight_one(self.root, min_bridge[0])
            self.root = self.PRV_insert(self.root, t, v, -1)
            value_Qnow = min_bridge[1]

        return value_Qnow

    def PRV_set_weight_zero (self, node, t):
        if (node.leaf):
            node.weight = 0
            return
        
        elif (t < node.min_right_time):
            self.PRV_set_weight_zero(node.left, t)

        else:
            self.PRV_set_weight_zero(node.right, t)

        node.max_out = self.set_new_max_out(node)
        node.min_in = self.set_new_min_in(node)
        node.weight = node.left.weight + node.right.weight
        
    def PRV_set_weight_one (self, node, t):
        if (node.leaf):
            node.weight = 1
            return
        
        elif (t < node.min_right_time):
            self.PRV_set_weight_one(node.left, t)

        else:
            self.PRV_set_weight_one(node.right, t)

        node.max_out = self.set_new_max_out(node)
        node.min_in = self.set_new_min_in(node)
        node.weight = node.left.weight + node.right.weight

    def PRV_insert(self, node, t, v, w):
        
        if (node.leaf):
            new_leaf = self.Leaf(t, v, w)   
            w_sum = node.weight + w
            
            # definir o valor maximo fora de Qnow
            if (w != 1 and node.weight != 1): max_out = [-1, -float('inf')]
            elif (w == 1 and node.weight != 1): max_out = [t, v]
            elif (w != 1 and node.weight == 1): max_out = [node.time, node.value]
            else:
                if (node.value > new_leaf.value): max_out = [node.time, node.value]
                else: max_out = [t, v]

            # definir o valor minimo dentro de Qnow
            if (w != 0 and node.weight != 0): min_in = [-1, float('inf')]
            elif (w == 0 and node.weight != 0): min_in = [t, v]
            elif (w != 0 and node.weight == 0): min_in = [node.time, node.value]
            else:
                if (node.value < new_leaf.value): min_in = [node.time, node.value]
                else: min_in = [t, v]
            
            if (t < node.time):
                if (w == node.weight and w > 0): top = 2
                elif (node.weight == 1 or (w == 1 and node.weight == 0)): top = 1
                else: top = 0

                new_node = self.Node(node.time, top, w_sum, max_out, min_in, new_leaf, node, 0, 1)

            else:
                if (w == node.weight and w > 0): top = 2
                elif (w == 1 or (node.weight == 1 and w == 0)): top = 1
                else: top = 0
                
                new_node = self.Node(t, top, w_sum, max_out, min_in, node, new_leaf, 0, 1)
            
            return new_node

        elif (t < node.min_right_time):
            node.left = self.PRV_insert(node.left, t, v, w)

        else:
            node.right = self.PRV_insert(node.right, t, v, w)

        top_sum = node.left.top + node.right.weight
        if (top_sum <= 0): node.top = 0
        else: node.top = top_sum
        
        if (w != -1):
            if (node.max_out[1] < v and w == 1): node.max_out = [t, v]
            elif (node.min_in[1] > v and w == 0): node.min_in = [t, v]
        
        node.weight = node.left.weight + node.right.weight
        node.size = 1 + self.PRV_size(node.left) + self.PRV_size(node.right)
        node.height = 1 + max(self.PRV_height(node.left), self.PRV_height(node.right))
        return self.PRV_balance(node)

    def last_bridge_before (self, t):
        if (self.root == None):
            return 0
            
        else:
            sum_weight = self.weight_count(t)
            if (sum_weight == 0): 
                return t
            else:
                kth = self.kth(t, sum_weight)
                if (len(kth) == 1 or kth[0] == None or kth[1] == None):
                    return 0
                return kth[1]

    def first_bridge_after (self, t):
        if (self.root == None):
            return 0
            
        else:
            sum_weight = self.weight_count(t)
            if (sum_weight == 0): 
                return t
            else:
                rvs_kth = self.reverse_kth(t, sum_weight)
                return rvs_kth[0]

    def max_after_bridge (self, t_bridge):
        if (self.root != None):
            return self.PRV_max_after_bridge(self.root, t_bridge)

    def PRV_max_after_bridge (self, node, t_bridge):
        if (node.leaf):
            if (node.weight == 1):
                return [node.time, node.value]
            else:
                return [-1, -float('inf')]
        
        elif (t_bridge < node.min_right_time):
            rtr = self.PRV_max_after_bridge(node.left, t_bridge)
            
            if (node.right.leaf and node.right.weight == 1 and node.right.value > rtr[1]):
                rtr = [node.right.time, node.right.value]
            elif (not node.right.leaf and node.right.max_out[1] > rtr[1]): 
                rtr = node.right.max_out
                
            return rtr
        else:
            return self.PRV_max_after_bridge(node.right, t_bridge)

    def min_before_bridge (self, t_bridge):
        if (self.root != None):
            return self.PRV_min_before_bridge(self.root, t_bridge)

    # devolve o menor valor em Qnow inserido até o instante t_bridge
    def PRV_min_before_bridge (self, node, t_bridge):
        if (node.leaf):
            if (node.weight == 0):
                return [node.time, node.value]
            else:
                return [-1, float('inf')]
        
        elif (t_bridge < node.min_right_time):
            return self.PRV_min_before_bridge(node.left, t_bridge)
            
        else:
            rtr = self.PRV_min_before_bridge(node.right, t_bridge)

            if (node.left.leaf and node.left.value < rtr[1] and node.left.weight == 0):
                rtr = [node.left.time, node.left.value]
            elif (not node.left.leaf and node.left.min_in[1] < rtr[1]): 
                rtr = node.left.min_in
                
            return rtr

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

    def set_new_max_out (self, node):
        if (node.left.leaf):
            if(node.left.weight == 1):
                max_left = [node.left.time, node.left.value]
            else:
                max_left = [-1, -float('inf')]
        else:
            max_left = node.left.max_out

        if (node.right.leaf):
            if(node.right.weight == 1):
                max_right = [node.right.time, node.right.value]
            else:
                max_right = [-1, -float('inf')]
        else:
            max_right = node.right.max_out

        if (max_left[1] > max_right[1]):
            return max_left
        return max_right

    def set_new_min_in (self, node):
        if (node.left.leaf):
            if(node.left.weight == 0):
                min_left = [node.left.time, node.left.value]
            else:
                min_left = [-1, float('inf')]
        else:
            min_left = node.left.min_in

        if (node.right.leaf):
            if(node.right.weight == 0):
                min_right = [node.right.time, node.right.value]
            else:
                min_right = [-1, float('inf')]
        else:
            min_right = node.right.min_in

        if (min_left[1] < min_right[1]):
            return min_left
        return min_right
            
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

        node_tmp.left.max_out = self.set_new_max_out(node_tmp.left)
        node_tmp.max_out = self.set_new_max_out(node_tmp)

        node_tmp.left.min_in = self.set_new_min_in(node_tmp.left)
        node_tmp.min_in = self.set_new_min_in(node_tmp)


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

        node_tmp.right.max_out = self.set_new_max_out(node_tmp.right)
        node_tmp.max_out = self.set_new_max_out(node_tmp)

        node_tmp.right.min_in = self.set_new_min_in(node_tmp.right)
        node_tmp.min_in = self.set_new_min_in(node_tmp)

        return node_tmp

    def PRV_search_node (self, node, t):
        if (node.leaf):
            return node
        if (t < node.min_right_time):
            return self.PRV_search_node(node.left, t)
        else:
            return self.PRV_search_node(node.right, t)
    
    def delete (self, t):        
        if (self.root != None):
            del_node = self.PRV_search_node(self.root, t)

            if (del_node.weight == 0):
               value_Qnow = [False, node.value]
            
            elif (del_node.weight == 1):
                t_bridge = self.first_bridge_after(t)
                min_bridge = self.min_before_bridge(t_bridge)
                self.PRV_set_weight_one(self.root, min_bridge[0])
                value_Qnow = [False, min_bridge[1]]

            else:
                t_bridge = self.last_bridge_before(t - 1) # ponte estritamente antes do instante t
                max_bridge = self.max_after_bridge(t_bridge)
                print(t_bridge)
                print(max_bridge)
                self.PRV_set_weight_zero(self.root, max_bridge[0])
                value_Qnow = [True, max_bridge[1]]

            self.root = self.PRV_delete(self.root, t, del_node.weight)
            return value_Qnow

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
                node.weight = node.left.weight + node.right.weight
                top_sum = node.left.top + node.right.weight
                if (top_sum <= 0): node.top = 0
                else: node.top = top_sum

        if (node.leaf):
            return node
        else:
            if (node.min_right_time == t):
                node.min_right_time = self.PRV_min(node.right)
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
            counter += node.left.weight
            return self.PRV_weight_count(node.right, t, counter)

    def kth (self, t, k):
        return self.PRV_kth(self.root, t, k)

    def PRV_kth (self, node, t, k):
        if (node.leaf):
            if (node.weight != 1 or k != 1):
                return [None, node.weight]
            else:
                return [node] #buscar o max(node.left)
        
        elif (t < node.min_right_time):
            return self.PRV_kth(node.left, t, k)
        
        else:
            kth_right = self.PRV_kth(node.right, t, k)
            if (kth_right[0] == None):
                k -= kth_right[1]
                if (node.left.top >= k):
                    return self.get_value(node.left, k)
                else:
                    return [None, kth_right[1] + node.left.weight]
                
            else: 
                if (len(kth_right) == 1):
                    kth_right.append(self.PRV_max(node.left))
                return kth_right

    def get_value (self, node, k):
        if (node.leaf):
            return [node, None]

        elif (node.right.top >= k):
            rtr_right = self.get_value(node.right, k)
            if (rtr_right[1] == None):
                rtr_right[1] = self.PRV_max(node.left)

            return rtr_right

        else:
            return self.get_value(node.left, k - node.right.weight)

    def reverse_kth (self, t, k):
        if (self.weight_count(t) == 0 or t < self.min()):
            return None
        return self.PRV_reverse_kth(self.root, t, k)      

    def PRV_reverse_kth (self, node, t, k):
        if (node.leaf):
            return [None, 0]
        
        elif (t < node.min_right_time):
            
            kth_left = self.PRV_reverse_kth(node.left, t, k)
            if (kth_left[0] == None):
                k -= kth_left[1]
                if (node.right.top == 0 and -node.right.weight >= k):
                    return self.reverse_get_value(node.right, k)
                else:
                    return [None, kth_left[1] - node.right.weight]
        else:
            return self.PRV_reverse_kth(node.right, t, k)

    def reverse_get_value (self, node, k):
        if (node.leaf):
            return [node.time]

        elif (node.left.top == 0 and -node.left.weight >= k):
            return self.reverse_get_value(node.left, k)

        else:
            return self.reverse_get_value(node.right, k + node.left.weight)

    def print (self):
        self.PRV_print(self.root, 0)
        print("-------------------")

    def PRV_print (self, node, i):
        if (node == None): return
        
        if (node.leaf):
            print(i*'  ' + 'leaf ' + str(node.time) + ' ' + str(node.value) + ' ' + str(node.weight))        
            return

        self.PRV_print(node.left, i+1)
        print(i* '  ' + 'node ' + str(node.min_right_time) + ' ' + str(node.weight) + ' ' + str(node.max_out)+ ' ' + str(node.min_in))
        self.PRV_print(node.right, i+1)
