#Uploaded 4.11.2016
#author: Aditya Kelekar

'''
PROBLEM STATEMENT:

This exercise was done as part of a course in Algorithms and Datastructures at Aalto University (Fall 2016).

A class implementing a minheap (used for a priority queue) was provided. The class can be used for simple prioritization tasks.
The task with the smallest integer has the highest priority.
For example, in the task queue [ (3, "Do homework"), (1, "Eat), (2, "Sleep") ] the task "Eat" has the highest priority.

Several of the methods needed by the minheap to work properly had not yet been implemented.
My task was to fix all the methods which begin with the comment: "Not Initially Implemented"


COMMENTS ON MY PROGRAM SOLUTION:
While working for a solution, I found a similar solution on the Web which had methods similar to the ones that I needed to implement.
https://interactivepython.org/runestone/static/pythonds/Trees/BinaryHeapImplementation.html
I noted that in my problem's minheap class, there was no "zeroth" array element, while the one in the above link had it.

I developed my understanding of the minheap class by reading the discussion in the above link and then created the logic and code to write out the missing methods.

Additionally I wrote a few test scripts to check that the methods work as intended. 


'''
class MinHeap:
    """
    A min heap implementation.
    Elements are stored internally in an array of tuples (priority, element),
    where element can be any object and priority is an comparable object.

    For example for (5, object3), (23, object2), (1, object7) the priority of
    the objects should be: object7, object3, object2.
    """

    def __init__(self, initial_data=None):
        """If initial_data is given, it should be an iterable sequence of tuples (lists of tuples are fine)."""
        if initial_data is None:
            self.clear()
        else:
            self.array = list(initial_data)# eg. array[0] = 10,  array[1] = 11... array[10] = 100
            self.size = len(self.array)  #size = 11

        self.buildheap()


    def clear(self):
        """Delete all elements from the heap and reset its size."""
        self.array = []
        self.size = 0


    def is_empty(self):
        return self.size == 0


    def buildheap(self):
        """Heapify the existing array."""
        # Build the heap by heapifying all internal nodes,
        # starting from the last internal node up to the root
        for i in range((self.size // 2) - 1, -1, -1):  # 11//2 = 5...  (5 - 1, -1, -1)  = (4, -1, -1)  = 4,3,2,1,0  = 5 iterations
            self._heapify_down(i)


    def _swap(self, i, j):
        """Swaps in-place the priority-object pairs at indexes i and j."""
        if i != j:
            self.array[j], self.array[i] = self.array[i], self.array[j]


    def _heapify_up(self, i):
        """Restore heap property from the element at i to the root."""
        while i > 0:
            # Select the parent of i
            parent_index = (i - 1) // 2
            # If the parent has a lower priority than i, swap parent with i
            if self._higher_priority(i, parent_index):
                self._swap(i, parent_index)
            # Heapify the parent
            i = parent_index


    def _left_child(self, i):
        """Return the index of the left child of i. Return -1 if i has no left child.
        Raise an IndexError if the index i is invalid."""
        if not 0 <= i < self.size:
            raise IndexError("A node which does not exist cannot have a left child")
        return i*2 + 1 if i < self.size//2 else -1


    def _right_child(self, i):
        """Return the index of the right child of i. Return -1 if i has no right child.
        Raise an IndexError if the index i is invalid."""
        if not 0 <= i < self.size:
            raise IndexError("A node which does not exist cannot have a right child")
        return i*2 + 2 if i < (self.size-1)//2 else -1


    def _is_leaf(self, i):
        """Return False if the node at i has one or more children, else True.
        Raise an IndexError if the index i is invalid."""
        if not 0 <= i < self.size:
            raise IndexError("A node which does not exist cannot be a leaf")
        return -1 == self._left_child(i) == self._right_child(i)


    def _min_child(self, i):
        """Return the index of the child with higher priority of the element at index i.
        Raise an IndexError if the node at index i is a leaf."""
        # Get indexes for the left and right child
        i_left = self._left_child(i)
        i_right = self._right_child(i)

        if -1 == i_left == i_right:
            # Node i is a leaf
            raise IndexError("The node at index i has no children.")
        if -1 == i_right:
            # Node i has only a left child
            return i_left

        # Node i has two children
        # Compare the elements and return the index with the higher priority
        return i_left if self._higher_priority(i_left, i_right) else i_right
        #adi: returns i_left or i_right after checking which one has higher priority



    #"Not Initially Implemented"
    def _higher_priority(self, i, j): #1 Done
        """Return True if element at index i has a higher priority (lower value)) than the element at index j, else False.""" 
        if self.array [[i][0]] < self.array [[j][0]]:  
                return True
        else:
                return False
       

    def insert(self, pair): #2 DONE
        """Insert a new (priority, object) pair into the heap and heapifiy the heap."""

        for i in self.array: #this tests if the pair provided for insertion has the same priority as an existing pair; rejects same priority pair. 
            if i[0] == pair[0]:
                return

        self.array.append (pair)
        self.size = self.size + 1
        self._heapify_up(self.size-1)  #the last element is at the position (self.size-1)
       


    def top(self): #3 DONE
        """Return the object at the top of the heap or None if heap is empty. """
        if self.is_empty():
            return None
        else:
            return self.array [0][1]
        


    def _heapify_down(self, i): #4 DONE 
        """Restore heap property from the element at i to the last leaf."""
        while 0 <= i < self.size and not self._is_leaf(i):
            mc = self._min_child(i)
            if self._higher_priority(mc, i): 
                self._swap(i, mc)
            i = mc
     



    def pop(self): #5 DONE
        """Remove the pair at the top of the heap and return the removed object.
        Raises a RuntimeError if the heap is empty."""
        # Raise error if the heap is empty
        if self.is_empty():
            raise RuntimeError("Cannot pop from an empty heap.")
        else:
            #temp = self.array [[0][1]]  #WRONG access style
            temp = self.array [0][1]
            #for removing the pair:
            #1.copy last pair to the root
            self.array [0] = self.array [self.size-1]
            #2.decrease the array size
            self.size = self.size - 1
            #3. remove the last pair
            del self.array[-1]
            #4. heapify_down the root pair
            self._heapify_down(0)
            return temp

#create a minHeap
minHeap1 = MinHeap(((11,2), (5,6), (7,8)))

minHeap1.insert((3,4))

minHeap3 = MinHeap(((11,2), (5,6), (1,1), (7,8)))

#checking top method
print(minHeap1.top())
print(minHeap3.top())
#prints:
#4
#1


#checking pop method
print(minHeap1.pop())
print(minHeap3.pop())
#prints:
#4
#1

#Second pop on minHeap3
print("Second pop on minHeap3")
print(minHeap3.pop())
#prints:
#6

#Checking combinations of pop and insert methods
minHeap3.insert((3,4))
#Third pop on minHeap3
print("Third pop on minHeap3 after an insert which is the new smallest")
print(minHeap3.pop())
#prints:
#4

minHeap3.insert((100,100))
#Third pop on minHeap3
print("Fourth pop on minHeap3 after an insert which is not the new smallest")
print(minHeap3.pop())
#prints:
#8


