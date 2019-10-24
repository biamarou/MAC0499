from _avl_tree import AVL
from _linked_list import DoublyLinkedList

class PartialQueue (object):
    def __init__(self):
        self.time_tree = AVL()
        self.enqueue_list = DoublyLinkedList()

    def insert_enqueue(self, t, v):
        cell = None
        node = self.time_tree.search_node(t)
        if (node):
            cell = node.ref
        new_cell = self.enqueue_list.insert(cell, t, v, True)
        self.time_tree.insert(new_cell)

    def insert_dequeue(self, t):
        self.enqueue_list.insert(None, t, None, False)

    def delete_enqueue(self, t):
        node = self.time_tree.search_node(t)
        if (node is None):
            cell = None
        else:
            cell = node.ref
        self.enqueue_list.delete(t, cell, True)
        self.time_tree.delete(t)

    def delete_dequeue(self, t):
        self.enqueue_list.delete(t, None, False)

    def query_front(self):
        print(self.enqueue_list.front.value)

    def query_back(self):
        print(self.enqueue_list.back.value)

    def print_structures(self):
        print("-------- List --------")
        self.enqueue_list.print()
        print("-------- Tree --------")
        self.time_tree.print()
        print("----------------------")

def tester ():
    print("Para finalizar, aperte 'ctrl+d'.")
    print("Insira operações para a fila parcialmente retroativa.")

    retro_strc = PartialQueue()

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