def is_circular(path):
    x = 0
    y = 0
    for i in range(len(path)):
        move = path[i]
        if move == 'R':
            x = x + 1
        elif move == 'L':
            x = x - 1
        elif move == 'U':
            y = y + 1
        elif move == 'D':
            y = y - 1
    return x, y


path = "UULLRRDD"
z = is_circular(path)
print(z)
if z == (0, 0):
    print('Circular')
else:
    print('NOT circular')
