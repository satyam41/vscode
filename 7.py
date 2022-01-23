"""Tuple is also a type of data storage, It is use to store data and it is immutable means it not changeable.
empty_tuple = ()
non_empty_tuple = (1,2,3,4,5)
non_empty_tuple_single_element = (1,)

functions of tuple:
    1.tuple.index()
    2.tuple.count()

tup = (1,2,3,2,4,5) # it cannot change.
print(tup)

print(tup.index(3))

print(tup.count(2))
"""

# Difference between List and Tuple
# List is mutable and tuple is immutable.
# list is written as [] and tuples is written in ()
tuple_name = ("Satyam", "Anubhav", "Anuj", "Sanmati")
list_name = ["Satyam", "Anubhav", "Anuj", "Sanmati"]
print(tuple_name.__sizeof__())
print(list_name.__sizeof__())