class DoublyLinkedList(object):

    class Cell(object):
        def __init__(self, t, v, n, p):
            self.time = t
            self.value = v
            self.next = n
            self.past = p

    def __init__(self):
        self.head = None
        self.front = None
        self.back = None

    def insert(self, cell, t, v, operation):
        new_cell = None
        if (operation):
            if (cell is None):
                new_cell = self.Cell(t, v, None, None)
                self.head = new_cell
                self.front = self.head
                self.back = self.head
            elif (t < cell.time):
                new_cell = self.Cell(t, v, cell, cell.past)
                if (cell.past):
                    cell.past.next = new_cell
                cell.past = new_cell
                if (cell == self.head):
                    self.head = cell.past
            else:
                new_cell = self.Cell(t, v, cell.next, cell)
                if (cell.next):
                    cell.next.past = new_cell
                cell.next = new_cell
                if (cell == self.back):
                    self.back = cell.next

        self._insert_update_pointer(t, operation)
        return new_cell

    def delete(self, t, cell, operation):
        if (self.head is None): return
        self._delete_update_pointer(t, operation)
        if (operation):
            if (cell.past is not None):
                cell.past.next = cell.next
            if (cell.next is not None):
                cell.next.past = cell.past
            if (cell == self.head):
                self.head = cell.next

    def _insert_update_pointer(self, t, operation):
        if (operation and t < self.front.time):
                self.front = self.front.past
        elif(not operation):
            self.front = self.front.next

    def _delete_update_pointer(self, t, operation):
        if (self.head is None): return
        if (operation and t <= self.front.time):
            self.front = self.front.next
        elif(not operation):
            self.front = self.front.past

    def print(self):
        self._print_forward(self.head)
        #self._print_backward(self.back)

    def _print_forward(self, cell):
        if (not cell): return
        print('cell ' + str(cell.time) + ' ' + str(cell.value))
        self._print_forward(cell.next)

    def _print_backward(self, cell):
        if (not cell): return
        print('cell ' + str(cell.time) + ' ' + str(cell.value))
        self._print_backward(cell.past)