from random_list import random_list_generator
from merge_sort import merge_sort, verify_sorted

l = random_list_generator(10, 1000)
# Output: [852, 206, 404, 578, 445, 310, 74, 191, 357, 476]

sorted = merge_sort(l)

verify_sorted(l)
# Output: False

verify_sorted(sorted)
# Output: True
