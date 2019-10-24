from heap_avl_tree import AVL
from _BST import _BST

class RtrPrioQueue:
    def __init__(self):
        self.q_now = _BST()
        self.updates = AVL()

    def insert_insert (self, t, k):
        value = self.updates.insert(t, k)
        self.q_now.insert(value)

    def insert_deleteMin (self, t):
        value = self.updates.insert(t, None)
        self.q_now.delete(value)

    def delete (self, t):
        value = self.updates.delete(t)
        if (value[0]):
            self.q_now.insert(value[1])
        else:
            self.q_now.delete(value[1])
        
    def min (self):
        min_key = self.q_now.min()
        print(min_key)
        return min_key
    
    def print_heap (self):
        self.updates.print()
    
    def print_qnow (self):
        self.q_now.print()

# função interativa para testar a estrutura
def tester ():
    print("Para finalizar, aperte 'ctrl+d'.")
    print("Insira operações para o heap retroativo.")

    retro_strc = RtrPrioQueue()

    while (True):
        try:
            command = input()
        except:
            print("Finalizando...")
            quit()

        command = command.split()
        args = len(command) - 1
        method_to_call = getattr(retro_strc, command[0])

        if (args == 0):
            method_to_call()
        elif (args == 1):
            method_to_call(int(command[1]))
        elif(args == 2):
            method_to_call(int(command[1]), int(command[2]))

tester()

# caso teste (-inf por causa do max_after_bridge)
#   insert_insert 10 7
#   insert_insert 20 2
#   insert_deleteMin 15
#   insert_insert 6 3
#   insert_insert 8 4
#   insert_insert 11 1
#   delete 11
#   delete 15

#   insert_insert 1 3
#   insert_insert 2 4
#   insert_deleteMin 5
#   insert_deleteMin 6