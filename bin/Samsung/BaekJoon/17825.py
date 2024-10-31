from itertools import permutations

import copy

aa = [[1,2],[3,4],[5,6]]
bb = copy.deepcopy(aa)
cc = [i[:] for i in aa]
dd = aa
print(id(dd))
print(id(aa))
print(id(bb))
print(id(cc))
print(bb)
print(cc)

aa[0][0] = 3
print(aa)
print(bb)
print(cc)