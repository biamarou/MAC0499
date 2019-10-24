from queue_avl_tree import AVL

class RetroQueue(object):
    
    def __init__(self):
        self.enqueue_tree = AVL()
        self.dequeue_tree = AVL()

    def insert_enqueue (self, t, v):
        self.enqueue_tree.insert(t, v)

    def insert_dequeue (self, t):
        self.dequeue_tree.insert(t, None)

    def delete_enqueue (self, t):
        self.enqueue_tree.delete(t)
    
    def delete_dequeue (self, t):
        self.dequeue_tree.delete(t)

    def query_kth (self, t, k):
        c = self.dequeue_tree.count(t)
        kth = self.enqueue_tree.kth(c + k)
        print(kth)
        return(kth)

    def query_first (self, t):
        return self.query_kth(t, 1)

    def debug_print (self, en):
        if (en):
            self.enqueue_tree.print()
        else:
            self.dequeue_tree.print()

# função interativa para testar a estrutura
def tester ():
    print("Para finalizar, aperte 'ctrl+d'.")
    print("Insira operações para a fila retroativa.")

    retro_strc = RetroQueue()

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