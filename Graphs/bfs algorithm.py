class qando:
    def __init__(self):
        self.q = []
        self.o = []
        self.f = None
        self.r = None

    def __len__(self):
        return len(q)

    def isEmpty(self):
        if self.f == None: return True
        if self.f > self.r: return True
        return False

    def enq(self, item, dequeued):
        self.q.append(item)
        if self.f == None:
            self.f = 0
            self.r = 0
        else:
            self.r += 1
        self.o.append(dequeued)

    def deq(self):
        if self.isEmpty(): return
        x = self.q[self.f]
        self.f += 1
        return x

    def readqando(self):
        i = self.r
        x = self.q[self.r]
        path = []
        while i >= 0 and x is not None:
            if self.q[i] == x:
                path.append(x)
                x = self.o[i]
            i -= 1
        path.reverse()
        return path

    def printcurrentstate(self):
        print("Q =", self.q, "F =", self.f, "R =", self.r)
        print("O =", self.o)

# Driver code for the qando class

# Creating an instance of the qando class
bfs_queue = qando()

# Enqueuing items
bfs_queue.enq("A", None)
bfs_queue.enq("B", "A")
bfs_queue.enq("C", "A")
bfs_queue.enq("D", "C")

# Printing initial state
print("Initial State:")
bfs_queue.printcurrentstate()

# Dequeuing items
dequeued_item1 = bfs_queue.deq()
dequeued_item2 = bfs_queue.deq()

print(f"\nDequeued Items: {dequeued_item1}, {dequeued_item2}")

# Enqueuing more items
bfs_queue.enq("E", "D")
bfs_queue.enq("F", "E")

# Printing state after more operations
print("\nState after Dequeues and Enqueues:")
bfs_queue.printcurrentstate()

# Reading the queue and output list to reconstruct the path
path = bfs_queue.readqando()
print("\nReconstructed Path:", path)

# Performing more operations
bfs_queue.enq("G", "F")
bfs_queue.enq("H", "G")
bfs_queue.enq("I", "H")

# Printing final state
print("\nFinal State:")
bfs_queue.printcurrentstate()

# Reading the queue and output list again
path_after_operations = bfs_queue.readqando()
print("\nReconstructed Path after More Operations:", path_after_operations)
