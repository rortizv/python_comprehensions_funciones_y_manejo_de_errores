set_a = { 'col', 'mex', 'usa', 'uru', 'bol' }
set_b = { 'col', 'uru', 'bra', 'arg', 'par' }

set_c = set_a.union(set_b)
print('Union', set_c)

set_d = set_a.intersection(set_b)
print('Intersection', set_d)
print('Intersection using &', set_a & set_b)

set_e = set_a.difference(set_b)
print('Difference', set_e)
print('Difference using -', set_a - set_b)

set_f = set_a.symmetric_difference(set_b)
print('Symmetric difference', set_f)
print('Symmetric difference using ^', set_a ^ set_b)