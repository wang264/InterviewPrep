# https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/


# importing copy module
import copy

# initializing list 1
li1 = [1, 2, [3, 5], 4]

# if we create a reference
reference = li1

# using copy for shallow copy
li2 = copy.copy(li1)

# using deepcopy for deepcopy
li3 = copy.deepcopy(li1)

id(reference)
id(li1)
id(reference) == id(li1)
# we can see that 'reference' and 'li1'actually point to the same list

# how about li1 and li2
id(li1)
id(li2)
id(li1) == id(li2)
# hmm, so li1 and li2 is different list.
# however, notice that they are list of list, the third element is a list.
id(li1[2]) == id(li2[2])
# they are actually the same list.
li1[2].append(4)
li2[2]


# how about li1 and li3
id(li1)
id(li3)
id(li1) == id(li3)
# hmm, so li1 and li3 is different list.
# however, notice that they are list of list, the third element is a list.
id(li1[2]) == id(li3[2])
# they are actually different list.
li1[2].append(4)
li3[2]


