def enemyBoats():
    #PRINTS A BOAT MATRIX
    columns = ' abcdefghij'
    for number in columns:
        print(number, end=" ")
    print()
    for letter, value in enumerate(matrix):
        print(letter, end=' ')
        for cell in value:
            print(cell, end=' ')
        print()


matrix = [['W' for x in range(10)] for x in range(10)]
enemyBoats()

