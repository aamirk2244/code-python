import numpy as np
def print_coordinate(a):
    oneDim = list(a.reshape(a.size))
    where = np.where(a)         # will get all indexes
    size = len(where)
    tail = len(where[0])
    print('printing {} dimentional Array'.format(len(where)))
    head = 0
    saveIndex = []
    while head != tail:
        for element in range(size):
            saveIndex.append(where[element][head])
        print('{} = {}'.format( tuple(saveIndex), oneDim.pop(0)))

        head += 1
        saveIndex = []
    
d4 = np.array([[[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]], [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]], [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]], [[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]]])
print_coordinate(d4)
d3 = np.array([[[1,2,3],[4,5,6]],
                [[7,8,9],[10,11,12]]])
print_coordinate(d3)
