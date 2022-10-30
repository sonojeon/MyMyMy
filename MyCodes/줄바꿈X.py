for x in range(1,5):
    for y in range (1,5):
        print (x, 'X', y, '=', x*y, end='')
        if x==4 and y==4:
            break
        print(', ', end='')
