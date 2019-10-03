from stack_avl_tree import AVL

class RtrStack:
    
    def __init__(self):
        self.stack_avl = AVL()

    def insert_push (self, t, v):
        self.stack_avl.insert(t, v, 1)

    def insert_pop (self, t):
        self.stack_avl.insert(t, None, -1)

    def delete_push (self, t):
        self.stack_avl.delete(t, 1)
    
    def delete_pop (self, t):
        self.stack_avl.delete(t, -1)

    def query_top (self, t):
        self.stack_avl.kth(t, 1)

    def kth (self, t, k):
        self.stack_avl.kth(t, k)
        
    def debug_print (self):
        self.stack_avl.print()
        


# função interativa para testar a estrutura
def tester ():
    print("Para finalizar, aperte 'ctrl+d'.")
    print("Insira operações para a pilha retroativa.")

    retro_strc = RtrStack()

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