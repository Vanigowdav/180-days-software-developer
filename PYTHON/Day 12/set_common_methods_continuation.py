# 4. issubset and superset : These methods check if set is subset or superset of another set.
my_set = {1, 2, 3, 4, 5}
your_set = { 2, 3, 4, 6}
print(my_set.issuperset(your_set))              # print False bcz my_set does not have all the elements of yourset.
print(your_set.issubset(my_set))               #print False bcz not all the elements of yourset are in myset

# 5. isdisjoint() method : checks if two sets are disjoint means do not have any elements in common. 
print(my_set.isdisjoint(your_set))

# 6. union() : returns a new set with all the elements from both sets. 
# operator = |
print(my_set | your_set)


# 6. intersection() : returns only the common elements from both sets. 
# operator = &
print(my_set & your_set)


# 6. Difference() : returns elements of  first set that are not in other set. 
# operator = -
print(my_set - your_set)


# 6. symmetric difference() : returns a new set with  the elements that are either in the first oro the second set but not in both. 
# operator = ^
print(my_set ^ your_set)

