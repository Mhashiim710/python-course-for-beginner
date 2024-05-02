import copy
l1 = [['Hashim', 24], [1, 3]]

print('List 1')
print(f'Address of List 1 = {hex(id(l1))}')
print(f'Address of List 1[0] index = {hex(id(l1[0]))}')
print(f'Address of List 1[0] index item[0] = {hex(id(l1[0][0]))}')
print(f'Address of List 1[0] index item[1] = {hex(id(l1[0][1]))}')
print('-----------------------------------------------------------')
print(f'Address of List 1[1] index = {hex(id(l1[1]))}')
print(f'Address of List 1[1] index item[0] = {hex(id(l1[1][0]))}')
print(f'Address of List 1[1] index item[1] = {hex(id(l1[1][1]))}')
print('-----------------------------------------------------------')
print('End of the first list')

l2 = copy.deepcopy(l1)
print('List 2')
print(f'Address of List 2 = {hex(id(l2))}')
print(f'Address of List 2[0] index = {hex(id(l2[0]))}')
print(f'Address of List 2[0] index item[0] = {hex(id(l2[0][0]))}')
print(f'Address of List 2[0] index item[1] = {hex(id(l2[0][1]))}')
print('-----------------------------------------------------------')
print(f'Address of List 2[1] index = {hex(id(l2[1]))}')
print(f'Address of List 2[1] index item[0] = {hex(id(l2[1][0]))}')
print(f'Address of List 2[1] index item[1] = {hex(id(l2[1][1]))}')
print('-----------------------------------------------------------')
print('End of the Second list')

print(l1)
print(l2)
l2[0] = 'a'
print(l2)
print(l1)