import time

import os
import sys


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, passed_in_value):
        # if the passed in value is less than the node
        if passed_in_value < self.value:
            # if there is no less than node
            if self.left == None:
                # make a node
                self.left = BinarySearchTree(passed_in_value)
            # if there is a node there
            else:
                # be recursive
                self.left.insert(passed_in_value)
        # if the passed in value is greater than the node
        else:
            # if there is no greater than node
            if self.right == None:
                # make a node
                self.right = BinarySearchTree(passed_in_value)
            # if a node already exists
            else:
                # be recursive
                self.right.insert(passed_in_value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if current value is right, return true
        if target == self.value:
            return target
        # if target is less than current value
        elif target < self.value:
            # if there is no left node, return false
            if self.left == None:
                return None
            # if there is a left node
            else:
                return self.left.contains(target)

        # if target is greater than current value
        else:
            # if there is no right node, return false
            if self.right == None:
                return None
            # if there is a right node
            else:
                return self.right.contains(target)


start_time = time.time()
# print(os.getcwd())
# print("Current working dir : %s" % os.getcwd())

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []  # Return the list of duplicates in this data structure

# Replace the nested for loops below with your improvements
tree = BinarySearchTree('Testing')

for name in names_1:
    tree.insert(name)
print('done')
for name in names_2:
    found_name = tree.contains(name)
    if found_name is not None:
        duplicates.append(found_name)

print('done')

# for name_1 in names_1:
# for name_2 in names_2:
# if name_1 == name_2:
# duplicates.append(name_1)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")


# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish?  Thare are no restrictions on techniques or data
# structures, but you may not import any additional libraries that you did not write yourself.
