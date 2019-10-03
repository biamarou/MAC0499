from avl_tree import AVL

class RtrQueue:
    
    def __init__(self):
        self.enqueue_bst = AVL()
        self.dequeue_bst = AVL()

    def insert_enqueue (self, t, v):
        self.enqueue_bst.insert(t, v)

    def insert_dequeue (self, t):
        self.dequeue_bst.insert(t, None)

    def delete_enqueue (self, t):
        self.enqueue_bst.delete(t)
    
    def delete_dequeue (self, t):
        self.dequeue_bst.delete(t)

    def query_kth (self, t, k):
        c = self.dequeue_bst.count(t)
        return self.enqueue_bst.kth(c + k)

    def query_first (self, t):
        return self.query_kth(t, 1)

# função interativa para testar a estrutura
def tester ():
    print("Para finalizar, aperte 'ctrl+d'.")
    print("Insira operações para a fila retroativa.")

    retro_strc = RtrQueue()

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