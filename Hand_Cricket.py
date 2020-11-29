print('--------------------------------------------------------------------------')
print('Welcome to IPL 2020.')
import random

# Variables to Store score u for Team_1 and c for Team_2.
u = 0
c = 0

# Selection of Teams:
print('CSK, MI, RCB, DC, KXIP, KKR, SRH, RR.')
Team_1 = input('Select your Favourite Team: ').upper()
Team_2 = input('Select Opponent Team: ').upper()

# Toss
print('\n######### TOSS #########')
T = input("Select H for Head or T for Tail: ").capitalize()
comp_toss = random.choice(['H', 'T'])
print(comp_toss)

# If Team_1 won the Toss and choose to Bat First.
if comp_toss == T:
    print(Team_1, 'won the toss.')
    A = int(input('Choose 1 for Batting and 2 for Bowling: '))
    if A == 1:
        print(Team_1, 'will bat first.')
        while True:
            # Team_1 is Batting.
            print('--------------------------------')
            print('1, 2, 3, 4, 5, 6')
            user_ip = int(input('Select any one: '))

            while user_ip not in (1, 2, 3, 4, 5, 6):
                print('Invalid IP.')
                user_ip = int(input('Select any one: '))

            # Team_2 is Bowling.
            comp_ip = random.choice([1, 2, 3, 4, 5, 6])
            print('Computer:', comp_ip)

            if user_ip != comp_ip:
                u += user_ip
                print(Team_1, '_score: ', u)

            elif user_ip == comp_ip:
                print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                print('Out!!!!!')
                print(Team_1, 'Final Score:', u)
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

                choice = int(input('Ready for 2nd innings??? (Select 1 if Yes and 2 if No.): '))
                while choice not in (1, 2):
                    print('Invalid Choice.')
                    choice = int(input('Ready for 2nd innings??? (Select 1 if Yes and 2 if No.): '))

                if choice == 2:
                    print('You have choose to exit the Game.')
                    exit()

                else:
                    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print('2nd Innings began.')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

                while c < u:
                    print('--------------------------------')
                    print(Team_2, 'need to score', u - c, 'runs to win the match.')
                    print('1, 2, 3, 4, 5, 6')
                    user_ip2 = int(input('Select any one: '))

                    while user_ip2 not in (1, 2, 3, 4, 5, 6):
                        print('Invalid IP.')
                        user_ip2 = int(input('Select any one: '))

                    comp_ip2 = random.choice([1, 2, 3, 4, 5, 6])
                    print('Computer:', comp_ip2)

                    if comp_ip2 != user_ip2:
                        c += comp_ip2
                        print('computer_score: ', c)
                        if c > u:
                            print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                            print(Team_1, 'Final Score:', u)
                            print(Team_2, 'Final Score:', c)
                            print(Team_2, 'Win the match.')
                            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
                            exit()

                    elif comp_ip2 == user_ip2:
                        print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        print('Out!!!!!')
                        print(Team_2, 'Final Score:', c)
                        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        break

                if u > c:
                    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print(Team_1, 'Final Score:', u)
                    print(Team_2, 'Final Score:', c)
                    print(Team_1, 'win the match by difference of', u - c, 'runs.')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    exit()


    # If Team_1 won the Toss and choose to Bowl First.
    elif A == 2:
        print(Team_1, 'will bowl first.')
        while True:
            print('--------------------------------')
            print('1, 2, 3, 4, 5, 6')
            user_ip = int(input('Select any one: '))

            while user_ip not in (1, 2, 3, 4, 5, 6):
                print('Invalid IP.')
                user_ip = int(input('Select any one: '))

            comp_ip = random.choice([1, 2, 3, 4, 5, 6])
            print('Computer:', comp_ip)

            if comp_ip != user_ip:
                c += comp_ip
                print(Team_2, '_score: ', c)

            elif comp_ip == user_ip:
                print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                print('Out!!!!!')
                print(Team_2, 'Final Score:', c)
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

                choice = int(input('Ready for 2nd innings??? (Select 1 if Yes and 2 if No.): '))
                while choice not in (1, 2):
                    print('Invalid Choice.')
                    choice = int(input('Ready for 2nd innings??? (Select 1 if Yes and 2 if No.): '))

                if choice == 2:
                    print('You have choose to exit the Game.')
                    exit()

                else:
                    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print('2nd Innings began.')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

                while u < c:
                    print('--------------------------------')
                    print(Team_1, 'need to score', c - u, 'runs to win the match.')
                    print('1, 2, 3, 4, 5, 6')
                    user_ip2 = int(input('Select any one: '))

                    while user_ip2 not in (1, 2, 3, 4, 5, 6):
                        print('Invalid IP.')
                        user_ip2 = int(input('Select any one: '))

                    comp_ip2 = random.choice([1, 2, 3, 4, 5, 6])
                    print('Computer:', comp_ip2)

                    if user_ip2 != comp_ip2:
                        u += user_ip2
                        print(Team_1, '_score: ', u)
                        if u >= c:
                            print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                            print(Team_2, 'Final Score:', c)
                            print(Team_1, 'Final Score:', u)
                            print(Team_1, 'Win the match.')
                            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
                            exit()

                    elif user_ip2 == comp_ip2:
                        print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        print('Out!!!!!')
                        print(Team_1, 'Final Score:', u)
                        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        break

                if c > u:
                    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print(Team_1, 'Final Score:', u)
                    print(Team_2, 'Final Score:', c)
                    print(Team_2, 'win the match by difference of', c - u, 'runs.')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    exit()


# If Team_2 won the Toss.
else:
    print(Team_1, 'lost the toss.')
    comp_team2 = random.choice(['Bat', 'Bowl'])
    print(Team_2, 'Will', comp_team2, 'first.')

    # If Team_2 won the Toss and choose to Bat First.
    if comp_team2 == 'Bat':

        while True:
            print('--------------------------------')
            print('1, 2, 3, 4, 5, 6')
            user_ip = int(input('Select any one: '))

            while user_ip not in (1, 2, 3, 4, 5, 6):
                print('Invalid IP.')
                user_ip = int(input('Select any one: '))

            comp_ip = random.choice([1, 2, 3, 4, 5, 6])
            print('Computer:', comp_ip)

            if comp_ip != user_ip:
                c += comp_ip
                print(Team_2, '_score: ', c)

            elif comp_ip == user_ip:
                print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                print('Out!!!!!')
                print(Team_2, 'Final Score:', c)
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

                choice = int(input('Ready for 2nd innings??? (Select 1 if Yes and 2 if No.): '))
                while choice not in (1, 2):
                    print('Invalid Choice.')
                    choice = int(input('Ready for 2nd innings??? (Select 1 if Yes and 2 if No.): '))

                if choice == 2:
                    print('You have choose to exit the Game.')
                    exit()

                else:
                    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print('2nd Innings began.')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

                while u < c:
                    print('--------------------------------')
                    print(Team_1, 'need to score', c - u, 'runs to win the match.')
                    print('1, 2, 3, 4, 5, 6')
                    user_ip2 = int(input('Select any one: '))

                    while user_ip2 not in (1, 2, 3, 4, 5, 6):
                        print('Invalid IP.')
                        user_ip2 = int(input('Select any one: '))

                    comp_ip2 = random.choice([1, 2, 3, 4, 5, 6])
                    print('Computer:', comp_ip2)

                    if user_ip2 != comp_ip2:
                        u += user_ip2
                        print(Team_1, '_score: ', u)
                        if u >= c:
                            print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                            print(Team_2, 'Final Score:', c)
                            print(Team_1, 'Final Score:', u)
                            print(Team_1, 'Win the match.')
                            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
                            exit()

                    elif user_ip2 == comp_ip2:
                        print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        print('Out!!!!!')
                        print(Team_1, 'Final Score:', u)
                        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        break

                if c > u:
                    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print(Team_1, 'Final Score:', u)
                    print(Team_2, 'Final Score:', c)
                    print(Team_2, 'win the match by difference of', c - u, 'runs.')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    exit()


    # If Team_2 won the Toss and choose to Bowl First.
    elif comp_team2 == 'Bowl':

        while True:
            print('--------------------------------')
            print('1, 2, 3, 4, 5, 6')
            user_ip = int(input('Select any one: '))

            while user_ip not in (1, 2, 3, 4, 5, 6):
                print('Invalid IP.')
                user_ip = int(input('Select any one: '))

            comp_ip = random.choice([1, 2, 3, 4, 5, 6])
            print('Computer:', comp_ip)

            if user_ip != comp_ip:
                u += user_ip
                print(Team_1, 'score: ', u)

            elif user_ip == comp_ip:
                print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                print('Out!!!!!')
                print(Team_1, 'Final Score:', u)
                print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

                choice = int(input('Ready for 2nd innings??? (Select 1 if Yes and 2 if No.): '))
                while choice not in (1, 2):
                    print('Invalid Choice.')
                    choice = int(input('Ready for 2nd innings??? (Select 1 if Yes and 2 if No.): '))

                if choice == 2:
                    print('You have choose to exit the Game.')
                    exit()

                else:
                    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print('2nd Innings began.')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')

                while c < u:
                    print('--------------------------------')
                    print(Team_2, 'need to score', u - c, 'runs to win the match.')
                    print('1, 2, 3, 4, 5, 6')
                    user_ip2 = int(input('Select any one: '))

                    while user_ip2 not in (1, 2, 3, 4, 5, 6):
                        print('Invalid IP.')
                        user_ip2 = int(input('Select any one: '))

                    comp_ip2 = random.choice([1, 2, 3, 4, 5, 6])
                    print('Computer:', comp_ip2)

                    if comp_ip2 != user_ip2:
                        c += comp_ip2
                        print('computer_score: ', c)
                        if c > u:
                            print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                            print(Team_1, 'Final Score:', u)
                            print(Team_2, 'Final Score:', c)
                            print(Team_2, 'Win the match.')
                            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n')
                            exit()

                    elif comp_ip2 == user_ip2:
                        print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        print('Out!!!!!')
                        print(Team_2, 'Final Score:', c)
                        print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                        break

                if u > c:
                    print('\n$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    print(Team_1, 'Final Score:', u)
                    print(Team_2, 'Final Score:', c)
                    print(Team_1, 'win the match by difference of', u - c, 'runs.')
                    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
                    exit()