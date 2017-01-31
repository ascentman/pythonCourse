import itertools

my_list = [[1,2,3],[4,5,6], [7], [8,9]]

flattened_list = list(itertools.chain.from_iterable(my_list))
print(flattened_list)