def enemyBoats():
    #PRINTS A BOAT MATRIX
    columns = ' ABCDEFGHIJ'
    for number in columns:
        print(number, end=" ")
    print()
    for letter, value in enumerate(matrix):
        print(letter, end=' ')
        for cell in value:
            print(cell, end=' ')
        print()


matrix = [['M' for x in range(10)] for x in range(10)]
print(matrix)
enemyBoats()

