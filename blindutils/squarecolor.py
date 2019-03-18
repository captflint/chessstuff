#!/usr/bin/env python3

import random, time

squares = []

for rank in range(1, 9):

    for file in range(1, 9):

        if rank % 2 == 1:

            if file % 2 == 1:

                color = 'dark'

            else:

                color = 'light'

        else:

            if file % 2 == 1:

                color = 'light'

            else:

                color = 'dark'
                
        sq = 'abcdefgh'[file - 1] + str(rank)
        squares.append((sq, color))

random.shuffle(squares)

mistakes = 0
t = int(time.time())

while squares:

    q = squares.pop()

    print('\n' * 100)
    a = input(q[0] + '? ')

    a = a.casefold()
    a = a[0]

    if a == 'w':
        a = 'l'

    if a == 'b':
        a = 'd'

    if a == q[1][0]:

        pass

    else:

        squares.append(q)
        squares.append(q)
        random.shuffle(squares)
        mistakes += 1

        input("Incorrect :( ")

t = int(time.time()) - t
print('\n' * 100)
print('You made', mistakes, 'mistake(s).')

if not mistakes:
    print('Great job!  ^_^')

print('You completed the test in', t // 60, 'minute(s) and', t % 60, 'second(s).')
