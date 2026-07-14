
import math


# creates a node object with a key-data pair
class Node(object):
    def __init__(self, k, d=0):
        self.key = k
        self.data = d
        
    # formatted string for the node object
    def __str__(self):
        return "(" + str(self.key) + "," + repr(self.data) + ")"


# MinMaxHeap class
class MinMaxHeap(object):
    
    # Constructor: sets array size and initializes number of items in the heap to 0
    def __init__(self, size):
        # create an array of specified size
        self.__arr = [None] * size
        # number of elements in the heap is initially 0
        self.__nItems = 0
    
    # private method to push down the elements of the heap
    def __pushDown(self, h, i):
        
        # If i is on a min (even) level (account for the array beginning at 1 by adding 1 to the log)
        level = math.log2(i+1) // 1
        if level % 2 == 0:        
            self.__pushDownMin(h, i)
        # If i is on a max (odd) level
        else:
            self.__pushDownMax(h, i)
            
    # private method to push down if i is on a min level
    def __pushDownMin(self, h, i):
        
        # Find the left and right children positions
        leftChild = 2*i+1
        rightChild = leftChild + 1
       
        # if i has children
        if leftChild < self.__nItems and rightChild < self.__nItems:
            smallest = leftChild
            
            # find the grandchildren
            a = 2*leftChild+1
            b = a + 1
            c = 2*rightChild+1
            d = rightChild + 1
            
            # Initially, grandChild is not the smallest
            grandChild = False
            children = [leftChild, rightChild, a, b, c, d]
            smallestKey = h[leftChild].key
            
            # loop through children and find the smallest grandchild or child of i
            for x in children:
                if h[x] is not None and h[x].key < smallestKey:
                    smallest = x
                    smallestKey = h[x].key
                    
            # if smallest is a grandChild
            if (h[c] is not None and smallestKey == h[c].key) or (h[d] is not None and smallestKey == h[d].key) or (h[a] is not None and smallestKey == h[a].key) or (h[b] is not None and smallestKey == h[b].key):
                # set grandChild to True
                grandChild = True   
                
            m = smallest   
            # if smallest is a grandChild    
            if grandChild == True:
                # and the grandchild is smaller than i
                if h[m].key < h[i].key:
                    # swap i and m
                    temp = h[m]
                    h[m] = h[i]
                    h[i] = temp
                    
                    # if m is larger than its parent
                    if h[m].key > h[((m-1) // 2)].key:
                        # swap the two
                        temp = h[m]
                        h[m] = h[((m-1) // 2)]
                        h[((m-1) // 2)] = temp
                        
                    # push down    
                    self.__pushDown(h, m)
                    
            # if m is smaller than i
            elif h[m].key < h[i].key:
                # swap them
                temp = h[m]
                h[m] = h[i]
                h[i] = temp  
        # else if there is a leftChild and leftChild is smaller than i
        elif leftChild < self.__nItems and h[leftChild].key < h[i].key:
            # swap the two
            temp = h[leftChild]
            h[leftChild] = h[i]
            h[i] = temp             
            
                
                
    # private method to push down if i is on a maxLevel            
    def __pushDownMax(self, h, i):
        
        # Find the left and right children positions
        leftChild = 2*i+1
        rightChild = leftChild + 1

        # if i has children
        if leftChild < self.__nItems and rightChild < self.__nItems:
            largest = leftChild
            
            # find the grandchildren
            a = 2*leftChild+1
            b = a + 1
            c = 2*rightChild+1
            d = rightChild + 1
            
            # Initially, grandChild is not the smallest
            grandChild = False
            children = [leftChild, rightChild, a, b, c, d]
            largestKey = h[leftChild].key
            
            # loop through the children to find the smallest grandchild or child of i
            for x in children:
                if h[x] is not None and h[x].key > largestKey:
                    largest = x
                    largestKey = h[x].key
                    
            # if largest is a grandChild
            if (h[c] is not None and largestKey == h[c].key) or (h[d] is not None and largestKey == h[d].key) or (h[a] is not None and largestKey == h[a].key) or (h[b] is not None and largestKey == h[b].key):
                # set grandChild to True
                grandChild = True    
            m = largest   
            
            # is smallest is a grandChild    
            if grandChild == True:
                # and the grandchild is larger than i
                if h[m].key > h[i].key:
                    # swap i and m
                    temp = h[m]
                    h[m] = h[i]
                    h[i] = temp
                    
                    # if m is smaller than its parent
                    if h[m].key < h[((m-1) // 2)].key:
                        # swap the two
                        temp = h[m]
                        h[m] = h[((m-1) // 2)]
                        h[((m-1) // 2)] = temp
                        
                    # push down    
                    self.__pushDown(h, m)
                    
            # if m is larger than i
            elif h[m].key > h[i].key:
                
                # swap then
                temp = h[m]
                h[m] = h[i]
                h[i] = temp  
                
        # else if there is a leftChild and leftChild is greater than i        
        elif leftChild < self.__nItems and h[leftChild].key > h[i].key:
            # swap them
            temp = h[leftChild]
            h[leftChild] = h[i]
            h[i] = temp           
        
               
     # insert a key, data pair into the heap.  
    def insert(self, key, data):
       
        # if the heap is full, return False
        if self.__nItems == len(self.__arr): return False
        
        #append the key to the end of the array
        self.__arr[self.__nItems] = Node(key, data)
        
        # pushUp to re-heap
        self.__pushUp(self.__arr, self.__nItems)
        
        # increment nItems
        self.__nItems += 1
        
        return True
        
    # private method pushUp to re-eap after insert    
    def __pushUp(self, h, i):
        # if i is not the root
        if i != 0:
            # find the parent
            parent = ((i-1) // 2)
            
            # find the current level
            level = math.log2(i+1) // 1
            
            # if i is on a min (even) row 
            if level % 2 == 0:
                # if i is greater than its parent
                if h[i].key > h[parent].key:
                    # swap them
                    temp = h[parent]
                    h[parent] = h[i]
                    h[i] = temp 
                    # pushUpMax
                    self.__pushUpMax(h, parent)
                else:
                    # or else do pushUpMin
                    self.__pushUpMin(h, i)
                    
            # if i is on a max (odd) row
            else:
                # if i is less than its parent
                if h[i].key < h[parent].key:
                    # swap them
                    temp = h[parent]
                    h[parent] = h[i]
                    h[i] = temp
                    # and pushUpMin
                    self.__pushUpMin(h, parent)
                    
                # or else do pushUpMax
                else:
                    self.__pushUpMax(h, i)
                     
    # private method pushUpMin called by pushUp                
    def __pushUpMin(self, h, i):
        
        # Find the parent and grandparent
        parent = ((i-1) // 2)
        g = ((parent-1) // 2)
        # if the grandparent exists and is is greater than i
        if g >= 0 and h[i].key < h[g].key:
            # swap then
            temp = h[i]
            h[i] = h[g]
            h[g] = temp
            # call pushUpMin
            self.__pushUpMin(h, g)
            
    # private method pushUpMax called by pushUp 
    def __pushUpMax(self, h, i):
        # Find the grandparent and parent
        parent = ((i-1) // 2)
        g = ((parent-1) // 2)   
        # if the grandparent exists and is is less than i
        if g >= 0 and h[i].key > h[g].key:
            # swap them
            temp = h[i]
            h[i] = h[g]
            h[g] = temp
            self.__pushUpMax(h, g)
        
    
    # find and return the minimum value
    def findMin(self):
        # if the heap is empty, return None
        if self.__nItems == 0: return None
        return self.__arr[0].key, self.__arr[0].data
    
    # find and return the maximum value
    def findMax(self):
        # If the heap is empty, return none
        if self.__nItems == 0: return None
        # If the array only has 1 element, return it
        if self.__nItems == 1: return self.__arr[0].key, self.__arr[0].data
        largest = self.__arr[1]
        # find the max of the 2 keys and return the key, data pair
        if self.__arr[2] is not None:
            if self.__arr[1].key > self.__arr[2].key:
                largest = self.__arr[1]
            else: largest = self.__arr[2]
           
        return largest.key, largest.data
    
    # remove and return the minimum value
    def removeMin(self):
        # if the heap is empty, return None
        if self.__nItems == 0: return None
        # The min is the top value
        minimum = self.__arr[0]
        # decrement nItems
        self.__nItems -= 1
        # replace the 1st value with the last value in the heap
        self.__arr[0] = self.__arr[self.__nItems]
        # re-heap
        self.__pushDown(self.__arr, 0)
        # set the last value to None (since it was placed at the top)
        self.__arr[self.__nItems] = None
        # return the key, data pair
        return minimum.key, minimum.data
        
    # remove and return the manimum value
    def removeMax(self): 
        # if the heap is empty, return None
        if self.__nItems == 0: return None
        
        
        # If the heap only has 1 element, it is the max
        if self.__nItems == 1:
            maximum = self.__arr[0]
            # decrement nItems
            self.__nItems -= 1
            return maximum.key, maximum.data
        
        # find the max if more than 2 elements
        if  self.__arr[2] is not None:
            if self.__arr[2].key > self.__arr[1].key:
                maximum = self.__arr[2]
                # decrement nItems
                self.__nItems -= 1
                # replace with the last item in the heap
                self.__arr[2] = self.__arr[self.__nItems]
                #pushDown
                self.__pushDown(self.__arr, 2) 
                self.__arr[self.__nItems] = None
            elif self.__arr[2].key < self.__arr[1].key:
                maximum = self.__arr[1]
                # decrement nItems
                self.__nItems -= 1
                # replace with the last element and pushDown to re-heap
                self.__arr[1] = self.__arr[self.__nItems]
                self.__pushDown(self.__arr, 1) 
                self.__arr[self.__nItems] = None                
        else:
            # the max is the first item in the second row
            maximum = self.__arr[1]
            # decrement nItems
            self.__nItems -= 1
            # replace with the last element and pushDown to re-heap
            self.__arr[1] = self.__arr[self.__nItems]
            self.__pushDown(self.__arr, 1) 
            self.__arr[self.__nItems] = None            
            
        # return the key, value pair
        return maximum.key, maximum.data
            
    






